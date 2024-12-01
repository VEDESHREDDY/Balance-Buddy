import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Fitness Tracker Data
def get_fitness_data():
    return [
        {"date": "2024-11-29", "activity": "Running", "duration": "30 minutes", "calories_burned": 300},
        {"date": "2024-11-28", "activity": "Cycling", "duration": "45 minutes", "calories_burned": 400},
    ]

# Motivational Quotes
def get_motivational_quote():
    quotes = [
        "Success is the sum of small efforts, repeated day in and day out.",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
        "The only bad workout is the one that didn’t happen.",
        "Don’t limit your challenges, challenge your limits.",
    ]
    return np.random.choice(quotes)

def show():
    # Header Section
    st.title("🌿 Balance Buddy")
    st.markdown(
        "Track your fitness activities with **HealthOptima** to maintain a healthy lifestyle!"
    )
    
    # Motivational Quote Section
    st.markdown(f"### 💪 Motivation for Today:")
    st.markdown(f"**{get_motivational_quote()}**")
    st.divider()

    # Fitness Tracker Section
    st.markdown("## 🏋️‍♀️ Fitness Tracker")
    st.info("Log your daily fitness activities to track progress.")

    # Display logged activities
    fitness_data = get_fitness_data()
    if fitness_data:
        st.markdown("### Logged Activities")
        for record in fitness_data:
            st.markdown(
                f"""
                - **Date**: {record['date']}
                - **Activity**: {record['activity']}
                - **Duration**: {record['duration']}
                - **Calories Burned**: {record['calories_burned']} kcal
                """
            )
            st.divider()
    else:
        st.warning("No activities logged yet.")

    # Add a new activity form
    st.markdown("### ✏️ Log a New Activity")
    with st.form(key="fitness_tracker_form"):
        date = st.date_input("📅 Select Date")
        activity = st.text_input("🏃‍♂️ Activity Name (e.g., Running, Cycling)")
        duration = st.text_input("⏱️ Duration (e.g., 30 minutes)")
        calories_burned = st.number_input("🔥 Calories Burned (kcal)", min_value=0, step=1)

        add_activity = st.form_submit_button("Add Activity ➕")
        if add_activity:
            st.success(f"Activity **{activity}** on **{date}** logged successfully! (Database not implemented)")

    # Calories Burned Chart
    st.markdown("## 📊 Calories Tracker")
    st.markdown(
        "Visualize the calories burned from your logged activities!"
    )

    # Mock data for chart
    calories_burned = [record['calories_burned'] for record in fitness_data]
    dates = [record['date'] for record in fitness_data]

    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Calories Burned': calories_burned,
    })

    # Plot chart
    fig, ax = plt.subplots(figsize=(8, 5))
    df.set_index('Date')['Calories Burned'].plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title("Calories Burned Over Time")
    ax.set_ylabel("Calories (kcal)")
    ax.set_xlabel("Date")
    st.pyplot(fig)

    # Footer Section
    st.markdown("---")
    st.markdown(
        "💡 *Tip: Regularly track your fitness activities for the best results.*"
    )

# Run the application
if __name__ == "__main__":
    show()
