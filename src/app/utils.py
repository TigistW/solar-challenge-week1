import pandas as pd

def load_data():
    # Placeholder paths - these CSVs should be ignored in Git
    benin = pd.read_csv('../../data/benin_clean.csv')
    sierra = pd.read_csv('../../data/sierra_leone_clean.csv')
    togo = pd.read_csv('../../data/togo_clean.csv')

    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    return pd.concat([benin, sierra, togo], ignore_index=True)

def get_top_regions(df, metric, n=5):
    return df.groupby('Region')[metric].mean().sort_values(ascending=False).head(n).reset_index()
