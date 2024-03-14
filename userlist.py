import streamlit as st
import pandas as pd
from datetime import datetime
datetoday2= datetime.today().strftime("%d-%m-%Y")
def app():
    #st.write('hello')
    if st.button('USER DETAILS'):
        df=pd.read_csv(f'Attendanc/Attendanc-{datetoday2}.csv')
        st.dataframe(df)
