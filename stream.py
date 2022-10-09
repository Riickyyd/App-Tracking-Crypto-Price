import streamlit as st
import pandas as pd
import datetime
from datetime import datetime


st.markdown('''# **Tracking Cryptocurrency Price**
Powered by Ricky ''')

st.header('**Selected Price**')

# Load market data from Binance API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

#update by time
def info():
    time = datetime.now().strftime("%H:%M:%S")

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 5))
    return a

col1, col2, col3, col4 = st.columns(4)

frame_head.after(100, info)

# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCUSDT'))
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHUSDT'))
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('NEARUSDT'))
col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('SOLUSDT'))


# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]



# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)



# Select the priceChangePercent column
col1_percent = f'{float(col1_df.priceChangePercent)}%'
col2_percent = f'{float(col2_df.priceChangePercent)}%'



# Create a metrics price box
col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)



st.header('**All Price**')
st.dataframe(df)

st.info("Referenced by Mr.Data Professor")


st.header('**Update at**')
