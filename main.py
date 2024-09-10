import streamlit as st

readme_page = st.Page("pages/readme.py",
                      title="📚 Readme", icon=":material/bookmark:")

elt_data_page = st.Page("pages/etl_data.py",
                        title="⬆️ Get data from API", icon=":material/add_circle:")

view_graphic = st.Page("pages/view_graphic.py",
                       title="📉 Charts")

view_dataframe = st.Page("pages/view_dataframe.py",
                         title="🎲 DataFrame", )

pg = st.navigation(
    {
        "Readme": [readme_page],
        "Process Data": [elt_data_page],
        "Reports": [view_graphic, view_dataframe]
    }
)


st.set_page_config(page_title="Data manager",
                   page_icon=":material/edit:", layout='wide')

pg.run()
