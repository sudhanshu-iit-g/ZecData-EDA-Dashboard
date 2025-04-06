# 📊 ZecData EDA Dashboard

Welcome to **ZecData EDA Dashboard** – an advanced, one-stop analytics and automated exploratory data analysis (Auto EDA) tool built with **Streamlit**. This dashboard streamlines data loading, cleaning, profiling, visualization, statistical analysis, time series analysis, sentiment analysis, and report generation — all in a sleek interface.

---

## 🚀 Features

- 📁 Upload CSV/Excel data
- 🔍 Auto type detection (numerical, categorical, datetime, text)
- 🧼 Missing value analysis and handling
- 📊 Visualizations:
  - Histograms, Pie Charts, Correlation Heatmaps
  - Boxplots, WordClouds
  - PCA scatter plots
- 📈 Statistical Tests:
  - ANOVA (Categorical vs Numeric)
  - Chi-Square (Categorical vs Categorical)
  - Pearson Correlation (Numeric vs Numeric)
- ⚠️ Outlier Detection using Z-Score
- 🧬 PCA Visualization for dimensionality reduction
- 📆 Time Series Decomposition (trend, seasonal, residual)
- 😊 Sentiment analysis using VADER (NLTK)
- 📄 Generate downloadable PDF report with embedded plots and summary

---

## 🛠️ Project Structure
ZecData-EDA-Dashboard/ ├── app.py ├── requirements.txt └── utils/ ├── loader.py ├── type_detection.py ├── missing_handler.py ├── visualizer.py ├── stats_analysis.py ├── ts_analysis.py ├── sentiment_analysis.py ├── report_generator.py └── outlier_pca.py


---

## 🧪 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudhanshu-iit-g/ZecData-EDA-Dashboard.git
   cd ZecData-EDA-Dashboard

2. python -m venv venv
   # Activate on Windows
  venv\Scripts\activate
  # Activate on Mac/Linux
  source venv/bin/activate

3. pip install -r requirements.txt
4. streamlit run app.py

📥 Exporting Reports
After performing your analysis, go to the sidebar and click 📄 Generate PDF Report to download a complete summary with:

Dataset dimensions

Data type overview

Plots and visualizations

👨‍💻 Author
Sudhanshu Raj
ZecData Intern | BTech Chemical Engineering | IIT Guwahati
GitHub: @sudhanshu-iit-g





