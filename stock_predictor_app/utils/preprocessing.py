import pandas as pd

def load_and_process(uploaded_file):
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    df = df[['Date', 'Close']].dropna()
    df.set_index('Date', inplace=True)
    return df