# data_loader.py
import pandas as pd

# Global DataFrame
df = None

def load_data(file_path):
    global df
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()  # Normalize column names
    
    # Convert date column to datetime (important for regression)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df.dropna(subset=['date'], inplace=True)
    
    print("Data loaded and cleaned successfully.\n")
    return df
