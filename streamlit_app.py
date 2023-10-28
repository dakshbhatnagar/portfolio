import streamlit as st
st.set_page_config(page_title='Daksh Bhatnagar | Data Analyst', layout="wide")
st.markdown("<h1 style='text-align: center; font-size: 28px; color: #FCF5ED;'>Daksh Bhatnagar</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 25px; color: #FCF5ED;'>Data Analyst</h2>", unsafe_allow_html=True)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

st.markdown(hide_default_format, unsafe_allow_html=True)

with st.sidebar:
    add_radio = st.markdown("<h1 style='text-align: center; color: #FCF5ED; font-size: 55px;'>Welcome</h1>", 
                unsafe_allow_html=True)
    sidebar_info = st.markdown("<h2 style='text-align: center; color: #FCF5ED; font-size: 16px;'>This app showcases my passion for data and tech through the collection of the work I've done. Hope you enjoy your stay!</h1>", 
                unsafe_allow_html=True)

def intro():
    st.markdown("Introduction")
    st.write("""
    📈 As a Data Analyst from Delhi, India, I enjoy unravelling the mysteries of data one byte at a time! 🕵️‍♂️

    ✅ With the help of Google Sheets & Looker, I can help you look deeper into your business & make informed decisions. Feel free to check out my [Tableau](https://public.tableau.com/app/profile/daksh.bhatnagar#!/) profile.

    🔥 I'm always on the quest for business problems that can be solved with the help of data and automation.

    💡 They say I'm a Kaggle Notebooks Master but don't trust them. See for yourself [here](https://www.kaggle.com/bhatnagardaksh/code).

    🤖 I'm also developing CNNs for [Zone Classification](https://www.kaggle.com/code/bhatnagardaksh/zone-classification-transfer-learning) for my freelancing project. 
    """)

def python_proj():
    st.write(
        """
        ##### 📁 Python Projects

        Here is a glimpse of projects that I've done using Python:

        1. **Customer Churn Prediction** 📊
            - Dive into the world of customer behavior analysis! Using ANN, we find out if the credit card customer is going to be churned or not. Click [here](https://github.com/dakshbhatnagar/python_files/blob/main/JupyterNotebooks/customer-churn-prediction-anns%20(1).ipynb) 

        2. **Stock Price Predictions** 📈
            - Stock Price predictions are always fun to make. Using Backtesting, a Stastical Model and a Deep Learning Network, we do exactly that. Check out the project [here](https://www.kaggle.com/code/bhatnagardaksh/stock-predictions-with-backtesting-arima-and-gru)

        3. **Sentiment Analysis** 📝
            - Understanding Sentiment of others can be tough. Let's make it a breeze. Click [here](https://www.kaggle.com/code/bhatnagardaksh/youtube-comments-analysis-updated) to find out how

        **And Many More!** 🚀 

        Check out the relevant Github Repository [here](https://github.com/dakshbhatnagar/python_files)
        
        """
    )
def JS_page():
    st.write("""
    ##### 📁 JavaScript Mini Projects

1. **Random Number Guesser** 🎲
    Are you a psychic when it comes to guessing numbers? Test your intuition with this fun & interactive Number Guesser game [here](https://github.com/dakshbhatnagar/JS_files/blob/main/index.js) 🤞

2. **Job Scraper** 📝
   The Job Scraper built using fetch API and regex concepts pulls the data from job portal & store it in a CSV. Take a peek [here](https://github.com/dakshbhatnagar/JS_files/blob/main/scraper.js) 💼🔍

3. **Snake, Water, and Gun Game** 🐍🌊🔫
   Challenge the computer to a [game](https://github.com/dakshbhatnagar/JS_files/blob/main/snake_water_gun.js) of Snake, Water, and Gun! Here's how it works:

   a. Snake beats Gun: Snakes are sneaky! They'll take down guns any day.
   
   b. Gun beats Water: Guns can shoot down even the most formidable waves.
   
   c. Water beats Snake: Water will drown the slithering snakes with ease.

    """)

def contact_me():
    st.markdown("Contact :")
    
    st.write(
        """ 

    🚀 If you want to connect or just say Hi, connect with me on [LinkedIn](https://www.linkedin.com/in/dakshb/) 
            
    ✉️ Got questions, or suggestions? I'm all ears! Let me hear it at bhatnagar91@gmail.com !        
        """)

page_names_to_funcs = {
    "Introduction": intro,
    "Python": python_proj,
    "JavaScript": JS_page,
    "Contact" : contact_me
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
