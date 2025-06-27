import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Display logo and title
st.image("logo.jpg", width=120)
st.title("New Zealand Kannada Koota Sports Day - 2025")

# Sidebar filters
with st.sidebar:
    st.header("🎯 Filter Tournament Entries")
    sport_filter = st.multiselect("Select Sport", df["Sport"].unique())
    name_filter = st.text_input("Search Name")

    if st.button("Clear Filters"):
        st.experimental_rerun()

# Apply filters
filtered_df = df.copy()
if sport_filter:
    filtered_df = filtered_df[filtered_df["Sport"].isin(sport_filter)]
if name_filter:
    filtered_df = filtered_df[filtered_df.apply(lambda row: row.astype(str).str.contains(name_filter, case=False).any(), axis=1)]

st.subheader("📋 Tournament Entries")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown("✅ Created by **EC, NZKK**")
