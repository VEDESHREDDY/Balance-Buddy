import streamlit as st

def show():
    st.title("Your Personalized Dashboard")
    
    col1, col2, col3 = st.columns(3)

    # Daily Overview
    with col1:
        st.header("Today's Goals")
        st.metric(label="Calories", value="1800 kcal", delta="-200 kcal")
        st.metric(label="Steps", value="8,000", delta="+2,000 steps")
    
    # Weekly Overview
    with col2:
        st.header("Weekly Progress")
        st.line_chart([1500, 1800, 1700, 1600, 2000])  # Example chart
    
    # Alerts and Tips
    with col3:
        st.header("Tips & Alerts")
        st.info("Hydrate more today! Aim for 2.5L of water.")
