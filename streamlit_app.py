import streamlit as st

st.set_page_config(
    page_title="Smart Traffic AI",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Smart Traffic AI")
st.subheader("AI-Based Four-Way Traffic Management System")

st.markdown("---")

# Demo traffic counts
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

st.header("Traffic Analysis")

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
        st.write(f"Density: **{density(traffic[side])}**")
        st.write(f"Green: **{green_time(traffic[side])} sec**")

st.markdown("---")

st.header("🚦 Smart Signal Decision")

st.success(
    f"Priority: {priority} | "
    f"Vehicles: {traffic[priority]} | "
    f"Green Signal: {green_time(traffic[priority])} seconds"
)

st.info(
    "Higher traffic density receives a longer green signal."
)

st.markdown("---")

st.caption(
    "Smart Traffic AI — Four-Way Traffic Management Prototype"
)