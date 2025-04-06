# utils/missing_handler.py

import pandas as pd

def handle_missing(df, data_types):
    for col, dtype in data_types.items():
        if dtype == 'numerical':
            df[col] = df[col].fillna(df[col].mean())
        elif dtype == 'categorical':
            mode_val = df[col].mode().iloc[0] if not df[col].mode().empty else "Unknown"
            df[col] = df[col].fillna(mode_val)
        elif dtype == 'text':
            df[col] = df[col].fillna("")
        elif dtype == 'datetime':
            df[col] = pd.to_datetime(df[col], errors='coerce')
    return df
