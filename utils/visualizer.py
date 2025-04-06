# utils/visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd
import io
from PIL import Image

image_list = []  # Global list to store plot images for the report

def save_plot_to_image(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image = Image.open(buf)
    image_list.append(image)

def plot_histograms(df, num_cols, st):
    for col in num_cols:
        st.write(f"📈 Histogram for: {col}")
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)
        save_plot_to_image(fig)

def plot_pie_charts(df, cat_cols, st):
    for col in cat_cols:
        st.write(f"📊 Pie Chart for: {col}")
        fig, ax = plt.subplots()
        df[col].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.axis('equal')
        st.pyplot(fig)
        save_plot_to_image(fig)

def plot_wordclouds(df, text_cols, st):
    for col in text_cols:
        st.write(f"☁️ WordCloud for: {col}")
        text = " ".join(df[col].dropna().astype(str))
        if text.strip():
            wc = WordCloud(width=800, height=400).generate(text)
            fig, ax = plt.subplots()
            ax.imshow(wc, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
            save_plot_to_image(fig)

def plot_correlation_heatmap(df, num_cols, st):
    if len(num_cols) >= 2:
        st.write("📉 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
        save_plot_to_image(fig)

def plot_boxplots(df, num_cols, cat_cols, st):
    for cat in cat_cols:
        for num in num_cols:
            st.write(f"📊 Boxplot: {num} by {cat}")
            fig, ax = plt.subplots()
            sns.boxplot(x=cat, y=num, data=df, ax=ax)
            st.pyplot(fig)
            save_plot_to_image(fig)

def get_saved_images():
    return image_list
