import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOGIN STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    # Hide Streamlit default elements
    st.markdown(
        """
        <style>

        #MainMenu {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        .stApp {
            background: #eef5f8;
        }

        /* Remove top spacing */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }

        /* Background image */
        .login-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;

            background-image:
                linear-gradient(
                    rgba(255,255,255,0.08),
                    rgba(255,255,255,0.08)
                ),
                url("login_background.png");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;

            z-index: 0;
        }

        /* Login card */
        .login-card {
            position: relative;
            z-index: 5;

            width: 520px;
            max-width: 90vw;

            margin: 170px auto 0 auto;

            padding: 35px 38px 28px 38px;

            background: rgba(255,255,255,0.96);

            border-radius: 20px;

            box-shadow:
                0 10px 35px rgba(0,0,0,0.18);

            text-align: left;
        }

        /* Project title */
        .project-title {
            position: relative;
            z-index: 5;

            text-align: center;

            margin-top: 45px;

            font-size: 43px;
            font-weight: 700;

            color: #183047;

            letter-spacing: 1px;
        }

        .project-subtitle {
            position: relative;
            z-index: 5;

            text-align: center;

            margin-top: 15px;

            font-size: 20px;

            color: #526276;
        }

        .title-line {
            width: 70px;
            height: 4px;

            background: #20a464;

            margin: 18px auto;

            border-radius: 10px;
        }

        /* Input labels */
        label {
            font-weight: 600 !important;
            color: #172b40 !important;
        }

        /* Text boxes */
        div[data-baseweb="input"] {
            border-radius: 10px !important;
        }

        div[data-baseweb="input"] input {
            font-size: 17px !important;
        }

        /* Login button */
        .stButton > button {
            width: 100%;

            height: 52px;

            background: #20a464;

            color: white;

            border: none;

            border-radius: 9px;

            font-size: 19px;

            font-weight: 600;

            margin-top: 12px;
        }

        .stButton > button:hover {
            background: #188951;
            color: white;
        }

        /* Bottom message */
        .login-footer {
            text-align: center;

            margin-top: 25px;

            color: #526276;

            font-size: 16px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # BACKGROUND
    # =====================================================

    st.markdown(
        '<div class="login-background"></div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # PROJECT TITLE
    # =====================================================

    st.markdown(
        """
        <div class="project-title">
            Adaptive Traffic Signal Control System
        </div>

        <div class="title-line"></div>

        <div class="project-subtitle">
            Smart Traffic Control for Smarter Cities
        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # LOGIN CARD
    # =====================================================

    st.markdown(
        '<div class="login-card">',
        unsafe_allow_html=True
    )

    username = st.text_input(
        "Username",
        placeholder="Enter your username",
        key="username"
    )

    password = st.text_input(
        "Password",
        placeholder="Enter your password",
        type="password",
        key="password"
    )

    login_button = st.button(
        "Login",
        use_container_width=True
    )

    if login_button:

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
        <div class="login-footer">
            👥 Smart Signals. Smooth Traffic. Safer Roads.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.stop()


# =========================================================
# DASHBOARD
# =========================================================

st.title("🚦 Adaptive Traffic Signal Control System")

if st.button("Logout"):

    st.session_state.logged_in = False

    st.rerun()


st.markdown("---")

st.header("🎥 Traffic Video")

uploaded_video = st.file_uploader(
    "Upload Traffic Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_video:

    st.success("Video uploaded successfully!")

    st.video(uploaded_video)


st.markdown("---")

st.header("📊 Traffic Analysis")

traffic = {
    "NORTH": 3,
    "EAST": 4,
    "SOUTH": 5,
    "WEST": 2
}

green_times = {
    "NORTH": 20,
    "EAST": 30,
    "SOUTH": 45,
    "WEST": 10
}

# Highest traffic gets priority
priority = max(
    traffic,
    key=traffic.get
)

# Priority gets zero waiting time
signal_order = sorted(
    traffic,
    key=traffic.get,
    reverse=True
)

waiting_times = {}
total_times = {}

wait = 0

for direction in signal_order:

    waiting_times[direction] = wait

    total_times[direction] = (
        wait + green_times[direction]
    )

    wait += green_times[direction]


cols = st.columns(4)

for col, direction in zip(
    cols,
    ["NORTH", "EAST", "SOUTH", "WEST"]
):

    with col:

        st.subheader(direction)

        st.write(
            f"**Vehicles:** "
            f"{traffic[direction]}"
        )

        st.write(
            f"**Green Signal:** "
            f"{green_times[direction]} sec"
        )

        st.write(
            f"**Waiting Time:** "
            f"{waiting_times[direction]} sec"
        )

        st.write(
            f"**Total Time:** "
            f"{total_times[direction]} sec"
        )


st.markdown("---")

st.success(
    f"🚦 Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: "
    f"{green_times[priority]} seconds"
)
