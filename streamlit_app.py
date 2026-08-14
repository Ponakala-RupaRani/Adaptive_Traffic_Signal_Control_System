import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="wide"
)


# =====================================================
# CSS
# =====================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #000000;
    }

    .block-container {
        padding-top: 1rem;
    }

    /* Login logo */
    .traffic-logo {
        text-align: center;
        font-size: 90px;
        margin-top: 50px;
        margin-bottom: 20px;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #20a464;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: 600;
        height: 50px;
    }

    div.stButton > button:hover {
        background-color: #188951;
        color: white;
    }

    /* Labels */
    label {
        color: white !important;
    }

    /* Input */
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

    /* Dashboard text */
    h1, h2, h3, p {
        color: white;
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

    st.markdown(
        """
        <div class="traffic-logo">
            🚦
        </div>
        """,
        unsafe_allow_html=True
    )

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

    # Forgot password
    col1, col2 = st.columns([4, 1])

    with col2:

        forgot = st.button(
            "Forgot Password?"
        )

    if forgot:

        st.info(
            "Please contact the system administrator "
            "to reset your password."
        )

    # Login
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
            color:#bbbbbb;
            margin-top:25px;
        ">
            👥 Smart Signals. Smooth Traffic. Safer Roads.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.stop()


# =====================================================
# DASHBOARD AFTER LOGIN
# =====================================================

st.markdown(
    """
    <h1 style="
        text-align:center;
        color:white;
    ">
        🚦 Adaptive Traffic Signal Control System
    </h1>

    <p style="
        text-align:center;
        color:#bbbbbb;
        font-size:18px;
    ">
        AI-Based Four-Way Traffic Management System
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")


# =====================================================
# LOGOUT
# =====================================================

logout_col1, logout_col2 = st.columns([6, 1])

with logout_col2:

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()


# =====================================================
# VIDEO UPLOAD
# =====================================================

st.header("🎥 Traffic Video")

uploaded_video = st.file_uploader(
    "Upload your traffic video",
    type=["mp4", "avi", "mov"],
    help="Upload the four-way traffic video for analysis."
)


# =====================================================
# SHOW VIDEO
# =====================================================

if uploaded_video is not None:

    st.success(
        "Traffic video uploaded successfully!"
    )

    st.video(
        uploaded_video
    )


# =====================================================
# TRAFFIC ANALYSIS
# =====================================================

st.markdown("---")

st.header("📊 Traffic Analysis")


# Demo values
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


# =====================================================
# SIGNAL ORDER
# =====================================================

signal_order = sorted(
    traffic,
    key=traffic.get,
    reverse=True
)

priority = signal_order[0]


# =====================================================
# WAITING + TOTAL
# =====================================================

waiting_times = {}
total_times = {}

current_wait = 0

for direction in signal_order:

    waiting_times[direction] = current_wait

    total_times[direction] = (
        current_wait
        + green_times[direction]
    )

    current_wait += green_times[direction]


# =====================================================
# DISPLAY FOUR DIRECTIONS
# =====================================================

cols = st.columns(4)

for col, direction in zip(
    cols,
    ["NORTH", "EAST", "SOUTH", "WEST"]
):

    with col:

        st.subheader(
            direction
        )

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


# =====================================================
# SMART SIGNAL DECISION
# =====================================================

st.markdown("---")

st.header(
    "🚦 Smart Signal Decision"
)

st.success(
    f"Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: "
    f"{green_times[priority]} seconds"
)

st.info(
    "The direction with the highest number "
    "of vehicles receives priority."
)
