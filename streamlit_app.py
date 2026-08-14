import streamlit as st

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="centered"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown(
        """
        <div style="
            text-align: center;
            margin-top: 80px;
            margin-bottom: 30px;
        ">
            <div style="font-size: 90px;">
                🚦
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    if st.button("LOGIN", use_container_width=True):
        button color=green

        if username == "admin" and password == "traffic123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()
