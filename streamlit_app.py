import streamlit
import pandas
streamlit.header ('A header with _italics_ :blue[colors] and emojis :sunglasses:')
streamlit.title('My Moms New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3  & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spanish & Rocket Smothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

