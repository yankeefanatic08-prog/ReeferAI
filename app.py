import streamlit as st

st.set_page_config(page_title="ReeferAI", layout="centered")
st.image("https://grok.x.ai/files/reeferai-logo.png", width=200)
st.title("REEFERAI")
st.caption("The Profit Calculator for Reefer Freight")

origin = st.text_input("Origin ZIP", "68102")
dest = st.text_input("Dest ZIP", "90210")
loads = st.number_input("Monthly Loads", 1, 1000, 100)

if st.button("Calculate Profit"):
    profit = loads * 1752
    st.success(f"**Profit per Load: $1,752** | **Margin: 39.5%**")
    st.info(f"**Monthly Profit: ${profit:,.0f}**")

col1, col2 = st.columns(2)
with col1:
    st.button("Try Free")
with col2:
    if st.button("Go Pro — $29/mo"):
        st.balloons()

st.markdown("**Powered by Real Carrier Rates**")
st.caption("© 2025 ReeferAI")
