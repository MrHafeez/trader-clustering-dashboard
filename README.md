# Trader Personality Clustering Dashboard

This is a Streamlit-based web application that analyzes and visualizes clustered trader profiles using unsupervised learning. It applies KMeans clustering to behavioral trade features such as average PnL, volatility, quantity, and win rate. PCA is used for 2D visualization.

## Features

- Full view of all clustered trader profiles
- Cluster-wise summary statistics
- Interactive PCA-based scatter plot (using Plotly)
- Feature comparison using boxplots
- CSV download of clustered dataset

## Use Cases

- Identify different trading behaviors and personalities
- Spot high-performing or risk-prone trader segments
- Compare cluster-level trends in quantity, win rate, and volatility

## Local Setup

### Prerequisites

- Python 3.8 or later

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/trader-clustering-dashboard.git
cd trader-clustering-dashboard
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

## Project Files

- `app.py`: Main Streamlit application
- `clustered_trader_profiles.csv`: Pre-clustered data file used for visualization
- `requirements.txt`: Python dependencies for running the app
- `README.md`: Project overview and usage guide

## Deployment

To deploy this project on Streamlit Cloud:

1. Push this code to a public GitHub repository
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with GitHub and deploy the app by selecting the repository and setting the main file path to `app.py`

## License

This project is open-source and available for educational use.
