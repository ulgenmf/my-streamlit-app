

import streamlit as st
import random
from shared.pages import pages
from streamlit_card import card
import random

# for page in pages:
#   if st.button(page["title"]):
#     st.switch_page(page["link"])
# cols = st.columns(3)

url = st.secrets['URL']
st.write()

for page in pages:

  res = card(title=page['title'],
         key=random.randint(1, 1000000),
         text=page['explanation'],
         image=page['image'],
         url=f"{url}{page['link']}",
         styles={
           'filter': {
             "background-color": 'rgba(28, 28, 28, 0.80)',
             "filter": "brightness(5%)",
           },
           "card": {
             "font-size": '18px',
             "background-color": "black",
             "width": "100%",
             "height": "400px",
             "border": "1px solid black",
             "padding": "20px",
             "overflow-wrap": "break-word",
             "word-break": "inherit",
             'gap': '10px'
           }
         })

print('asdjashd')
