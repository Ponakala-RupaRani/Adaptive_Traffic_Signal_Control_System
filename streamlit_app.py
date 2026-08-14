import streamlit as st
import base64

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

    # -----------------------------------------------------
    # LOAD BACKGROUND IMAGE
    # -----------------------------------------------------

    try:
        with open("login_background.png", "rb") as f:
            image_data = base64.b64encode(
                f.read()
            ).decode()

        background = (
            f"data:image/png;base64,{image_data}"
        )

    except:
        background = ""


    # -----------------------------------------------------
    # CSS
    # -----------------------------------------------------

    st.markdown(
        f"""
        <style>

        /* Hide Streamlit UI */
        #MainMenu {{
            visibility: hidden;
        }}

        header {{
            visibility: hidden;
        }}

        footer {{
            visibility: hidden;
        }}

        .stApp {{
            background-image:
                url("{background}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }}

        /* Dark/light overlay */
        .stApp::before {{
            content: "";
            position: fixed;
            inset: 0;

            background: rgba(
                255,
                255,
                255,
                0.20
            );

            z-index: 0;
            pointer-events: none;
        }}

        /* Main content */
        .main-content {{
            position: relative;
            z-index: 2;
        }}

        /* Title */
        .project-title {{
            text-align: center;

            font-size: 42px;
            font-weight: 700;

            color: #183047;

            margin-top: 45px;

            letter-spacing: 1px;
        }}

        .title-line {{
            width: 70px;
            height: 4px;

            background: #20a464;

            margin: 18px auto;

            border-radius: 10px;
        }}

        .project-subtitle {{
            text-align: center;

            font-size: 20px;

            color: #526276;

            margin-bottom: 35px;
        }}

        /* Login area */
        .login-box {{
            width: 520px;

            max-width: 90%;

            margin: 0 auto;

            padding: 28px 38px 25px 38px;

            background: rgba(
                255,
                255,
                255,
                0.96
            );

            border-radius: 20px;

            box-shadow:
                0 10px 35px
                rgba(0,0,0,0.20);
        }}

        /* Labels */
        label {{
            color: #172b40 !important;
            font-weight: 600 !important;
        }}

        /* Inputs */
        div[data-baseweb="input"] {{
            border-radius: 10px !important;
            background: white !important;
        }}

        div[data-baseweb="input"] input {{
            font-size: 17px !important;
        }}

        /* Login button */
        .stButton > button {{
            width: 100%;

            height: 52px;

            background: #20a464;

            color: white;

            border: none;

            border-radius: 9px;

            font-size: 19px;

            font-weight: 600;

            margin-top: 12px;
        }}

        .stButton > button:hover {{
            background: #188951;
            color: white;
        }}

        /* Bottom text */
        .login-footer {{
            text-align: center;

            margin-top: 20px;

            font-size: 16px;

            color: #526276;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # MAIN CONTENT
    # =====================================================

    st.markdown(
        '<div class="main-content">',
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------

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
    # LOGIN BOX
    # =====================================================

    # Use columns to create a centered login area
    left, center, right = st.columns(
        [1, 2, 1]
    )

    with center:

        st.markdown(
            '<div class="login-box">',
            unsafe_allow_html=True
        )

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            placeholder="Enter your password",
            type="password"
        )

        login = st.button(
            "Login",
            use_container_width=True
        )

        if login:

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


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.stop()


# =========================================================
# AFTER LOGIN
# =========================================================

st.title(
    "🚦 Adaptive Traffic Signal Control System"
)

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

    st.success(
        "Video uploaded successfully!"
    )

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
signal_order = sorted(
    traffic,
    key=traffic.get,
    reverse=True
)

priority = signal_order[0]

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
