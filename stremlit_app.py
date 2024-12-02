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

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose up to 5 ingredients:',my_dataframe,max_selections=5)

#session = get_Active_session()

cnx = st.connection("snowflake")
session = cnx.session()
