import streamlit as st
import base64

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
# LOAD LOGIN BACKGROUND
# =========================================================

def load_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


bg = load_image("login_bg.png")


# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    st.markdown(
        f"""
        <style>

        /* Remove Streamlit default spacing */
        .block-container {{
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }}

        [data-testid="stHeader"] {{
            display: none;
        }}

        /* Full background */
        .stApp {{
            background-image: url(
                "data:image/png;base64,{bg}"
            );

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;

            min-height: 100vh;
        }}

        /* White cover over the ORIGINAL form in image */
        .login-cover {{
            position: fixed;
            top: 48%;
            left: 50%;
            transform: translate(-50%, -50%);

            width: 500px;
            height: 390px;

            background: rgba(255,255,255,0.98);

            border-radius: 22px;

            box-shadow:
                0px 10px 35px
                rgba(0,0,0,0.18);

            z-index: 1;
        }}

        /* Real Streamlit form */
        .login-content {{
            position: fixed;
            top: 48%;
            left: 50%;

            transform: translate(-50%, -50%);

            width: 430px;

            z-index: 10;
        }}

        .login-heading {{
            text-align: center;
            font-size: 27px;
            font-weight: 700;
            color: #17324d;
            margin-bottom: 20px;
        }}

        </style>

        <div class="login-cover"></div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # REAL LOGIN FORM
    # =====================================================

    st.markdown(
        '<div class="login-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="login-heading">
            Login
        </div>
        """,
        unsafe_allow_html=True
    )

    username = st.text_input(
        "Username",
        placeholder="Enter your username",
        key="username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
        key="password"
    )

    login_button = st.button(
        "Login",
        use_container_width=True
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            margin-top:18px;
            color:#5b6b7c;
            font-size:15px;
        ">
            🚦 Smart Signals. Smooth Traffic. Safer Roads.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # LOGIN CHECK
    # =====================================================

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

    st.stop()


# =========================================================
# DASHBOARD AFTER LOGIN
# =========================================================

st.title(
    "🚦 Adaptive Traffic Signal Control System"
)

if st.button("Logout"):

    st.session_state.logged_in = False
    st.rerun()


st.markdown("---")

st.header("🎥 Traffic Analysis")

uploaded_video = st.file_uploader(
    "Upload Traffic Video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video:

    st.success(
        "Traffic video uploaded successfully!"
    )

    st.video(uploaded_video)


st.markdown("---")

st.header("📊 Four-Way Traffic Status")


# =========================================================
# DEMO VALUES
# =========================================================

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


# Highest traffic gets first priority

priority = max(
    traffic,
    key=traffic.get
)


signal_order = sorted(
    traffic,
    key=traffic.get,
    reverse=True
)


# =========================================================
# WAITING TIME
# =========================================================

waiting = {}
total = {}

current_wait = 0

for direction in signal_order:

    waiting[direction] = current_wait

    total[direction] = (
        current_wait
        + green_times[direction]
    )

    current_wait += green_times[direction]


# =========================================================
# DISPLAY
# =========================================================

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
            f"{waiting[direction]} sec"
        )

        st.write(
            f"**Total Time:** "
            f"{total[direction]} sec"
        )


st.markdown("---")

st.success(
    f"🚦 Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: "
    f"{green_times[priority]} seconds"
)
