import streamlit as st

st.set_page_config(page_title="Option Pricing App", page_icon="📈")

home = st.Page("pages/1_Home.py", title="Home")
black_scholes = st.Page("pages/2_Black_Scholes_Model.py", title="Black-Scholes Model")
binomial = st.Page("pages/3_Binomial_Model.py", title="Binomial Model")
visualizations = st.Page("pages/4_Visualizations.py", title="Visualizations")
about = st.Page("pages/5_About_Me.py", title="About Me")

pg = st.navigation(
    [home, black_scholes, binomial, visualizations, about],
    position="sidebar"
)

pg.run()
