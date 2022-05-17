import streamlit as st
from multiapp import MultiApp
# import your app modules here 
from apps import tab1, tab2, tab3 
# if you do not wish to have a separate folder (apps) for saving the files (tab1.py, tab2.py, tab3.py)
# the app modules can also be placed in the same location as app.py and multiapp.py
# and can be imported as "import tab1, tab2, tab3"

st.set_page_config(layout='wide')

app = MultiApp()

# Add all your application here
app.add_app("Tab1", tab1.app)
app.add_app("Tab2", tab2.app)
app.add_app("Tab3", tab3.app)

# The main app
app.run()
