import numpy as np
from scipy.stats import zscore
import streamlit as st
from sklearn.decomposition import PCA
import plotly.express as px
import pandas as pd

def outlier_detection(df, num_cols):
    for col in num_cols:
        z_scores = np.abs(zscore(df[col].dropna()))
        outliers = (z_scores > 3).sum()
        st.write(f"📌 {col} has {outliers} outliers (z > 3)")

def pca_viz(df, num_cols):
    if len(num_cols) >= 2:
        pca = PCA(n_components=2)
        pc = pca.fit_transform(df[num_cols].fillna(0))
        df_pca = pd.DataFrame(data=pc, columns=['PC1', 'PC2'])
        fig = px.scatter(df_pca, x='PC1', y='PC2', title="📉 PCA - 2D Projection of Numerical Features")
        st.plotly_chart(fig)
