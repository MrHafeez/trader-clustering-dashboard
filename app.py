import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load the clustered data
features = pd.read_csv("clustered_trader_profiles.csv")

# Page configuration
st.set_page_config(page_title="Trader Clustering Dashboard", layout="wide")

# Page title
st.title("Trader Personality Clustering Dashboard")

# Sidebar Tips for Students
with st.sidebar:
    st.markdown("### 🔍 Explore the Data")
    st.markdown("- Which cluster has the **highest win rate**?")
    st.markdown("- Who trades more aggressively (**high quantity, low win rate**)?")
    st.markdown("- Patterns in **avg PnL vs pnl volatility**?")
    st.markdown("\n---\n")
    st.markdown("**Project Guide:** This dashboard uses KMeans + PCA to cluster traders based on behavioral metrics.")

# Section 1: Display Clustered Data
st.subheader("Full Clustered Data")
st.dataframe(features)

# Section 2: Cluster Summary
st.subheader("Cluster-wise Summary")
summary = features.groupby('cluster').mean(numeric_only=True).round(2)
st.dataframe(summary)

# Section 3: PCA Cluster Distribution with Plotly (interactive)
st.subheader("PCA Cluster Distribution")
fig_pca = px.scatter(
    features,
    x="pca1",
    y="pca2",
    color=features['cluster'].astype(str),
    hover_data=["user_id", "num_trades", "avg_pnl", "win_rate"],
    title="Interactive PCA Cluster Plot",
    height=500,
    color_continuous_scale=px.colors.sequential.Darkmint,
    template="plotly_dark"
)
st.plotly_chart(fig_pca, use_container_width=True)

# Section 4: Responsive Layout for Feature Boxplot
st.subheader("Feature Comparison by Cluster")
col1, col2 = st.columns([1, 2])

with col1:
    feature_options = [
        "avg_quantity", "avg_price", "avg_pnl", "pnl_volatility",
        "num_trades", "buy_sell_ratio", "win_rate"
    ]
    selected_feature = st.selectbox("Select a feature", feature_options)

with col2:
    fig_box, ax = plt.subplots()
    sns.boxplot(data=features, x="cluster", y=selected_feature, palette="dark", ax=ax)
    ax.set_title(f"{selected_feature} by Cluster", fontsize=12)
    st.pyplot(fig_box)

# Section 5: Download CSV
st.subheader("Download")
csv = features.to_csv(index=False).encode("utf-8")
st.download_button("Download Clustered CSV", csv, "clustered_trader_profiles.csv", "text/csv")
