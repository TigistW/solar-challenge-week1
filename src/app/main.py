import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_top_regions

st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

st.title("🌞 Cross-Country Solar Dashboard")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
country_options = st.sidebar.multiselect("Select Countries", options=df['Country'].unique(), default=df['Country'].unique())
metric = st.sidebar.selectbox("Select Metric", ['GHI', 'DNI', 'DHI'])

# Filtered data
filtered_df = df[df['Country'].isin(country_options)]

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(4,2))
sns.boxplot(data=filtered_df, x='Country', y=metric, ax=ax, palette='Set2')
st.pyplot(fig)

# Top Regions Table
st.subheader(f"📈 Top 3 Regions by Average {metric}")
if 'Country' in df.columns:
    top_regions = get_top_regions(filtered_df, metric)
    st.dataframe(top_regions)
else:
    st.info("Region column not found in dataset.")
