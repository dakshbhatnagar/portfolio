import streamlit as st

# Page configuration
st.set_page_config(
    page_title='Daksh Bhatnagar | Data Analyst',
    layout="wide",
    initial_sidebar_state='expanded'
)

# Hide default Streamlit formatting
hide_default_format = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Main header
st.markdown(
    """
    <h1 style='text-align: center; font-size: 28px; color: #ffffff;'>Daksh Bhatnagar</h1>
    <h2 style='text-align: center; font-size: 25px; color: #ffffff;'>Data Analyst</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <h1 style='text-align: center; color: #FCF5ED; font-size: 36px;'>Welcome</h1>
        <h2 style='text-align: center; color: #FCF5ED; font-size: 16px;'>This app showcases my passion for data and tech through my work collection. Hope you enjoy your stay!</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# Functions for different pages
def intro():
    st.markdown(
        """
        ## Introduction
        **📈 As a Data Analyst from New Delhi, India, I enjoy unraveling the mysteries of data one byte at a time!**

        ✅ Using [Google Sheets](https://docs.google.com/spreadsheets/d/14h0UCZOhi1nQx7oT7DY8SYmqp3S0Y5UssEjkGAuVgXo/edit#gid=312503756) & Looker, I can help you make informed business decisions. Check out my [Tableau](https://public.tableau.com/app/profile/daksh.bhatnagar#!/) profile.

        🔥 I'm always on the quest for business problems that can be solved with data and automation.

        💡 I'm a Kaggle Notebooks Master. See for yourself [here](https://www.kaggle.com/bhatnagardaksh/code).

        🤖 Currently developing CNNs for [Zone Classification](https://www.kaggle.com/code/bhatnagardaksh/zone-classification-transfer-learning) and open to freelance projects.
        """,
        unsafe_allow_html=True
    )

def google_sheets():
    st.markdown(
        """
        ### 📊 Google Sheets Experience
        - Leveraged Google Sheets and AppScript for cost reduction and automation in business processes.

        - Developed a Google Sheets pipeline by bringing in data from different worksheets for instant insights, boosting data-driven decisions by 20%.

        - Automated daily reports with Google AppScript, ensuring regular updates to the management and reducing manual work which led to 15% increase in efficiency.

        - Automated monthly incentive calculations (recruiters and TL) and distributions with Google Sheets, AppScript, reducing manual work by 15%.
        
        - [Project Example](https://docs.google.com/spreadsheets/d/14h0UCZOhi1nQx7oT7DY8SYmqp3S0Y5UssEjkGAuVgXo/edit#gid=312503756)
        """
    )

def python_proj():
    st.markdown(
        """
        ### 📁 Python Projects

        **1. Customer Churn Prediction** 📊 - Analyze customer behavior with ANN. [Explore here](https://github.com/dakshbhatnagar/python_files/blob/main/JupyterNotebooks/customer-churn-prediction-anns%20(1).ipynb).

        **2. Stock Price Predictions** 📈 - Predict stock prices using Backtesting, ARIMA, and GRU. [Check it out](https://www.kaggle.com/code/bhatnagardaksh/stock-predictions-with-backtesting-arima-and-gru).

        **3. Sentiment Analysis** 📝 - Simplify sentiment analysis. [Learn more](https://www.kaggle.com/code/bhatnagardaksh/youtube-comments-analysis-updated).

        **And Many More!** 🚀

        View more on [GitHub](https://github.com/dakshbhatnagar/python_files).
        """,
        unsafe_allow_html=True
    )

def sql_projects():
    st.markdown(
        """
        ###  SQL Projects
        🧬 Using SQL I analysed HR Data where in I looked at questions like:-

        - How many people are in each job
        - Which job pays more
        - Here is the [Project Link](https://github.com/dakshbhatnagar/SQLProjects/tree/main/HRData)

        - Advanced SQL queries for data extraction and analysis.

        - 🙋‍♂️ [SQL GitHub Repository](https://github.com/dakshbhatnagar/SQLProjects)
        """
    )

def visualization():
    st.markdown(
        """
        ### 📈 BI Tool Projects

        - 🧾 Trend of Digital Payments in India - [Link](https://public.tableau.com/app/profile/daksh.bhatnagar/viz/IndianDigitalPayments/Dashboard1)
        
        - 💉  COVID -19 Dashboard - [Link](https://public.tableau.com/app/profile/daksh.bhatnagar/viz/COVID-19Dashboard_16433078005920/Dashboard)
        
        - 🙋‍♂️ Check out the whole [Tableau Profile](https://public.tableau.com/app/profile/daksh.bhatnagar#!/)
        """
    )

def contact_me():
    st.markdown(
        """
        ## Contact
        🚀 Connect with me on [LinkedIn](https://www.linkedin.com/in/dakshb/).

        ✉️ Questions or suggestions? Email me at bhatnagar91@gmail.com!
        """,
        unsafe_allow_html=True
    )

# Page navigation
page_names_to_funcs = {
    "Introduction": intro,
    "Google Sheets": google_sheets,
    "Python": python_proj,
    "SQL": sql_projects,
    "Visualization": visualization,
    "Contact": contact_me
}

demo_name = st.sidebar.selectbox("Choose a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()