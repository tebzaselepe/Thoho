import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_login_auth_ui.widgets import __login__
import streamlit_book as stb


__login__obj = __login__(auth_token = "pk_test_9J565P8EY847JAKEKF7F9JX94HJN",
                    company_name = "TFS",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')
add_logo("logo-250.png", height=200)
LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

def show_book():
    stb.set_book_config(
                menu_title=None,
                menu_icon="public",
                options=[
                    "Dashboard",
                    "Clients",
                    "Employees",
                    ], 
                paths=[
                    "admin/charts.py",
                    "admin/clients.py",
                    "admin/employees.py"
                    ],
                save_answers=False,
                styles={
                    "nav-link": {"--hover-color": "#fde8ec"},
                    "nav-link-selected": {"background-color": "#DC143C"},
                    "nav-link": {"background": "0 0"}
                }
    )

if LOGGED_IN != True:
    st.stop()
else:
    show_book()
    st.write(username)
   # stb.render_file('clients.py')
   