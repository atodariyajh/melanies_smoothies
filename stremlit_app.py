# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

st.title(":cup_with_straw: Customize Your Smoothie  :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smoothie"""
)
from snowflake.snowpark.functions import col

name_on_order = st.text_input("Name of Smoothie")
st.write("The Name on your smoothie will be :", name_on_order)

from snowflake.snowpark.functions import col


#session = get_Active_session()

cnx = st.connection("snowflake")
session = cnx.session()
