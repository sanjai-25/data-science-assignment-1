import pandas as pd

def analyze_csv(file):
    df = pd.read_csv(file)
    
    print("\n===== DATA PREVIEW =====")
    print(df.head())
    
    print("\n===== BASIC INFO =====")
    df.info()
    
    print("\n===== STATISTICAL SUMMARY =====")
    print(df.describe())
    
    print("\n===== MEAN =====")
    print(df.mean(numeric_only=True))
    
    print("\n===== MEDIAN =====")
    print(df.median(numeric_only=True))
    
    print("\n===== MODE =====")
    print(df.mode(numeric_only=True).iloc[0])
    
    print("\n===== VARIANCE =====")
    print(df.var(numeric_only=True))
    
    print("\n===== STANDARD DEVIATION =====")
    print(df.std(numeric_only=True))

if _name_ == "_main_":
    file = input("Enter CSV file path: ")
    analyze_csv(file)
