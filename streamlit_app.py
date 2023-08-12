import streamlit as st
import numpy as np
import yfinance as yf
import pandas as pd
import plotly.express as px
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
from datetime import date, timedelta
import plotly.graph_objects as go
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

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

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
        train = df[df.index.year<2021]
        test = df[df.index.year>=2021]
        st.write(f"Model trained on {len(train)} days worth of data")
        exogenous_features = ['Open', 'High', 'Low']
        train = train[train.columns[:4]]
        test = test[test.columns[:4]]
        model = sm.tsa.arima.ARIMA(endog=train['Close'], exog=train[exogenous_features], order=(1, 1, 1))
        model_fit = model.fit()
        
        forecast = [model_fit.forecast(exog=test[exogenous_features].iloc[i]).values[0] for i in range(len(test))]
        test['Forecast'] = forecast
        arr = test[['Close','Forecast']][-30:]
        fig = px.line(arr,color_discrete_sequence=["#0474BA", "#F17720"])
        st.plotly_chart(fig, theme="streamlit",  title="Prediction Chart", use_container_width=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h5 style='text-align: center; color: black; font-size: 20px;'>Actual Price and Predictions</h1>", 
                    unsafe_allow_html=True)
            st.dataframe(arr)
            csv = convert_df(arr)
            st.download_button(label="Download data as CSV",data=csv,file_name='predictions.csv',mime='text/csv')
             
            MSE = np.square(np.subtract(test.Close,test.Forecast)).mean()
            rmse = round(np.sqrt(MSE),2)
            Col1, Col2, Col3 = st.columns(3)

            with Col1:
                st.write(' ')

            with Col2:
                st.metric(label='RMSE', value=rmse)

            with Col3:
                st.write(' ')
            
            st.info("*RMSE (Root Mean Square Error) is a measure used to find how accurate a prediction model is by calculating the average difference between predicted and actual values in a dataset.")

        with col2:
            st.write("About :")
            st.write(data.info['longBusinessSummary'])
            st.write(f"Industry : {data.info['industry']}")
            st.write(f"CEO : {data.info['companyOfficers'][0]['name']}")
    else:
        st.markdown("<h5 style='text-align: center; color: black; font-size: 20px;'>Please enter a symbol above!</h5>", 
                    unsafe_allow_html=True)
    

def explore():
    
    st.markdown(f"<h5 style='text-align: left; color: black; font-size: 12px;'>Collected {data_hist.shape[0]} days worth of data</h1>", unsafe_allow_html=True)
    
    with st.expander("See Original Data"):
        st.dataframe(df)
        csv = convert_df(df)
        st.download_button(label="Download data as CSV",data=csv,file_name='Raw Data.csv',mime='csv')
    
    df.index = df.index.date
    days_to_subtract = 365
    end = date.today()
    start = end - timedelta(days=days_to_subtract)

    new_df = df[start:end]
    trace = go.Candlestick(x=new_df.index,
                        open=new_df['Open'],
                        high=new_df['High'],
                        low=new_df['Low'],
                        close=new_df['Close'])

    layout = go.Layout(title=f'{symbol} Candlestick Chart, 365 Days', title_x=0.4, width=800, height=500)
    fig = go.Figure(data=[trace], layout=layout)
    st.plotly_chart(fig)


    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Institutional Holders</h5>", 
                    unsafe_allow_html=True)
        st.dataframe(data.institutional_holders)
        csv = convert_df(data.institutional_holders)
        st.download_button(label="Download data as CSV",data=csv,file_name='institutional_holders.csv',mime='text/csv')
        
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Cash Flow</h5>", 
                    unsafe_allow_html=True)
        st.dataframe(data.cashflow)
        csv = convert_df(data.cashflow)
        st.download_button(label="Download data as CSV",data=csv,file_name='cashflow.csv',mime='text/csv')

    with col2:
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Balance Sheet</h5>", unsafe_allow_html=True)
        st.dataframe(data.balancesheet)
        csv = convert_df(data.balancesheet)
        st.download_button(label="Download data as CSV",data=csv,file_name='balancesheet.csv',mime='text/csv')
        st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Earning Dates</h5>", unsafe_allow_html=True)
        st.dataframe(data.earnings_dates)
        csv = convert_df(data.earnings_dates)
        st.download_button(label="Download data as CSV",data=csv,file_name='earnings_dates.csv',mime='text/csv')
    
    
page_names_to_funcs = {
    "Predict": predict,
    "Explore": explore
}

with st.sidebar:
    logo ='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Yahoo%21_Finance_logo_2021.png/1200px-Yahoo%21_Finance_logo_2021.png?20220131010522'
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        st.image(logo, width=100)

    with col3:
        st.write(' ')
    
    st.markdown("<h1 style='text-align: center; color: black; font-size: 25px;'>Stock Predictions using yfinance</h1>", 
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black; font-size: 10px;'>The prediction model used is ARIMA, a statistical model used to predict future values by combining past data and patterns.</p>", 
                unsafe_allow_html=True)
    demo_name = st.selectbox('Predict Or Explore', page_names_to_funcs.keys())
    
    st.markdown("Contact :")
    
    contact = st.write(
        """ 

    🚀 Connect with me on [LinkedIn](https://www.linkedin.com/in/dakshb/) 
            
    ✉️ Shoot me an email at bhatnagar91@gmail.com !        
        """)

page_names_to_funcs[demo_name]()
