import pandas as pd
import plotly.express as px
import streamlit as st
# from js import name, addTwoNumbers

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

# ---- READ EXCEL ----
# @st.cache
# def get_data_from_excel():
#     df = pd.read_csv("data.csv")
#     return df

# df = get_data_from_excel()
df = pd.read_csv("data.csv")

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
options = st.sidebar.selectbox('Options', ('Filter Data', 'Search Data'))
st.sidebar.empty()
if options == 'Filter Data':
    city = st.sidebar.multiselect(
        "Select the City:",
        options=df["CITY"].unique(),
        default=df["CITY"].unique()
    )

    policy_type = st.sidebar.multiselect(
        "Select the Policy Type:",
        options=df["POLICY_TYPE"].unique(),
        default=df["POLICY_TYPE"].unique(),
    )

    policy_cover = st.sidebar.multiselect(
        "Select the Policy Cover:",
        options=df["POLICY_COVER"].unique(),
        default=df["POLICY_COVER"].unique(),
    )

    gender = st.sidebar.multiselect(
        "Select the Gender:",
        options=df["GENDER"].unique(),
        default=df["GENDER"].unique()
    )

    paid = st.sidebar.multiselect(
        "Select the paid the month:",
        options=df["HAS_PAID"].unique(),
        default=df["HAS_PAID"].unique()
    )

    df_selection = df.query(
        "HAS_PAID == @paid  & POLICY_COVER == @policy_cover &  CITY == @city & POLICY_TYPE == @policy_type & GENDER == @gender"
    )

    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_sales = int(df_selection["MONTHLY_PREMIUM"].sum())
    # average_rating = round(df_selection["Rating"].mean(), 1)
    # star_rating = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df_selection["MONTHLY_PREMIUM"].mean(), 2)

    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Totals Expected:")
        st.subheader(f"R {total_sales:,}")
    with right_column:
        st.subheader("Average Rating:")
        # st.subheader(f"{average_rating} {star_rating}")
    with right_column:
        st.subheader("Average Sales Per Transaction:")
        st.subheader(f"R {average_sale_by_transaction}")

    # st.markdown("""---""")

    # SALES BY PRODUCT LINE [BAR CHART]
    sales_by_product_line = (
        df_selection.groupby(by=["POLICY_TYPE"]).sum()[["MONTHLY_PREMIUM"]].sort_values(by="MONTHLY_PREMIUM")
    )
    st.dataframe(sales_by_product_line)
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="MONTHLY_PREMIUM",
        y=sales_by_product_line.index,
        orientation="h",
        title="<b>Sales by Product Line</b>",
        color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
        template="plotly_white",
    )
    fig_product_sales.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )
    left_column, right_column = st.columns(2)
    # left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
    right_column.plotly_chart(fig_product_sales, use_container_width=True)

# <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
# <script defer src="https://pyscript.net/latest/pyscript.js"></script>

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)