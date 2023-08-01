import streamlit as st
st.set_page_config(layout="wide")
st.balloons()
st.markdown("<h1 style='text-align: center; color: black;'>Daksh Bhatnagar</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: light grey;'>Data Analyst</h2>", unsafe_allow_html=True)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

with st.sidebar:
    add_radio = st.markdown("<h1 style='text-align: center; color: black; font-size: 55px;'>Welcome</h1>", 
                unsafe_allow_html=True)
    st.sidebar.info("This platform showcases my passion for data and tech, through the collection of the work I've done. Enjoy your stay!")

def intro():
    st.write("""
    📈 As a Data Analyst from Delhi, India, I enjoy unravelling the mysteries of data one byte at a time! 🕵️‍♂️

    ✅ With the help of Google Sheets and Looker, I can help you look deeper into your business and make informed decisions. Feel free to check out my [Tableau](https://public.tableau.com/app/profile/daksh.bhatnagar#!/) profile.

    🔥 I am always on the quest for business problems that can be solved with the help of data and some automation. Problem Solving is fun!.

    💡 They say I'm a Kaggle Notebooks Expert but don't trust them. See for yourself on this : [link](https://www.kaggle.com/bhatnagardaksh/code)

    🤖 I am also developing CNNs for [Zone Classification](https://www.kaggle.com/code/bhatnagardaksh/zone-classification-transfer-learning) for my unpaid side gig.

    🍻 If you have got a data problem then I am more than willing to help 🎉 Whether it's discovering hidden patterns or making sense of the data chaos, I'm your data ally! 

""")

def python_proj():
    
    st.write(
        """
        ## 📁 Python Projects

        Here is a glimpse of projects that I have done using Python:

        1. **Customer Churn Prediction** 📊
            - Dive into the world of customer behavior analysis! Unravel the secrets of churn prediction and explore strategies to retain valuable customers.

        2. **Stock Price Predictions** 📈
            - Embark on a financial adventure! Forecast stock prices and witness the magic of predictive analytics in the unpredictable world of finance.

        3. **Sentiment Analysis** 📝
            - Delve into the art of sentiment analysis! Unleash the power of Natural Language Processing (NLP) to understand and analyze the sentiments hidden within text.

        4. **And Many More!** 🚀 
        
        """
    )
def JS_page():
    st.write("""
    ## 📁 JavaScript Mini Projects

1. **Random Number Guesser** 🎲
    Are you a psychic when it comes to guessing numbers? Test your intuition with this fun and interactive Number Guesser game [here](https://github.com/dakshbhatnagar/JS_files/blob/main/index.js) 🤞

2. **Job Scraper** 📝
   The Job Scraper built using fetch API and regex concepts pulls the data from job portal and store it in a CSV. Take a look [here](https://github.com/dakshbhatnagar/JS_files/blob/main/scraper.js) 💼🔍

3. **Snake, Water, and Gun Game** 🐍🌊🔫
   Challenge the computer to a game of Snake, Water, and Gun! Can you outsmart the computer in this age-old battle of wits? Here's how it works:

   a. 🐍 Snake beats 🔫 Gun: Snakes are sneaky! They'll take down guns any day.
   
   b. 🔫 Gun beats 🌊 Water: Guns can shoot down even the most formidable waves.
   
   c. 🌊 Water beats 🐍 Snake: Water will drown the slithering snakes with ease.

Choose your move wisely, and let the dance-off and game showdown begin! 💃🎲""")

def contact_me():
    
    st.write(
        """ 

    🚀 If you want to connect or just say Hi, connect with me on [LinkedIn](https://www.linkedin.com/in/dakshb/) 
            
    Got questions, or suggestions? I'm all ears! Feel free to reach out to me at bhatnagar91@gmail.com, and I promise to respond faster than ChatGPT! ⚡️!        
        """)

page_names_to_funcs = {
    "Introduction": intro,
    "Python": python_proj,
    "JavaScript": JS_page,
    "Contact" : contact_me
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
