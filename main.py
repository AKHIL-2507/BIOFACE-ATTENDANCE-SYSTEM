

import streamlit as st

from streamlit_option_menu import option_menu


import main,Home,Adduser,addattendance,userlist
st.set_page_config(
        page_title="BIOFACE ATTENDANCE SYSTEM"
)

class MultiApp:



    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='MAIN MENU ',
                options=['HOME','ADD NEW USER','ADD ATTENDANCE','USERLIST'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "16px"}, 
        "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "HOME":
            Home.app()
        if app == "ADD NEW USER":
            Adduser.app()    
        if app == "ADD ATTENDANCE":
            addattendance.app()        
        if app == 'USERLIST':
           userlist.app()
        #if app == 'about':
         #   about.app()    
             
    run()         
         
