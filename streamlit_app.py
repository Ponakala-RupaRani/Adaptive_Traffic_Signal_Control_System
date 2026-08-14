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
            text-align:center;
            padding:40px 10px 20px 10px;
        ">

            <div style="
                font-size:75px;
            ">
                🚦
            </div>

            <h1>
                ADAPTIVE TRAFFIC SIGNAL
                CONTROL SYSTEM
            </h1>

            <p style="font-size:18px;">
                AI-Based Four-Way Traffic Management System
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    if st.button(
        "🚦 LOGIN",
        use_container_width=True
    ):

        if username == "admin" and password == "traffic123":

            st.session_state.logged_in = True
            st.rerun()

        else:

            st.error(
                "❌ Invalid username or password"
            )

    st.stop()
