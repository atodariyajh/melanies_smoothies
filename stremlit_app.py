# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

st.title(":cup_with_straw: Customize Your Smoothie  :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smoothie"""
)
from snowflake.snowpark.functions import col

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

session = get_Active_session()

cnx = st.connection("snowflake")
session = cnx.session()
