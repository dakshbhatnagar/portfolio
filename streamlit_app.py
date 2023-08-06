import numpy as np
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 14
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (22,5)
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

st.set_page_config(page_title='Stock Predictions', layout="wide", initial_sidebar_state="auto")
st.markdown(hide_default_format, unsafe_allow_html=True)

symbol = st.text_input('Enter a Symbol Here', '')
data = yf.Ticker(symbol)
data_hist = data.history(period="max")
df = data_hist[["Open", "High", "Low", "Close", "Volume"]]

def predict():
    if symbol:
        st.markdown(f"<h5 style='text-align: center; color: black; font-size: 20px;'>Predicting {symbol} Close prices</h1>", 
                    unsafe_allow_html=True)
        train = df[df.index.year<2020]
        test = df[df.index.year>=2020]
        exogenous_features = ['Open', 'High', 'Low']
        train = train[train.columns[:4]]
        test = test[test.columns[:4]]
        model = sm.tsa.arima.ARIMA(endog=train['Close'], exog=train[exogenous_features], order=(1, 1, 1))
        model_fit = model.fit()
        
        forecast = [model_fit.forecast(exog=test[exogenous_features].iloc[i]).values[0] for i in range(len(test))]
        test['Forecast'] = forecast
        arr = test[['Close','Forecast']][-50:]
        fig, ax = plt.subplots()
        ax.set_ylabel('Price')
        ax.set_xlabel('Time')
        
        ax.legend(['Actual Price', 'Predicted Price'])
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False);
        ax.plot(arr)
        st.pyplot(fig)
        st.markdown("<h5 style='text-align: center; color: black; font-size: 20px;'>Actual Price and Predictions</h1>", 
                    unsafe_allow_html=True)
        st.dataframe(arr)
    else:
        st.markdown('You did not enter a symbol.')

def explore():
    
    st.markdown(f"<h5 style='text-align: center; color: black; font-size: 15px;'>The model was trained on {data_hist.shape[0]} days worth of data</h1>", unsafe_allow_html=True)
    with st.expander("See Original Data"):
        st.dataframe(df)

    st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Finding the values of p and q</h1>", 
                    unsafe_allow_html=True)
    # plot the ACF plot
    fig = plot_acf(df.High, lags=5, title=f'Auto Correlation Function plot, {symbol}')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    st.pyplot(fig)

    fig = plot_pacf(df.High, lags=5, title=f'Auto Partial Correlation Function plot, {symbol}')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    st.pyplot(fig)

    with st.expander("See Explanation"):
        st.write("You should stop looking further for p and q values when the ACF and PACF plots show a sharp cut-off or when the correlation values of the lags drop below a certain threshold.")
        st.write("This usually indicates that the pattern of the data has been captured and adding additional lags would not provide any additional information.")
    
    st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>For Integrated Order</h1>", 
                    unsafe_allow_html=True)

    fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(15, 10))
    ax1.plot(df.High); ax1.set_title('Original Series'); ax1.axes.xaxis.set_visible(False)
    ax1.spines['top'].set_visible(False)

    # 1st Differencing
    ax2.plot(df.High.diff()); ax2.set_title('1st Order Differencing'); ax2.axes.xaxis.set_visible(False)
    ax2.spines['top'].set_visible(False)

    # 2nd Differencing
    ax3.plot(df.High.diff().diff()); ax3.set_title('2nd Order Differencing')
    ax3.spines['top'].set_visible(False)

    plt.xlabel('Lags')
    plt.tight_layout()
    st.pyplot(fig)

    with st.expander("See Explanation"):
        st.write("Integrated order (I) is a parameter in an ARIMA model that refers to the number of times the data have been differenced in order to make it stationary.")
        st.write("A value of 0 indicates that the data has not been differenced, while a value of 1 indicates that the data has been differenced once. Higher values indicate that the data has been differenced multiple times.")

page_names_to_funcs = {
    "Predict": predict,
    "Explore": explore
}

with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: black; font-size: 30px;'>Stock Predictions using ARIMA</h1>", 
                unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: black; font-size: 15px;'>The ARIMA model which we are using here is used as a forecasting tool to predict how something will act in the future based on past performance</h6>", 
                unsafe_allow_html=True)
    demo_name = st.selectbox('Predict Or Explore', page_names_to_funcs.keys())
    
    st.markdown("Contact :")
    
    contact = st.write(
        """ 

    🚀 Connect with me on [LinkedIn](https://www.linkedin.com/in/dakshb/) 
            
    ✉️ Shoot me an email at bhatnagar91@gmail.com !        
        """)

page_names_to_funcs[demo_name]()
