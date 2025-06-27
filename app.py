import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Display logo and title
st.image("logo.jpg", width=120)
st.title("New Zealand Kannada Koota Sports Day - 2025")

# Sidebar filters
with st.sidebar:
    st.header("🎯 Filter Participants")
    event_filter = st.multiselect("Select Event", df["Event"].unique())
    gender_filter = st.multiselect("Select Gender", df["Gender"].unique())
    category_filter = st.multiselect("Select Category", df["Category"].unique())
    payment_status = st.multiselect("Payment Status", df["Payment Status"].unique())

    if st.button("Clear Filters"):
        st.experimental_rerun()

# Apply filters
filtered_df = df.copy()
if event_filter:
    filtered_df = filtered_df[filtered_df["Event"].isin(event_filter)]
if gender_filter:
    filtered_df = filtered_df[filtered_df["Gender"].isin(gender_filter)]
if category_filter:
    filtered_df = filtered_df[filtered_df["Category"].isin(category_filter)]
if payment_status:
    filtered_df = filtered_df[filtered_df["Payment Status"].isin(payment_status)]

st.subheader("📋 Filtered Participants")
st.dataframe(filtered_df)

st.markdown("---")
st.markdown("Created by **Group 2, PGDCS-2, IIT Jammu**")
