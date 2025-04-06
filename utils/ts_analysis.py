# utils/ts_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
import io
from PIL import Image

def analyze_time_series(df, date_cols, st, image_list):
    st.subheader("📅 Time Series Trends")

    if not date_cols:
        st.info("No datetime columns detected for time series analysis.")
        return

    for col in date_cols:
        try:
            df['_dt'] = pd.to_datetime(df[col], errors='coerce')
            ts = df.set_index('_dt').resample('D').size()

            st.line_chart(ts)

            # Decompose seasonal components
            if len(ts.dropna()) > 20:
                result = seasonal_decompose(ts, model='additive', period=7)
                fig = result.plot()
                st.pyplot(fig)

                # Save image for report
                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                buf.seek(0)
                img = Image.open(buf)
                image_list.append(img)
        except Exception as e:
            st.warning(f"❌ Time series analysis failed for {col}: {str(e)}")
