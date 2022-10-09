import streamlit as st
import pandas as pd
import datetime
from datetime import datetime

st.markdown (''' **Crypto Tracking Price**
* A simple app to check the price, powered by Ricky *''')

st.header ("Trending Price")

#getting data from api 
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

col1, col2, col3 =st.columns(3)


#widget
col1_selection = st.sidebar.selectbox('Price1', df.symbol, list(df.symbol).index('BTCBUSD'))

#frame
col1_df = df[df.symbol] == col1_selection 

st.dataframe(df)

st.info()