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

        if username == "admin" and password == "traffic123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()

# =====================================================
# DASHBOARD AFTER LOGIN
# =====================================================

st.set_page_config(
    page_title="Adaptive Traffic Signal Control System",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Adaptive Traffic Signal Control System")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.markdown("---")

# Video Upload
st.header("🎥 Traffic Video")

uploaded_video = st.file_uploader(
    "Upload Traffic Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_video:
    st.success("Video uploaded successfully!")
    st.video(uploaded_video)

st.markdown("---")

# Traffic Counts
traffic = {
    "NORTH": 3,
    "EAST": 4,
    "SOUTH": 5,
    "WEST": 2
}

def density(count):
    if count <= 2:
        return "LOW"
    elif count <= 4:
        return "MEDIUM"
    else:
        return "HIGH"

def green_time(count):
    if count <= 2:
        return 20
    elif count <= 4:
        return 30
    else:
        return 45

priority = max(traffic, key=traffic.get)

# Traffic Analysis
st.header("📊 Traffic Analysis")

col1, col2, col3, col4 = st.columns(4)

for col, side in zip(
    [col1, col2, col3, col4],
    ["NORTH", "EAST", "SOUTH", "WEST"]
):
    with col:
        st.metric(
            side,
            f"{traffic[side]} vehicles"
        )

        st.write(
            f"Density: **{density(traffic[side])}**"
        )

        st.write(
            f"Green Signal: **{green_time(traffic[side])} sec**"
        )

# Smart Signal
st.markdown("---")

st.header("🚦 Smart Signal Decision")

st.success(
    f"Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: {green_time(traffic[priority])} seconds"
)
