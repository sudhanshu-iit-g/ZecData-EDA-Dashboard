# utils/sentiment_analysis.py

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
from PIL import Image

sia = SentimentIntensityAnalyzer()

def analyze_text_columns(df, text_cols, st, image_list):
    st.subheader("☁️ Text Insights & Sentiment Analysis")

    if not text_cols:
        st.info("No text columns detected for sentiment analysis.")
        return

    for col in text_cols:
        st.markdown(f"**📌 Analyzing Text Column: `{col}`**")

        # WordCloud Generation
        text = " ".join(df[col].dropna().astype(str))
        if text.strip():
            wc = WordCloud(width=800, height=400).generate(text)
            fig, ax = plt.subplots()
            ax.imshow(wc, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)

            # Save for report
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            img = Image.open(buf)
            image_list.append(img)

        # Sentiment Analysis
        sentiments = df[col].astype(str).apply(lambda x: sia.polarity_scores(x)['compound'])
        st.write(f"**📈 Average Sentiment Score for `{col}`**: `{sentiments.mean():.2f}`")
