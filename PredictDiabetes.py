import home
import indexSVM
import indexRFC
import streamlit as st
PAGES = {
    "Home": home,
    "Support Vector Machine": indexSVM,
    "Random Forest Classifier": indexRFC
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.main()