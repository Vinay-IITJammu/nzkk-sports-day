import streamlit as st
import pandas as pd

st.set_page_config(page_title="NZKK Sports Day 2025", layout="wide")

df = pd.read_csv("data.csv")

# Logo and event info
st.image("logo.jpg", width=120)
st.title("New Zealand Kannada Koota - Sports Day 2025")
st.markdown("📅 **Date:** Sunday, 14 July 2025")
st.markdown("📍 **Location:** Action Indoor Sports, Takanini")
st.markdown("⏰ **Time:** 9:00 AM – 6:00 PM")
st.markdown("---")

# Filters
with st.expander("🔍 Filter Participants", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        sport = st.multiselect("Select Sport", df["Sport"].unique())
    with col2:
        category = st.multiselect("Select Category", df["Category"].unique())
    with col3:
        name_search = st.text_input("Search by Name")

    clear = st.button("Clear Filters")
    if clear:
        st.experimental_rerun()

# Apply filters
filtered = df.copy()
if sport:
    filtered = filtered[filtered["Sport"].isin(sport)]
if category:
    filtered = filtered[filtered["Category"].isin(category)]
if name_search:
    filtered = filtered[filtered["Name"].str.contains(name_search, case=False)]

st.subheader("📋 Registered Participants")
st.dataframe(filtered, use_container_width=True)

# Download
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Filtered Data", data=csv, file_name="filtered_participants.csv", mime="text/csv")

st.markdown("---")
st.markdown("✅ Created by **EC, NZKK**")
