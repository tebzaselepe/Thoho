import streamlit as st
import streamlit_book as stb
import streamlit_authenticator as stauth
# from db_fxn import *

def login():
    
    names = ['Admin']
    usernames = ['admin']
    passwords = ['1234']
    
    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=1, preauthorized=None)
    name, authentication_status, username = authenticator.login('Login', 'main')
        
    if st.session_state["authentication_status"]:
        
        
        test=authenticator.logout('Logout', 'main')
        log_name = st.session_state["name"] + " Portal"
        st.title('Private content')
        stb.set_book_config(
                menu_title=log_name,
                menu_icon="public",
                options=[
                    "Dashboard",
                    "Clients",
                    "Employees",
                    ], 
                paths=[
                    "private/charts.py",
                    "private/client.py",
                    "private/employees.py"
                    ],
                save_answers=False,
                styles={
                    "nav-link": {"--hover-color": "#fde8ec"},
                    "nav-link-selected": {"background-color": "#DC143C"},
                    "nav-link": {"background": "0 0"}
    
                }
                )
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')
        
def main():
    login()

if __name__ == "__main__":
    main()