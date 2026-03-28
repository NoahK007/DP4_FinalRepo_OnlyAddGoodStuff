import streamlit as st

#Feedback Dialog
@st.dialog("Send Feedback", width = "medium", dismissible = True, icon = '📃')
def give_feedback():
    selected = st.feedback("stars")
    fb = st.text_input("Share your feedback below:")
    if st.button("Submit Feedback"):
        st.rerun()

def home_page():
    
    st.set_page_config(initial_sidebar_state="expanded", page_title="Maccessible")

    #Remove the extra page things at the top that are unnecessary and
    #unfortunately don't have emojis
    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

    st.title("**MACCESSIBLE**  :sunglasses:!", width = "stretch", text_alignment = "center")
    st.space("xsmall")
    st.markdown("Your all-in-one place for accessibility mapping, currently available only at McMaster University.",
                text_alignment = "center")

    #Setting Sidebar to have linked pages (i.e. like a menu) (not buttons)
    ##
    st.sidebar.subheader("Menu")
    st.sidebar.page_link("Home.py", label = "Home", icon = '🏠')
    st.sidebar.page_link("pages/Map.py", label = "Map", icon = '🚗')
    st.sidebar.page_link("pages/Help.py", label = "Help!", icon = '⁉️')
    st.sidebar.page_link("pages/About Us.py", label = "About Us...", icon = '✨')
    st.sidebar.page_link("pages/FAQs.py", label = "FAQs", icon = '❓')
    st.sidebar.page_link("pages/Dr McDonald's Contact Info.py", label =
                         "Dr McDonald's Contact Info", icon = '💯')

    st.space("small")
    st.balloons()
    to_map = st.button("Take me to Map!", icon = '➡️', width="stretch")
    if to_map:
        st.switch_page("pages/Map.py")
    elif to_map and data_to != None and data_from != None:
        st.switch_page("pages/Map.py")
    #Feedback Form
    st.space("xsmall")    
    feedback = st.button(":bar_chart: Looking to give feedback?", width = "stretch")
    if feedback:
        give_feedback()
            
home_page()
