# utils/stats_analysis.py

import pandas as pd
from scipy.stats import f_oneway, chi2_contingency, pearsonr

def perform_anova(df, num_cols, cat_cols, st):
    st.subheader("📐 ANOVA Tests")
    if len(cat_cols) >= 1 and len(num_cols) >= 1:
        for cat in cat_cols:
            try:
                groups = [df[df[cat] == level][num_cols[0]] for level in df[cat].dropna().unique()]
                if len(groups) > 1:
                    anova = f_oneway(*groups)
                    st.write(f"ANOVA for {num_cols[0]} across {cat}: p = {anova.pvalue:.4f}")
            except:
                continue

def perform_chi_square(df, cat_cols, st):
    st.subheader("📊 Chi-Square Tests")
    if len(cat_cols) >= 2:
        try:
            table = pd.crosstab(df[cat_cols[0]], df[cat_cols[1]])
            chi2, p, _, _ = chi2_contingency(table)
            st.write(f"Chi-Square between {cat_cols[0]} and {cat_cols[1]}: p = {p:.4f}")
        except:
            st.warning("⚠️ Chi-Square test failed due to data formatting issues.")

def perform_pearson(df, num_cols, st):
    st.subheader("📈 Pearson Correlation")
    if len(num_cols) >= 2:
        try:
            corr, _ = pearsonr(df[num_cols[0]], df[num_cols[1]])
            st.write(f"Pearson Correlation between {num_cols[0]} and {num_cols[1]}: {corr:.2f}")
        except:
            st.warning("⚠️ Pearson correlation failed due to missing or invalid data.")
