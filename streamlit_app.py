import streamlit as st
from pages.apply_leave import apply_leave
from pages.display_leaves import display_leaves
from pages.account import app
from database import Base, engine
Base.metadata.create_all(engine)

PAGES = {
    "Home" : app,
    "Apply Leave": apply_leave,
    "Display Leaves": display_leaves
}
page = st.sidebar.selectbox("Go to", list(PAGES.keys()))
print(PAGES[page])
PAGES[page]()
