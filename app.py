import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_login_auth_ui.widgets import __login__
import streamlit_book as stb


__login__obj = __login__(auth_token = "pk_test_9J565P8EY847JAKEKF7F9JX94HJN",
                    company_name = "TFS",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = True,
                    hide_footer_bool = True,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')
add_logo("logo-250.png", height=200)
LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <a class="navbar-brand" href="#">Fixed navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
        </ul>
        <form class="form-inline mt-2 mt-md-0">
          <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
    """,
    height=80
)

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

if LOGGED_IN is not True:
    st.stop()
else:
    show_book()
    # st.write(username)
   # stb.render_file('clients.py')
   