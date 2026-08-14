import streamlit as st

st.set_page_config(
    page_title="Smart Traffic AI",
    page_icon="🚦",
    layout="wide"
)

# ---------------- LOGIN ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🚦 Smart Traffic AI")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        # Demo credentials
        if username == "admin" and password == "traffic123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

    st.info("Demo Username: admin")

    st.stop()


# ---------------- DASHBOARD ----------------

st.title("🚦 Smart Traffic AI")
st.subheader("AI-Based Four-Way Traffic Management System")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.markdown("---")

uploaded_video = st.file_uploader(
    "🎥 Upload Traffic Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_video:
    st.success("✅ Video uploaded successfully!")
    st.video(uploaded_video)

st.markdown("---")

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
    return "HIGH"

def green_time(count):
    if count <= 2:
        return 20
    elif count <= 4:
        return 30
    return 45

priority = max(traffic, key=traffic.get)

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
            f"Green: **{green_time(traffic[side])} sec**"
        )

st.markdown("---")

st.header("🚦 Smart Signal Decision")

st.success(
    f"Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: {green_time(traffic[priority])} seconds"
)
