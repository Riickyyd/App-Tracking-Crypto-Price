import streamlit as st
import pandas as pd
import datetime
from datetime import datetime
import pytz
import numpy as np
from PIL import Image
from urllib.request import urlopen
import requests
import json

#theme
backgroundColor="white"
secondaryBackgroundColor="#F0F2F6"
font="sans serif"


imageBTC = Image.open(urlopen('https://www.lacampionessa.com/29336-large_default/202122-juventus-fc-away-sponsor-logo-ufficiale-bitget.jpg'))
new_image = imageBTC.resize((150, 150))
st.image(new_image)

st.markdown('# **Tracking Cryptocurrency Price**')
st.markdown('Powered by Ricky')

st.header('**Selected Price**')


# Load market data from Binance API
df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# Custom function for rounding values
def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 5))
    return a

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)


# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCUSDT'))
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHUSDT'))
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('NEARUSDT'))
col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('FTMUSDT'))
col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('BNBUSDT'))
col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('SANDUSDT'))




# DataFrame of selected Cryptocurrency
col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]
col3_df = df[df.symbol == col3_selection]
col4_df = df[df.symbol == col4_selection]
col5_df = df[df.symbol == col5_selection]
col6_df = df[df.symbol == col6_selection]



# Apply a custom function to conditionally round values
col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)
col3_price = round_value(col3_df.weightedAvgPrice)
col4_price = round_value(col4_df.weightedAvgPrice)
col5_price = round_value(col5_df.weightedAvgPrice)
col6_price = round_value(col6_df.weightedAvgPrice)


# Select the priceChangePercent column and round value
col1_percent = f'{float(round(col1_df.priceChangePercent,2))}%'
col2_percent = f'{float(round(col2_df.priceChangePercent,2))}%'
col3_percent = f'{float(round(col3_df.priceChangePercent,2))}%'
col4_percent = f'{float(round(col4_df.priceChangePercent,2))}%'
col5_percent = f'{float(round(col5_df.priceChangePercent,2))}%'
col6_percent = f'{float(round(col6_df.priceChangePercent,2))}%'




# Create a metrics price box
col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)
col3.metric(col3_selection, col3_price, col3_percent)
col4.metric(col4_selection, col4_price, col4_percent)
col5.metric(col5_selection, col5_price, col5_percent)
col6.metric(col6_selection, col6_price, col6_percent)

#update real time
t = datetime.now(pytz.timezone("EST")).strftime("%H:%M:%S")
st.write('Update at: ', t)

#talble
st.header ('All information')
st.dataframe(df)

st.balloons()

#Exchange to other currencies BTC
st.header ('BTC Exchange')
image2 = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(image2)

@st.experimental_memo
def info():
#     api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR,VND"
    api_link = "https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&e=Kraken"
    req = requests.get(api_link)
    dic = req.json()
    
    VND_value =  (dic["RAW"])
    st.table(VND_value)
#     VND_value =  (dic["VND"])
#     VND_formatted_value = "{:,.3f}".format(VND_value)
#     st.write('Price to VNĐ: ', VND_formatted_value + "đ")
    
#     euro_value =  (dic["EUR"])
#     euro_formatted_value = "{:,.3f}".format(euro_value)
#     st.write('Price to Euro: ', euro_formatted_value + "€")
    
 
info ()



#change
st.info("Referenced by Mr.Data Professor")
