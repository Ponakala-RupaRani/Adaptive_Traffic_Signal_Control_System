import streamlit as st
import base64

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="wide"
)

# =====================================================
# LOGIN STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# =====================================================
# BACKGROUND IMAGE
# =====================================================

def get_base64_image(path):

    with open(path, "rb") as file:
        return base64.b64encode(
            file.read()
        ).decode()


bg_image = get_base64_image("login_bg.png")


# =====================================================
# LOGIN PAGE
# =====================================================

if not st.session_state.logged_in:

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
                url("data:image/png;base64,{bg_image}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            min-height: 100vh;
        }}

        [data-testid="stHeader"] {{
            background: transparent;
        }}

        .login-box {{
            background: rgba(255,255,255,0.96);
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.15);
            margin-top: 180px;
        }}

        .project-title {{
            text-align: center;
            font-size: 38px;
            font-weight: 700;
            color: #17324d;
            margin-top: 50px;
        }}

        .subtitle {{
            text-align: center;
            font-size: 18px;
            color: #5b6b7c;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    # Space for the logo/title area in the image
    st.markdown(
        """
        <div class="project-title">
            Adaptive Traffic Signal Control System
        </div>

        <div class="subtitle">
            Smart Traffic Control for Smarter Cities
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Center login form
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
            type="password",
            placeholder="Enter your password"
        )

        login = st.button(
            "Login",
            use_container_width=True
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                margin-top:20px;
                color:#5b6b7c;
            ">
                👥 Smart Signals. Smooth Traffic. Safer Roads.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
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

    st.stop()


# =====================================================
# DASHBOARD
# =====================================================

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

priority = max(
    traffic,
    key=traffic.get
)

signal_order = sorted(
    traffic,
    key=traffic.get,
    reverse=True
)

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
