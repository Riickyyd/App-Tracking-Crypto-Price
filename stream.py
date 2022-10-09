import streamlit as st
import pandas as pd

st.markdown('''# **Tracking Cryptocurrency Price**
Powered by Ricky ''')

st.header('**Selected Price**')

# Load market data from Binance API
df = pd.read_json('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a

col1, col2, col3 = st.columns(3)

# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('USD') )


# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_selection]


# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.weightedAvgPrice)


# Select the priceChangePercent column
col1_percent = f'{float(col1_df.priceChangePercent)}%'


# Create a metrics price box
col1.metric(col1_selection, col1_price, col1_percent)


st.header('**All Price**')
st.dataframe(df)

st.info("Referenced by Mr.Data Professor")
