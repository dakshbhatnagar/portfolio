# Import necessary libraries
import streamlit as st
import numpy as np
import yfinance as yf
import pandas as pd
import plotly.express as px
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
from datetime import date, timedelta
import plotly.graph_objects as go

# Hide default Streamlit format for cleaner appearance
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """


st.set_page_config(page_title='Stock Predictions', layout="wide", initial_sidebar_state="auto")

st.markdown(hide_default_format, unsafe_allow_html=True)

# Get user input for stock symbol
symbol = st.text_input('Enter a Symbol Here e.g GOOGL or AAPL', '')
data = yf.Ticker(symbol)

#Fetching the records for the lifetime of the stock
data_hist = data.history(period="max")

##Skipping the dividend column
df = data_hist[["Open", "High", "Low", "Close", "Volume"]]

# Function to predict and display stock metrics and predictions
def predict():
    
    if symbol:
        # Display real-time stock metrics
        col1, col2, col3, col4= st.columns(4)
        with col1:
            open_val = round(data.history(period='1d').Open.values[0],2)
            st.metric(label='Open', value=open_val)
        with col2:
            high_val = round(data.history(period='1d').High.values[0],2)
            st.metric(label='High',value=high_val)
        with col3:
            low_val = round(data.history(period='1d').Low.values[0],2)
            st.metric(label='Low',value=low_val)
        with col4:
            close_val = round(data.history(period='1d').Close.values[0],2)
            st.metric(label='Close',value=close_val)
        st.markdown(f"<h5 style='text-align: center; color: black; font-size: 20px;'>Predicting {symbol} Close prices</h1>", 
                    unsafe_allow_html=True)
        
        # Train ARIMA model 
        # taking all the records before 2022 to train the data
        train = df[df.index.year<2022]
        #creating a test set with the records including and after 2022
        test = df[df.index.year>=2022]
        st.write(f"Model trained on {len(train)} days worth of data")
        exogenous_features = ['Open', 'High', 'Low']
        train = train[train.columns[:4]]
        test = test[test.columns[:4]]
        model = sm.tsa.arima.ARIMA(endog=train['Close'], exog=train[exogenous_features], order=(1, 1, 1))
        model_fit = model.fit()

        # Generate forecast
        forecast = [model_fit.forecast(exog=test[exogenous_features].iloc[i]).values[0] for i in range(len(test))]
        test['Forecast'] = forecast
        test['Confidence'] =  np.around(1/(1+ np.exp(-test['Forecast']))*100,2)
        
        
        
        # Plot prediction chart
        arr = test[['Close','Forecast']][-30:]

        fig = px.line(arr,color_discrete_sequence=["#0474BA", "#F17720"])
        st.plotly_chart(fig, theme="streamlit",  title="Prediction Chart", use_container_width=True)
        
        # Plot scatter plot for actual vs predicted close prices
        fig = px.scatter(arr, x='Close', y='Forecast', color_discrete_sequence=["#0474BA", "#F17720"],
                        trendline="ols",  # Ordinary Least Squares regression line,
                        trendline_color_override="#F17720",
                        labels={'Close': 'Actual Close', 'Forecast': 'Predicted Close'},
                        title='Actual vs Predicted Close Prices, Test Set',
                        opacity=0.7,
                        size_max=15)  # Adjust the marker size

        st.plotly_chart(fig, theme="streamlit",  title="Actuals and Predictions Scattterplot", use_container_width=True)
        
        # Display metrics and information
        col1, col2 = st.columns(2)
        with col1:

            arr = test[['Close','Forecast', 'Confidence']][-30:]
            st.markdown("<h5 style='text-align: center; color: black; font-size: 20px;'>Actual Close and Predictions</h1>", 
                    unsafe_allow_html=True)
            st.dataframe(arr)
             
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
            # Display information about the stock
            about = data.get_info()['longBusinessSummary']
            
            st.write("About :\n\n", about)
    else:
       st.markdown("<h5 style='text-align: center; color: black; font-size: 30px;'>Welcome!</h5>", 
                    unsafe_allow_html=True)
       
       text = """
        Welcome to the app that utilizes the power of statistical modeling to forecast historical stock prices. The app (powered by Yahoo Finance API) is designed to assist individuals of all technical backgrounds in gaining valuable insights into the stock market.

        \n\nHarnessing the ARIMA (Autoregressive Integrated Moving Average) model, the app analyzes historical stock price data to identify patterns and trends. This analysis forms the basis for predicting future price movements, providing valuable guidance for informed investment decisions.

        \n\nEmbark on your investment journey with the app and unlock a world of informed financial decision-making.
                """
        
       st.markdown(f"<p style='text-align: center; color: black; font-size: 17px;'>{text}</p>", 
                    unsafe_allow_html=True)
       
# Function to explore stock data and display various information       
def explore():
    # Display collected data and candlestick chart
    st.markdown(f"<h5 style='text-align: left; color: black; font-size: 12px;'>Collected {data_hist.shape[0]} days worth of data</h1>", unsafe_allow_html=True)
    
    with st.expander("See Original Data"):
        if symbol:
            st.dataframe(df)
    
    if symbol:
        # Display candlestick chart
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

        # Display institutional holders, cash flow, balance sheet, and earning dates
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Institutional Holders</h5>", 
                        unsafe_allow_html=True)
            
            holders = data.institutional_holders.fillna(0)
            st.dataframe(holders)
            
            st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Cash Flow</h5>", 
                        unsafe_allow_html=True)
            st.dataframe(data.cashflow.fillna(0))


        with col2:
            st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Balance Sheet</h5>", unsafe_allow_html=True)
            st.dataframe(data.balancesheet.fillna(0))
            st.markdown("<h5 style='text-align: center; color: red; font-size: 20px;'>Earning Dates</h5>", unsafe_allow_html=True)
            st.dataframe(data.earnings_dates.fillna(0))
# Dictionary mapping page names to corresponding functions    
page_names_to_funcs = {
    "Predict": predict,
    "Explore": explore
}
# Streamlit sidebar
with st.sidebar:
    logo ='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Yahoo%21_Finance_logo_2021.png/1200px-Yahoo%21_Finance_logo_2021.png?20220131010522'
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')

    with col2:
        st.image(logo, width=100)

    with col3:
        st.write(' ')
    
    st.markdown("<h1 style='text-align: center; color: black; font-size: 25px;'>Stock Prediction App</h1>", 
                unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: black; font-size: 10px;'>The prediction model used is ARIMA, a statistical model used to predict future values by combining past data and patterns.</p>", 
                unsafe_allow_html=True)
    # Dropdown to select the page (Predict or Explore)
    demo_name = st.selectbox('Predict Or Explore', page_names_to_funcs.keys())
    
    st.markdown("Contact :")
    
    contact = st.write(
        """ 
    🤝 Check out my [Portfolio Website](https://dakshbhatnagar.github.io)

    🚀 Connect with me on [LinkedIn](https://www.linkedin.com/in/dakshb/) 
            
    ✉️ Shoot me an [email](bhatnagar91@gmail.com)!        
        """)
# Call the selected function based on the dropdown selection

page_names_to_funcs[demo_name]()
