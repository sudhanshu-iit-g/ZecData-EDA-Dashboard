import streamlit as st
import pandas as pd
import nltk

# Local module imports
from utils import (
    loader,
    type_detection,
    missing_handler,
    visualizer,
    stats_analysis,
    ts_analysis,
    sentiment_analysis,
    report_generator,
    outliers_pca
)
nltk.download('vader_lexicon')

st.set_page_config(page_title="📊 ZecData: Auto EDA Beast Dashboard", layout="wide")
st.title("📊 ZecData: Auto EDA Beast Dashboard with Everything Built-In")

# File Upload
st.sidebar.header("📂 Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file:
    df = loader.load_data(uploaded_file)
    st.success("✅ Dataset loaded successfully!")
    st.dataframe(df.head())

    # Detect and handle types
    data_types = type_detection.detect_data_types(df)
    df = missing_handler.handle_missing(df, data_types)

    # Split types
    num_cols = [col for col, t in data_types.items() if t == 'numerical']
    cat_cols = [col for col, t in data_types.items() if t == 'categorical']
    text_cols = [col for col, t in data_types.items() if t == 'text']
    date_cols = [col for col, t in data_types.items() if t == 'datetime']

    # Descriptive Stats
    st.subheader("📌 Descriptive Statistics")
    st.write(df.describe(include='all'))

    # Univariate Analysis
    st.subheader("📊 Univariate Analysis")
    visualizer.plot_histograms(df, num_cols, st)
    visualizer.plot_pie_charts(df, cat_cols, st)
    visualizer.plot_wordclouds(df, text_cols, st)

    # Bivariate Analysis
    st.subheader("🔁 Bivariate Analysis")
    visualizer.plot_correlation_heatmap(df, num_cols, st)
    visualizer.plot_boxplots(df, num_cols, cat_cols, st)

    # Statistical Tests
    st.subheader("📐 Statistical Tests")
    stats_analysis.perform_anova(df, num_cols, cat_cols, st)
    stats_analysis.perform_chi_square(df, cat_cols, st)
    stats_analysis.perform_pearson(df, num_cols, st)

    # Image list for final report
    image_list = visualizer.get_saved_images()

    # Time Series Analysis
    ts_analysis.analyze_time_series(df, date_cols, st, image_list)

    # Outlier Detection
    st.subheader("⚠️ Outlier Detection")
    outliers_pca.outlier_detection(df, num_cols)

    # PCA Visualization
    st.subheader("📉 PCA Visualization")
    outliers_pca.pca_viz(df, num_cols)

    # Sentiment Analysis (adds images to image_list for PDF)
    sentiment_analysis.analyze_text_columns(df, text_cols, st, image_list)

    # Export Report
    report_generator.generate_pdf_report(df, data_types, image_list, st)

else:
    st.warning("⚠️ Please upload a CSV file to start analysis.")