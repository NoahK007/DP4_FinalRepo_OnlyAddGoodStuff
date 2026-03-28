import streamlit as st

def contact_us():
    
    st.title("Get in Touch!", text_alignment = "center")
    st.divider()
    col1, col2 = st.columns([1.5,1], gap="small")
    col2.image('pages/DrMcDonald.jpg', caption="Please direct all questions and concerns to Dr. McDonald, not the developers of this site : )")

    col1.subheader(":frowning_man: Dr. Colin McDonald")
    col1.markdown(":email: cmcdona@mcmaster.ca")
    col1.markdown(":classical_building: MDCL 3515/D  ")
    col1.markdown(":telephone_receiver: 905-525-9140 ext. 24131")

    col1.write("Disclaimer: Permission has been sought to use this epic photo.")

contact_us()
