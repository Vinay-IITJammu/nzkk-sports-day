import streamlit as st
import pandas as pd
import json
from PIL import Image

# Load logo and event details
logo = Image.open("logo.jpg")
with open("event_metadata.json", "r") as f:
    event_info = json.load(f)

# Load data
df = pd.read_csv("nzkk_sports_entries.csv")

# Sidebar
st.sidebar.image(logo, width=120)
st.sidebar.markdown(f"### 📍 {event_info['Event Address']}")
st.sidebar.markdown(f"### 🕗 {event_info['Event Timing']}")

# Title
st.title(event_info["Event Name"])

# Filters
sports = st.multiselect("Select Sport(s):", options=sorted(df["Sport"].unique()), default=sorted(df["Sport"].unique()))
categories = st.multiselect("Select Category:", options=sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
search_name = st.text_input("Search by Name (partial allowed):")

# Filter logic
filtered_df = df[df["Sport"].isin(sports) & df["Category"].isin(categories)]
if search_name:
    filtered_df = filtered_df[filtered_df["Name"].str.contains(search_name, case=False, na=False)]

# Display
st.dataframe(filtered_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Created by EC, NZKK**")
