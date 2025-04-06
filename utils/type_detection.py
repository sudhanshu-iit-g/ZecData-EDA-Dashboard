# utils/type_detection.py

import pandas as pd

def detect_data_types(df):
    types = {}
    for col in df.columns:
        try:
            if pd.api.types.is_numeric_dtype(df[col]):
                types[col] = 'numerical'
            elif pd.to_datetime(df[col], errors='coerce').notna().sum() > 0:
                types[col] = 'datetime'
            elif df[col].nunique() < 30:
                types[col] = 'categorical'
            else:
                types[col] = 'text'
        except:
            types[col] = 'text'
    return types
