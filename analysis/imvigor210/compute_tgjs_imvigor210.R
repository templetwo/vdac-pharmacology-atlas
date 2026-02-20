#!/usr/bin/env Rscript
# =============================================================================
# tGJS Analysis: IMvigor210 Atezolizumab Cohort — Supplementary Analysis S3
# =============================================================================
# Tests whether the transcriptomic Gate-Jamming Score (tGJS) predicts
# atezolizumab response in the Mariathasan 2018 urothelial carcinoma cohort.
#
# Data: IMvigor210CoreBiologies R package (CC-BY 3.0)
# Ref:  Mariathasan et al., Nature 554:544-548, 2018
#
# Key tests:
#   1. tGJS vs binary response (logistic regression)
#   2. tGJS vs RECIST 4-level response (Kruskal-Wallis)
#   3. tGJS × TMB interaction (primary hypothesis)
#   4. tGJS × immune phenotype interaction
#   5. Overall survival by tGJS (Kaplan-Meier + Cox)
#   6. Component-level analysis (HK2, BCL2L1, TSPO individually)
# =============================================================================

suppressWarnings(suppressPackageStartupMessages({
  library(Biobase)
  library(survival)
  library(ggplot2)
  library(dplyr)
}))

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR <- dirname(normalizePath(commandArgs(trailingOnly=FALSE)[
  grep("--file=", commandArgs(trailingOnly=FALSE))] |>
  sub("--file=", "", x=_), mustWork=FALSE))
if (nchar(SCRIPT_DIR) == 0) SCRIPT_DIR <- getwd()

DATA_DIR   <- file.path(SCRIPT_DIR, "data")
PLOT_DIR   <- file.path(SCRIPT_DIR, "figures")
dir.create(DATA_DIR,  showWarnings=FALSE, recursive=TRUE)
dir.create(PLOT_DIR,  showWarnings=FALSE, recursive=TRUE)

cat("=============================================================\n")
cat("tGJS ANALYSIS — IMvigor210 ATEZOLIZUMAB (Supplementary S3)\n")
cat("=============================================================\n\n")

# ── 1. Load Data ─────────────────────────────────────────────────────────────
cat("[1] Loading IMvigor210 data...\n")
suppressWarnings(
  load("/tmp/imvigor210/IMvigor210CoreBiologies/data/cds.RData")
)

# Extract via S4 slots (no DESeq package needed)
counts_mat <- cds@assayData[["counts"]]    # 31286 x 348, rows=Entrez IDs
fdat       <- cds@featureData@data         # gene annotations
pdat       <- cds@phenoData@data           # clinical data

cat(sprintf("  Counts: %d genes × %d samples\n", nrow(counts_mat), ncol(counts_mat)))
cat(sprintf("  Clinical variables: %s\n", ncol(pdat)))

# ── 2. TPM Normalization ──────────────────────────────────────────────────────
cat("\n[2] Normalizing to TPM...\n")
gene_lengths <- fdat$length
gene_lengths[is.na(gene_lengths) | gene_lengths == 0] <- median(
  fdat$length[fdat$length > 0], na.rm=TRUE
)

# TPM: divide by gene length (kb), then normalize to per-million
rpk        <- counts_mat / (gene_lengths / 1000)
tpm_mat    <- t(t(rpk) / colSums(rpk, na.rm=TRUE)) * 1e6

cat(sprintf("  TPM matrix: %d × %d\n", nrow(tpm_mat), ncol(tpm_mat)))

# ── 3. Extract tGJS Genes ────────────────────────────────────────────────────
cat("\n[3] Extracting tGJS genes...\n")
sym <- fdat$symbol

find_gene <- function(gene_sym) {
  idx <- which(sym == gene_sym)
  if (length(idx) == 0) {
    cat(sprintf("  WARNING: %s not found by symbol, trying Symbol column\n", gene_sym))
    idx <- which(fdat$Symbol == gene_sym)
  }
  if (length(idx) == 0) stop(sprintf("Gene %s not found", gene_sym))
  if (length(idx) > 1) idx <- idx[1]
  idx
}

hk2_idx    <- find_gene("HK2")
bcl2l1_idx <- find_gene("BCL2L1")
tspo_idx   <- find_gene("TSPO")

hk2_tpm    <- as.numeric(tpm_mat[hk2_idx,    ])
bcl2l1_tpm <- as.numeric(tpm_mat[bcl2l1_idx, ])
tspo_tpm   <- as.numeric(tpm_mat[tspo_idx,   ])

cat(sprintf("  HK2:    median TPM = %.2f\n", median(hk2_tpm,    na.rm=TRUE)))
cat(sprintf("  BCL2L1: median TPM = %.2f\n", median(bcl2l1_tpm, na.rm=TRUE)))
cat(sprintf("  TSPO:   median TPM = %.2f\n", median(tspo_tpm,   na.rm=TRUE)))

# ── 4. Compute tGJS ──────────────────────────────────────────────────────────
cat("\n[4] Computing tGJS (z-score weighted)...\n")
hk2_z    <- as.numeric(scale(hk2_tpm))
bcl2l1_z <- as.numeric(scale(bcl2l1_tpm))
tspo_z   <- as.numeric(scale(tspo_tpm))

tGJS <- 0.40 * hk2_z + 0.30 * bcl2l1_z + 0.30 * tspo_z
names(tGJS) <- colnames(tpm_mat)

cat(sprintf("  tGJS: mean=%.3f  sd=%.3f  range=[%.3f, %.3f]\n",
    mean(tGJS, na.rm=TRUE), sd(tGJS, na.rm=TRUE),
    min(tGJS, na.rm=TRUE), max(tGJS, na.rm=TRUE)))

# ── 5. Assemble Clinical Data ─────────────────────────────────────────────────
cat("\n[5] Assembling clinical data...\n")
clin <- pdat
clin$tGJS      <- tGJS
clin$HK2_tpm   <- hk2_tpm
clin$BCL2L1_tpm<- bcl2l1_tpm
clin$TSPO_tpm  <- tspo_tpm
clin$tGJS_high <- ifelse(tGJS > median(tGJS, na.rm=TRUE), "High", "Low")
clin$tGJS_tertile <- cut(tGJS,
  breaks = quantile(tGJS, c(0, 1/3, 2/3, 1), na.rm=TRUE),
  labels = c("Low", "Mid", "High"), include.lowest=TRUE)

# TMB
tmb_col <- "FMOne mutation burden per MB"
clin$TMB <- as.numeric(clin[[tmb_col]])
clin$TMB_group <- ifelse(is.na(clin$TMB), NA,
                  ifelse(clin$TMB >= 10, "TMB-high", "TMB-low"))

# Response
clin$response4 <- as.character(clin$`Best Confirmed Overall Response`)
clin$resp_bin  <- as.integer(clin$binaryResponse == "CR/PR")

cat(sprintf("  N = %d samples\n", nrow(clin)))
cat("  Response distribution:\n")
print(table(clin$response4, useNA="ifany"))
cat("  Binary response:\n")
print(table(clin$resp_bin, useNA="ifany"))
cat("  TMB group:\n")
print(table(clin$TMB_group, useNA="ifany"))
cat("  Immune phenotype:\n")
print(table(clin$`Immune phenotype`, useNA="ifany"))

# ── 6. Primary Test: tGJS vs Binary Response ─────────────────────────────────
cat("\n[6] Primary test: tGJS vs binary response...\n")

complete_resp <- clin[!is.na(clin$resp_bin) & !is.na(clin$tGJS), ]
cat(sprintf("  N with response + tGJS: %d\n", nrow(complete_resp)))

# Wilcoxon (non-parametric)
cr_pr <- complete_resp$tGJS[complete_resp$resp_bin == 1]
sd_pd <- complete_resp$tGJS[complete_resp$resp_bin == 0]
wtest <- wilcox.test(cr_pr, sd_pd)
cat(sprintf("  CR/PR mean tGJS: %.3f (n=%d)\n", mean(cr_pr), length(cr_pr)))
cat(sprintf("  SD/PD mean tGJS: %.3f (n=%d)\n", mean(sd_pd), length(sd_pd)))
cat(sprintf("  Wilcoxon p = %.4f\n", wtest$p.value))

# Logistic regression
logit1 <- glm(resp_bin ~ tGJS, data=complete_resp, family="binomial")
s1 <- summary(logit1)
or_tgjs <- exp(coef(logit1)["tGJS"])
p_logit  <- s1$coefficients["tGJS", "Pr(>|z|)"]
cat(sprintf("  Logistic: OR = %.3f, p = %.4f\n", or_tgjs, p_logit))

# Spearman correlation with continuous RECIST
resp_num <- c("CR"=4, "PR"=3, "SD"=2, "PD"=1)
complete_resp$resp_num <- resp_num[complete_resp$response4]
sp <- cor.test(complete_resp$tGJS, complete_resp$resp_num,
               method="spearman", exact=FALSE)
cat(sprintf("  Spearman rho vs RECIST: %.3f, p = %.4f\n", sp$estimate, sp$p.value))

# ── 7. RECIST Distribution by tGJS Tertile ───────────────────────────────────
cat("\n[7] RECIST distribution by tGJS tertile...\n")
tert_resp <- table(complete_resp$tGJS_tertile,
                   complete_resp$response4)[, c("CR","PR","SD","PD")]
print(tert_resp)
resp_rate_by_tert <- tapply(complete_resp$resp_bin, complete_resp$tGJS_tertile,
                            function(x) round(mean(x, na.rm=TRUE)*100, 1))
cat("  Response rate (%) by tertile:\n")
print(resp_rate_by_tert)

kw <- kruskal.test(resp_num ~ tGJS_tertile, data=complete_resp)
cat(sprintf("  Kruskal-Wallis p = %.4f\n", kw$p.value))

# ── 8. TMB Interaction — Primary Hypothesis ───────────────────────────────────
cat("\n[8] TMB interaction (primary hypothesis)...\n")
tmb_sub <- complete_resp[!is.na(complete_resp$TMB_group), ]
cat(sprintf("  N with TMB data: %d\n", nrow(tmb_sub)))

# tGJS in TMB-low vs TMB-high
for (grp in c("TMB-low", "TMB-high")) {
  sub <- tmb_sub[tmb_sub$TMB_group == grp, ]
  w   <- wilcox.test(tGJS ~ resp_bin, data=sub)
  sp  <- cor.test(sub$tGJS, sub$resp_num, method="spearman", exact=FALSE)
  rr  <- mean(sub$resp_bin, na.rm=TRUE)
  cat(sprintf("  %s (n=%d, RR=%.0f%%): tGJS Wilcoxon p=%.4f, Spearman rho=%.3f p=%.4f\n",
      grp, nrow(sub), rr*100, w$p.value, sp$estimate, sp$p.value))
}

# Interaction logistic
logit_int <- glm(resp_bin ~ tGJS * TMB_group, data=tmb_sub, family="binomial")
s_int <- summary(logit_int)
int_row <- grep("tGJS:TMB_group", rownames(s_int$coefficients))
if (length(int_row) > 0) {
  p_int <- s_int$coefficients[int_row, "Pr(>|z|)"]
  cat(sprintf("  Interaction term p = %.4f\n", p_int))
}

# ── 9. Immune Phenotype Stratification ───────────────────────────────────────
cat("\n[9] Immune phenotype stratification...\n")
for (phen in c("inflamed", "excluded", "desert")) {
  sub <- complete_resp[tolower(complete_resp$`Immune phenotype`) == phen, ]
  if (nrow(sub) < 10) next
  sp <- tryCatch(cor.test(sub$tGJS, sub$resp_num, method="spearman", exact=FALSE),
                 error=function(e) NULL)
  rr <- mean(sub$resp_bin, na.rm=TRUE)
  cat(sprintf("  %s (n=%d, RR=%.0f%%): Spearman rho=%.3f p=%.4f\n",
      phen, nrow(sub), rr*100,
      if(!is.null(sp)) sp$estimate else NA,
      if(!is.null(sp)) sp$p.value else NA))
}

# ── 10. Overall Survival by tGJS ─────────────────────────────────────────────
cat("\n[10] Overall survival analysis...\n")
surv_sub <- clin[!is.na(clin$os) & !is.na(clin$censOS) & !is.na(clin$tGJS), ]
cat(sprintf("  N with OS data: %d (events: %d)\n",
    nrow(surv_sub), sum(surv_sub$censOS == 0, na.rm=TRUE)))

# Cox: tGJS continuous
cox1 <- coxph(Surv(os, 1 - censOS) ~ tGJS, data=surv_sub)
s_cox <- summary(cox1)
hr <- s_cox$conf.int["tGJS", "exp(coef)"]
hr_lo <- s_cox$conf.int["tGJS", "lower .95"]
hr_hi <- s_cox$conf.int["tGJS", "upper .95"]
p_cox <- s_cox$coefficients["tGJS", "Pr(>|z|)"]
cat(sprintf("  tGJS continuous HR = %.3f (95%% CI: %.3f-%.3f), p = %.4f\n",
    hr, hr_lo, hr_hi, p_cox))

# Cox: multivariate (tGJS + TMB + IC Level)
cox2 <- tryCatch(
  coxph(Surv(os, 1-censOS) ~ tGJS + TMB + `IC Level`, data=surv_sub),
  error=function(e) NULL
)
if (!is.null(cox2)) {
  s_cox2 <- summary(cox2)
  cat("  Multivariate Cox (tGJS + TMB + IC Level):\n")
  for (v in rownames(s_cox2$coefficients)) {
    cat(sprintf("    %-15s HR=%.3f p=%.4f\n", v,
        s_cox2$conf.int[v,"exp(coef)"],
        s_cox2$coefficients[v,"Pr(>|z|)"]))
  }
}

# Log-rank: tGJS high vs low
lr <- survdiff(Surv(os, 1-censOS) ~ tGJS_high, data=surv_sub)
p_lr <- 1 - pchisq(lr$chisq, df=1)
cat(sprintf("  Log-rank (high vs low): p = %.4f\n", p_lr))

# Median OS
for (grp in c("High","Low")) {
  sub <- surv_sub[surv_sub$tGJS_high == grp, ]
  fit <- survfit(Surv(os, 1-censOS) ~ 1, data=sub)
  med_os <- quantile(fit, probs=0.5)$quantile
  cat(sprintf("  Median OS (%s tGJS): %.1f months\n", grp, med_os))
}

# ── 11. Component Analysis ───────────────────────────────────────────────────
cat("\n[11] Individual component analysis...\n")
for (gene in c("HK2","BCL2L1","TSPO")) {
  col <- paste0(gene, "_tpm")
  v   <- log2(complete_resp[[col]] + 1)
  sp  <- cor.test(v, complete_resp$resp_num, method="spearman", exact=FALSE)
  cat(sprintf("  log2(%s+1) vs RECIST: rho=%.3f p=%.4f\n",
      gene, sp$estimate, sp$p.value))
}

# ── 12. Save Results ─────────────────────────────────────────────────────────
cat("\n[12] Saving results...\n")

# Clinical + tGJS matrix
write.csv(clin[, c("tGJS","tGJS_high","tGJS_tertile","HK2_tpm","BCL2L1_tpm","TSPO_tpm",
                   "Best Confirmed Overall Response","binaryResponse","resp_bin",
                   "os","censOS","TMB","TMB_group",
                   "IC Level","TC Level","Immune phenotype",
                   "Lund","TCGA Subtype")],
          file=file.path(DATA_DIR, "imvigor210_tgjs_matrix.csv"), row.names=TRUE)

# Summary JSON
summary_list <- list(
  study      = "IMvigor210 (Mariathasan 2018)",
  n_samples  = nrow(clin),
  n_resp_data= nrow(complete_resp),
  tGJS_stats = list(mean=mean(tGJS,na.rm=T), sd=sd(tGJS,na.rm=T)),
  primary_test = list(
    wilcoxon_p = wtest$p.value,
    logistic_OR = or_tgjs,
    logistic_p  = p_logit,
    spearman_rho_vs_RECIST = as.numeric(sp$estimate),
    spearman_p  = sp$p.value
  ),
  survival = list(
    continuous_HR = hr,
    HR_95CI = c(hr_lo, hr_hi),
    cox_p   = p_cox,
    logrank_p = p_lr
  ),
  kw_tertile_p = kw$p.value
)

cat(jsonlite::toJSON(summary_list, pretty=TRUE, auto_unbox=TRUE),
    file=file.path(DATA_DIR, "imvigor210_tgjs_summary.json"))

cat(sprintf("  Saved to %s\n", DATA_DIR))

# ── 13. Figures ──────────────────────────────────────────────────────────────
cat("\n[13] Generating figures...\n")

theme_pub <- theme_bw(base_size=13) +
  theme(panel.grid.minor=element_blank(),
        strip.background=element_blank(),
        plot.title=element_text(face="bold", size=12))

# Fig S3a: tGJS by RECIST response
plot_df <- complete_resp[!is.na(complete_resp$response4), ]
plot_df$response4 <- factor(plot_df$response4, levels=c("CR","PR","SD","PD"))
resp_colors <- c("CR"="#1565C0","PR"="#42A5F5","SD"="#FFA726","PD"="#E53935")

p1 <- ggplot(plot_df, aes(x=response4, y=tGJS, fill=response4)) +
  geom_violin(alpha=0.7, draw_quantiles=0.5) +
  geom_jitter(width=0.15, size=1, alpha=0.5) +
  scale_fill_manual(values=resp_colors, guide="none") +
  labs(title="tGJS by RECIST Response (IMvigor210, n=348)",
       subtitle=sprintf("Spearman ρ = %.3f, p = %.4f | Wilcoxon p = %.4f",
                        as.numeric(sp$estimate), sp$p.value, wtest$p.value),
       x="Best Confirmed Response", y="tGJS") +
  theme_pub
ggsave(file.path(PLOT_DIR, "figS3a_tgjs_by_recist.png"), p1, width=7, height=5, dpi=300)
ggsave(file.path(PLOT_DIR, "figS3a_tgjs_by_recist.svg"), p1, width=7, height=5)
cat("  Saved: figS3a\n")

# Fig S3b: Response rate by tGJS tertile
tert_rr <- complete_resp %>%
  filter(!is.na(tGJS_tertile)) %>%
  group_by(tGJS_tertile) %>%
  summarise(n=n(), resp_rate=mean(resp_bin,na.rm=T)*100,
            se=sd(resp_bin,na.rm=T)/sqrt(n)*100, .groups="drop")

p2 <- ggplot(tert_rr, aes(x=tGJS_tertile, y=resp_rate, fill=tGJS_tertile)) +
  geom_col(alpha=0.8) +
  geom_errorbar(aes(ymin=resp_rate-se, ymax=resp_rate+se), width=0.2) +
  geom_text(aes(label=sprintf("n=%d\n%.0f%%",n,resp_rate)), vjust=-0.5, size=3.5) +
  scale_fill_manual(values=c("Low"="#42A5F5","Mid"="#FFA726","High"="#E53935"),
                    guide="none") +
  labs(title="Atezolizumab Response Rate by tGJS Tertile",
       subtitle=sprintf("Kruskal-Wallis p = %.4f", kw$p.value),
       x="tGJS Tertile", y="CR/PR Rate (%)") +
  ylim(0, max(tert_rr$resp_rate) * 1.4) +
  theme_pub
ggsave(file.path(PLOT_DIR, "figS3b_response_rate_by_tertile.png"), p2, width=6, height=5, dpi=300)
ggsave(file.path(PLOT_DIR, "figS3b_response_rate_by_tertile.svg"), p2, width=6, height=5)
cat("  Saved: figS3b\n")

# Fig S3c: TMB interaction — tGJS vs response by TMB group
tmb_plt <- tmb_sub[!is.na(tmb_sub$response4), ]
tmb_plt$response4 <- factor(tmb_plt$response4, levels=c("CR","PR","SD","PD"))

p3 <- ggplot(tmb_plt, aes(x=response4, y=tGJS, fill=response4)) +
  geom_violin(alpha=0.7, draw_quantiles=0.5) +
  geom_jitter(width=0.15, size=1.2, alpha=0.6) +
  scale_fill_manual(values=resp_colors, guide="none") +
  facet_wrap(~TMB_group, labeller=label_both) +
  labs(title="tGJS vs Response Stratified by TMB",
       subtitle="Primary hypothesis: tGJS effect strongest in TMB-low",
       x="Best Confirmed Response", y="tGJS") +
  theme_pub
ggsave(file.path(PLOT_DIR, "figS3c_tgjs_tmb_interaction.png"), p3, width=9, height=5, dpi=300)
ggsave(file.path(PLOT_DIR, "figS3c_tgjs_tmb_interaction.svg"), p3, width=9, height=5)
cat("  Saved: figS3c\n")

# Fig S3d: Kaplan-Meier overall survival by tGJS (high vs low)
km_data <- surv_sub
km_data$tGJS_high <- factor(km_data$tGJS_high, levels=c("Low","High"))
km_fit  <- survfit(Surv(os, 1-censOS) ~ tGJS_high, data=km_data)

png(file.path(PLOT_DIR, "figS3d_km_os_by_tgjs.png"), width=700, height=550, res=120)
plot(km_fit, col=c("#1565C0","#E53935"), lwd=2,
     xlab="Overall Survival (months)", ylab="Survival probability",
     main=sprintf("OS by tGJS (IMvigor210)\nLog-rank p = %.4f | HR = %.2f (%.2f-%.2f)",
                  p_lr, hr, hr_lo, hr_hi))
legend("topright", legend=c("Low tGJS","High tGJS"),
       col=c("#1565C0","#E53935"), lwd=2, bty="n")
dev.off()
cat("  Saved: figS3d\n")

# Fig S3e: Component scatter (HK2, BCL2L1, TSPO vs tGJS)
comp_long <- rbind(
  data.frame(gene="HK2", expr=log2(complete_resp$HK2_tpm+1), tGJS=complete_resp$tGJS),
  data.frame(gene="BCL2L1", expr=log2(complete_resp$BCL2L1_tpm+1), tGJS=complete_resp$tGJS),
  data.frame(gene="TSPO",   expr=log2(complete_resp$TSPO_tpm+1),   tGJS=complete_resp$tGJS)
)
p5 <- ggplot(comp_long, aes(x=expr, y=tGJS)) +
  geom_point(alpha=0.3, size=1.2) +
  geom_smooth(method="lm", se=TRUE, color="red") +
  facet_wrap(~gene, scales="free_x") +
  labs(title="tGJS Components vs Composite Score",
       x="log2(TPM + 1)", y="tGJS") +
  theme_pub
ggsave(file.path(PLOT_DIR, "figS3e_tgjs_components.png"), p5, width=10, height=4, dpi=300)
ggsave(file.path(PLOT_DIR, "figS3e_tgjs_components.svg"), p5, width=10, height=4)
cat("  Saved: figS3e\n")

cat("\n=============================================================\n")
cat("INTERPRETATION SUMMARY\n")
cat("=============================================================\n")
cat(sprintf("\nPRIMARY TEST (n=%d with response data):\n", nrow(complete_resp)))
cat(sprintf("  tGJS vs binary response: Wilcoxon p=%.4f\n", wtest$p.value))
cat(sprintf("  Logistic OR = %.3f, p = %.4f\n", or_tgjs, p_logit))
cat(sprintf("  Spearman rho (vs RECIST): %.3f, p=%.4f\n",
    as.numeric(sp$estimate), sp$p.value))
if (p_logit < 0.05) {
  cat(sprintf("  DIRECTION: %s\n",
      if(or_tgjs < 1) "HIGH tGJS -> WORSE response (predicted)" else
      "HIGH tGJS -> BETTER response (unexpected)"))
} else {
  cat("  RESULT: Not statistically significant\n")
}

cat(sprintf("\nSURVIVAL:\n"))
cat(sprintf("  HR per 1-SD tGJS = %.3f (95%% CI: %.3f-%.3f), p=%.4f\n",
    hr, hr_lo, hr_hi, p_cox))
cat(sprintf("  Log-rank (high vs low): p=%.4f\n", p_lr))

cat(sprintf("\nKEY NUMBERS FOR S3 WRITEUP:\n"))
cat(sprintf("  N total: 348\n"))
cat(sprintf("  N with response: %d\n", nrow(complete_resp)))
cat(sprintf("  CR/PR mean tGJS: %.3f | SD/PD mean tGJS: %.3f\n",
    mean(cr_pr), mean(sd_pd)))
cat(sprintf("  Kruskal-Wallis (tertile): p=%.4f\n", kw$p.value))
cat(sprintf("  Multivariate HR (tGJS): %.3f, p=%.4f\n", hr, p_cox))
cat("=============================================================\n")
