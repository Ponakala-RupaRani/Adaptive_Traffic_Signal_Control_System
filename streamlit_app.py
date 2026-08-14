import streamlit as st

st.set_page_config(
    page_title="Smart Traffic AI",
    page_icon="🚦",
    layout="centered"
)

# ---------- CUSTOM STYLE ----------

st.markdown("""
<style>

.login-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-top: 40px;
}

.login-subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.login-box {
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #444;
}

</style>
""", unsafe_allow_html=True)


# ---------- LOGIN STATE ----------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------- LOGIN PAGE ----------

if not st.session_state.logged_in:

    st.markdown(
        '<div class="login-title">🚦 Smart Traffic AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-subtitle">'
        'AI-Based Four-Way Traffic Management System'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="login-box">',
        unsafe_allow_html=True
    )

    st.subheader("🔐 Login")

    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    login = st.button(
        "Login",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if login:

        if username == "admin" and password == "traffic123":

            st.session_state.logged_in = True
            st.rerun()

        else:

            st.error(
                "❌ Invalid username or password"
            )

    st.caption(
        "Smart Traffic AI • Secure Demo Portal"
    )

    st.stop()


# ---------- DASHBOARD ----------

st.title("🚦 Smart Traffic AI")
st.subheader(
    "AI-Based Four-Way Traffic Management System"
)

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

st.markdown("---")


# ---------- VIDEO ----------

st.header("🎥 Traffic Video")

uploaded_video = st.file_uploader(
    "Upload Traffic Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_video:

    st.success(
        "✅ Traffic video uploaded successfully!"
    )

    st.video(uploaded_video)


st.markdown("---")


# ---------- TRAFFIC DATA ----------

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


priority = max(
    traffic,
    key=traffic.get
)


# ---------- TRAFFIC ANALYSIS ----------

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


# ---------- SMART SIGNAL ----------

st.markdown("---")

st.header("🚦 Smart Signal Decision")

st.success(
    f"Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: "
    f"{green_time(traffic[priority])} seconds"
)

st.info(
    "Higher traffic density receives a longer "
    "green signal."
)

st.markdown("---")

st.caption(
    "Smart Traffic AI — Four-Way Traffic Management Prototype"
)
