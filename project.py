# AI powered technical analysis dashboard

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

st.title("📶 AI Powered Technical Analysis Dashboard")
st.title("🪟Chart Dataframe")

# List of csv files
csv_files = {"AAPL":"stock1.csv","MSFT":"stock2.csv","TSLA":"stock3.csv"}

# Let user select one
selected_stock  = st.sidebar.selectbox("SELECT THE STOCK",list(csv_files.keys()))

# Now load csv files
df = pd.read_csv(csv_files[selected_stock])
st.success(f"file loaded for {selected_stock}")




#
st.dataframe(df.iloc[:, :])

# Converting date in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Dashboard
st.title("Stock's Chart")

col1, col2, col3, col4, col5, col6= st.columns(6)



# Plot 1

if col1.button("Price",icon="💸",use_container_width=True):
    st.write("Price of the stock")
    fig1 , ax1 = plt.subplots(figsize=(8,4))
    ax1.plot(df['Date'], df['Price'],label='Price', color='blue')
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Price")
    plt.legend()
    st.pyplot(fig1)
    st.button("close")


# Plot2
if col2.button("Open",icon="🟢",use_container_width=True):
    st.write("Opening Price Of Stocks")
    fig2 , ax2 = plt.subplots(figsize=(8,4))
    ax2.plot(df['Date'], df['Open'],label='Open', color='red')
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Open")
    plt.legend()
    st.pyplot(fig2)
    st.button("Close")

# Plot 3
if col3.button("High",icon="💹",use_container_width=True):
    st.write("Highest Price Of The Stock")
    fig3 , ax3 = plt.subplots(figsize=(8,4))
    ax3.plot(df['Date'], df['High'],label='High', color='brown')
    ax3.set_xlabel("Date")
    ax3.set_ylabel("High")
    plt.legend()
    st.pyplot(fig3)
    st.button("Close")

# Plot4
if col4.button("Low",icon="📉",use_container_width=True):
    st.write("Lowest Price Of The Stock")
    fig4 , ax4 = plt.subplots(figsize=(8,4))
    ax4.plot(df['Date'], df['Low'],label='Low', color='orange')
    ax4.set_xlabel("Date")
    ax4.set_ylabel("Low")
    plt.legend()
    st.pyplot(fig4)
    st.button("Close")

# Plot 5
if col5.button("📊Volume",use_container_width=True):
    st.write("Volume Of The Stock")
    fig5 , ax5 = plt.subplots(figsize=(8,4))
    ax5.plot(df['Date'], df['Vol.'],label='volume', color='green')
    ax5.set_xlabel("Date")
    ax5.set_ylabel("Vol.")
    plt.legend()
    st.pyplot(fig5)
    st.button("Close")

#Plot 6
if col6.button("↕️Change%",use_container_width=True):
    st.write("Percentage Change Price Of The Stock")
    fig6 , ax6 = plt.subplots(figsize=(8,4))
    ax6.plot(df['Date'], df['Change%'],label='Change %', color='red')
    ax6.set_xlabel("Date")
    ax6.set_ylabel("percentage change")
    plt.legend()
    st.pyplot(fig6)
    st.button("Close")

                 
