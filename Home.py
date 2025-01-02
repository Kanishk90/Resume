import streamlit as st

pages = [
        st.Page("contact.py", title="Contact Me"),
        st.Page("Project.py", title="Projects"),

        st.Page("resume.py", title="Resume"),
        st.Page("resources.py", title="Resources")
        

]

pg = st.navigation(pages)
pg.run()