import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="centered"
)


# =====================================================
# CSS
# =====================================================

st.markdown(
    """
    <style>

    /* Black background */
    .stApp {
        background-color: #000000;
    }

    .block-container {
        padding-top: 0rem;
    }

    /* Traffic light logo */
    .traffic-logo {
        text-align: center;
        font-size: 90px;
        margin-top: 70px;
        margin-bottom: 25px;
    }

    /* Login button */
    div.stButton > button {
        width: 100%;
        height: 50px;

        background-color: #20a464;
        color: white;

        border: none;
        border-radius: 8px;

        font-size: 18px;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #188951;
        color: white;
    }

    /* Labels */
    label {
        color: white !important;
    }

    /* Input boxes */
    div[data-baseweb="input"] {
        background-color: #1a1a1a !important;
        border: 1px solid #444444 !important;
    }

    div[data-baseweb="input"] input {
        color: white !important;
    }

    div[data-baseweb="input"] input::placeholder {
        color: #aaaaaa !important;
    }

    /* Password eye icon */
    div[data-baseweb="input"] svg {
        color: white !important;
    }

    /* Forgot password */
    .forgot-text {
        text-align: right;
        color: #20a464;
        font-size: 14px;
        margin-top: -5px;
        margin-bottom: 12px;
    }

    /* Footer */
    .login-footer {
        text-align: center;
        color: #bbbbbb;
        margin-top: 25px;
        font-size: 15px;
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

    # -------------------------------------------------
    # LOGO
    # -------------------------------------------------

    st.markdown(
        """
        <div class="traffic-logo">
            🚦
        </div>
        """,
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # TITLE
    # -------------------------------------------------

    st.markdown(
        """
        <h1 style="
            text-align:center;
            color:white;
            font-size:32px;
        ">
            Adaptive Traffic Signal
            Control System
        </h1>

        <p style="
            text-align:center;
            color:#bbbbbb;
            font-size:17px;
            margin-bottom:35px;
        ">
            Smart Traffic Control for Smarter Cities
        </p>
        """,
        unsafe_allow_html=True
    )


    # -------------------------------------------------
    # USERNAME
    # -------------------------------------------------

    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )


    # -------------------------------------------------
    # PASSWORD
    # -------------------------------------------------

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )


    # -------------------------------------------------
    # FORGOT PASSWORD
    # -------------------------------------------------

    st.markdown(
        """
        <div class="forgot-text">
            Forgot Password?
        </div>
        """,
        unsafe_allow_html=True
    )

    forgot = st.button(
        "Forgot Password?"
    )

    if forgot:
        st.info(
            "Please contact the system administrator "
            "to reset your password."
        )


    # -------------------------------------------------
    # LOGIN
    # -------------------------------------------------

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


    # -------------------------------------------------
    # FOOTER
    # -------------------------------------------------

    st.markdown(
        """
        <div class="login-footer">
            👥 Smart Signals. Smooth Traffic. Safer Roads.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.stop()


# =====================================================
# AFTER LOGIN
# =====================================================

st.markdown(
    """
    <h1 style="
        color:white;
        text-align:center;
    ">
        🚦 Adaptive Traffic Signal Control System
    </h1>
    """,
    unsafe_allow_html=True
)

st.success("Login successful!")


# =====================================================
# LOGOUT
# =====================================================

if st.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()
