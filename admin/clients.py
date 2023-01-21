import datetime
import streamlit as st
from db_fxn import *
from streamlit_login_auth_ui.widgets import __login__
import streamlit_book as stb
import extra_streamlit_components as stx
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization", "Data Manipulation"],
    icons=["pencil-fill", "bar-chart-fill", "bar-chart"],
    orientation="horizontal",
)

# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":

    with st.expander('Principle member', expanded=True):
        col1,col2 = st.columns(2)
        id_photo = ""
        
        with col1:
            first_name = st.text_input("First name", value="Tebza")
            id_no = st.text_input("ID Number", value=1130125766082, max_chars=13)
            email = st.text_input("Email", value="tebza.mre@gmail.com")
            gender = st.selectbox("Gender", ('Male', 'Female','Transgender', 'Rather not say'))
            start_date = st.date_input("Start date").isoformat()
        selected_id_photo_method = st.radio('Do you wish to upload an existing photo of your ID? or take a picture using camera?', ('Upload existing', 'Take a picture'))
        if selected_id_photo_method == 'Upload existing':
            uploaded_id_photo = st.file_uploader('Upload ID photo')
            if uploaded_id_photo is not None:
                id_photo = uploaded_id_photo
        else:
            taken_id_photo = st.camera_input(label='Take a picture of the ID photo', key=None, help='picture must be clear, well lit and not cropped', on_change=None, args=None, kwargs=None, disabled=False)
            if taken_id_photo is not None:
                id_photo = taken_id_photo
            
        with col2:
            last_name = st.text_input("last name", value="selepe")
            dob = st.date_input("Date of Birth")
            phone_no = st.text_input("Mobile number", value='+27', max_chars=12)
            race = st.selectbox("Ethnecity", ('African', 'Colored', 'Indian', 'Asian', 'Other' 'White'))
            payment_date = st.date_input("Payment date").isoformat()
        st.markdown('---')
        ben_col1,ben_col2 = st.columns(2)
        with ben_col1:
            beneficiary_names = st.text_input("Beneficiary's First and Last Names", value="kgomotso selepe")
        with ben_col2:
            beneficiary_phone = st.text_input("Beneficiary's contact number", value='+27', max_chars=12)

with st.expander('Dependants & Beneficiaries'):
    pol_col1,pol_col2,pol_col3 = st.columns(3)
    with pol_col1: 
        policy_type = st.radio("Policy type", ('Gold', 'Silver', 'Platinum'), horizontal=False)
    with pol_col2:
        policy_cover = st.radio("Policy cover", ('single', 'family'))
    num_dependents = 0
    with pol_col3:
        payment_method = st.radio("Payment method", ('Cash', 'SASSA','Direct-Bank'), horizontal=False)
    if policy_cover == 'family':
            num_dependents = st.slider("Number of Dependents", min_value=1, step=1, max_value=3, help='minimum of 1, maximum of 3 dependants')
        
st.markdown('---')
dependents = []
dep_col1, dep_col2,dep_col3,dep_col4 = st.columns(4)

for i in range(num_dependents):
    with dep_col1:
        dependent_names = st.text_input(f"Dependent {i+1} Full Name")
    with dep_col2:
        dependent_id = st.text_input(f"Dependent {i+1} ID number", max_chars=13)
    with dep_col3:
        relation = st.text_input(f"Relation with member", key={i+1})
    with dep_col4:
        dependent_dob = st.date_input(f"Dependent {i+1} Date of Birth")
    dependent_age = calculate_age(dependent_dob)
    dependents.append({"name" : dependent_names ,"id" : dependent_id , "age" : dependent_age})
policy_premium = calculate_policy_premium(policy_type, num_dependents)










































# Main_Memeber_TAB, Beneficiary_TAB, Dependants_TAB = st.tabs(["🎈Main Member", "🍕 Beneficiary", "☘ Dependants"])
# menu = ["Add Member","View Members","Update","Delete","About"]
# choice = st.sidebar.selectbox("Menu",menu)

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )

# with Main_Memeber_TAB:
    
#     st.header('Main Member Section (Policy Holder)')
#     with st.expander("Personal Details"):
        
#         COL_1,COL_2 = st.columns(2)
    
#         with COL_1:
#             first_name = st.text_input('first Name', key='Main_fname')
#             id_no = st.text_input("ID Number", max_chars=13, key='Main_id_no')
#             gender = st.selectbox("Gender", ("Male", "Female"), key='Main_gender')
#             martitial_status = st.selectbox("Maritial Status", ("Married", "Single", "Divorced"), key='martial_stats')
#             email = st.text_input("Email Address", key='Main_email')
#             employment_status = st.checkbox('Are you employed?', value=False)
#         with COL_2:
#             last_name = st.text_input('Last Name', key='Main_lname')
#             dob = st.date_input("Date of Birth",datetime.date(2019, 7, 6), min_value=None, key='Main_dob')
#             mobile_no = st.text_input("Mobile Number", value="+27", max_chars=12, key='Main_cell_no')
#             age = st.slider('Age', min_value=18, value=18, step=1, key='Main_age')
#             physical_address = st.text_area('Physical Address', key='phys_address')
#         btn_next = st.button('Next', key='MM_btn_next', help='Go onto the next step')
# with Beneficiary_TAB:
#     st.header('Beneficiary Section')
#     with st.expander("Personal Details"):
#         Bene_first_name = st.text_input('first Name', key='Bene_first_name')
#         Bene_id_no = st.text_input("ID Number", max_chars=13, key='Bene_id_no')
#         Bene_phone_no = st.text_input("Mobile Number", value="+27", max_chars=12, key='Bene_phone_no')
#         age = st.slider('Age', min_value=18, value=18, step=1)
#         Bene_physical_address = st.text_area('Physical Address', key='Bene_phys_address')
#     with st.expander('Relation with Main Member(policy holder)'):
#         relation_link = st.selectbox("What is your relation with the policy holder ? You're their...", ('Child', 'Romantic Partner', 'Sibling/Relative', 'Friend', 'Other'), help='What is your relation with the policy holder ?',key='relation_link')
#         if relation_link == 'Other':
#             relation_link_other = st.text_input('Other form of relation', key='other_relation_link', disabled=False)    

# with Dependants_TAB:
#     st.header('Dependants Section')
#     with st.expander("Personal Details"):
#         Dep_first_name = st.text_input('first Name', key='Dep_first_name')
#         Dep_id_no = st.text_input("ID Number", max_chars=13, key='Dep_id_no')
#         Dep_phone_no = st.text_input("Mobile Number", value="+27", max_chars=12, key='Dep_phone_no')
#         Dep_age = st.slider('Age', min_value=18, value=18, step=1, key='Dep_age')
#         Dep_physical_address = st.text_area('Physical Address', key='Dep_physical_address')
#     with st.expander('Relation with Main Member(policy holder)'):
#         Dep_relation_link = st.selectbox("What is your relation with the policy holder ? You're their...", ('Child', 'Romantic Partner', 'Sibling/Relative', 'Friend', 'Other'), help='What is your relation with the policy holder ?',key='dep_relation_link')
#         if relation_link == 'Other':
#             relation_link_other = st.text_input('Other form of relation', key='other_relation_link', disabled=False)