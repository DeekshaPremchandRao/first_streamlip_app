import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header ('A header with _italics_ :blue[colors] and emojis :sunglasses:')
streamlit.title('My Moms New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3  & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spanish & Rocket Smothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create a repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    #streamlit.text(fruityvice_response.json()) # just writes data to the screen
    # takes the json version of the response and normalise it
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # output it the screen as a table
    return fruityvice_normalized


# New section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice=streamlit.text_input('What fruit do you like information about?','Kiwi')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
       back_from_function= get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()

# don't run anything past here while we trubleshoot
#streamlit.stop()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return  my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

#Allow the end user to add the fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
         return  "Thanks for adding" + new_fruit

fruit_choice = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function= insert_row_snowflake(fruit_choice)
    streamlit.dataframe(back_from_function)



