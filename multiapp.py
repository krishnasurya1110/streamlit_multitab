"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from streamlit_option_menu import option_menu

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    # def run(self):    
    #     app = st.selectbox('Navigation', self.apps, format_func=lambda app: app['title'])
    #     app['function']()

    def run(self):
        #st.write(self.apps)
        titles = []
        for apps in self.apps:
             titles.append(apps['title'])
        selected_title = option_menu(None, titles, 
                                    icons=['house', 'cloud-upload', "list-task", 'gear'], 
                                    menu_icon="cast", default_index=0, orientation="horizontal",
                                    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
                                            "icon": {"color": "orange", "font-size": "25px"}, 
                                            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                            "nav-link-selected": {"background-color": "green"},} 
                                    )
        for apps in self.apps:
            if apps['title'] == selected_title:
                apps['function']()
        
