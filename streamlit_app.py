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

symbol = st.text_input('Enter a Symbol Here e.g GOOGL or AAPL', '')
data = yf.Ticker(symbol)
data_hist = data.history(period="max")
df = data_hist[["Open", "High", "Low", "Close", "Volume"]]

def predict():
    if symbol:
        col1, col2, col3, col4= st.columns(4)
        with col1:
            st.metric(label='Open', value=data.info['open'])
        with col2:
            st.metric(label='High',value=data.info['dayHigh'])
        with col3:
            st.metric(label='Low',value=data.info['dayLow'])
        with col4:
            st.metric(label='Close',value=data.info['previousClose'])
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
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h5 style='text-align: center; color: black; font-size: 20px;'>Actual Price and Predictions</h1>", 
                    unsafe_allow_html=True)
            st.dataframe(arr)
        with col2:
            st.write("About :")
            st.write(data.info['longBusinessSummary'])
            st.write(f"Industry : {data.info['industry']}")
            st.write(f"CEO : {data.info['companyOfficers'][0]['name']}")
    else:
        st.markdown('You did not enter a symbol.')

def explore():
    
    st.markdown(f"<h5 style='text-align: center; color: black; font-size: 15px;'>The model was trained on {data_hist.shape[0]} days worth of data</h1>", unsafe_allow_html=True)
    with st.expander("See Original Data"):
        st.dataframe(df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Institutional Holders</h5>", 
                    unsafe_allow_html=True)
        st.dataframe(data.institutional_holders)
        
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Cash Flow</h5>", 
                    unsafe_allow_html=True)
        st.dataframe(data.cashflow)

    with col2:
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Balance Sheet</h5>", unsafe_allow_html=True)
        st.dataframe(data.balancesheet)
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Earning Dates</h5>", unsafe_allow_html=True)
        st.dataframe(data.earnings_dates)

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
