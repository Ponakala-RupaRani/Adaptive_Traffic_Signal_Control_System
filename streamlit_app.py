import streamlit as st

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="centered"
)

# =====================================================
# GREEN LOGIN BUTTON STYLE
# =====================================================

st.markdown(
    """
    <style>

    /* Login button */
    div.stButton > button {
        width: 100%;
        height: 50px;

        background-color: #20a464;
        color: black;

        border: none;
        border-radius: 8px;

        font-size: 18px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #188951;
        color: white;
    }

    /* Center the traffic light */
    .traffic-logo {
        text-align: center;
        font-size: 90px;
        margin-top: 70px;
        margin-bottom: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# LOGIN STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged_in:

    # Logo
    st.markdown(
        """
        <div class="traffic-logo">
            🚦
        </div>
        """,
        unsafe_allow_html=True
    )

    # Title
    st.markdown(
        """
        <h1 style="
            text-align:center;
            color:#183047;
            font-size:32px;
        ">
            Adaptive Traffic Signal
            Control System
        </h1>

        <p style="
            text-align:center;
            color:#526276;
            font-size:17px;
            margin-bottom:35px;
        ">
            Smart Traffic Control for Smarter Cities
        </p>
        """,
        unsafe_allow_html=True
    )


    # Username
    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )


    # Password
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )


    # Login button
    if st.button(
        "LOGIN",
        use_container_width=True
    ):

        if (
            username == "admin"
            and password == "traffic123"
        ):

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error(
                "Invalid username or password"
            )


    st.markdown(
        """
        <p style="
            text-align:center;
            color:#526276;
            margin-top:25px;
        ">
            👥 Smart Signals. Smooth Traffic. Safer Roads.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.stop()


# =====================================================
# AFTER LOGIN
# =====================================================

st.title(
    "🚦 Adaptive Traffic Signal Control System"
)

st.success(
    "Login successful!"
)

if st.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
