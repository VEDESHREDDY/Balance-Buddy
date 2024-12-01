import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to display the app
def show():
    st.title("Your Progress Tracker")

    # Input Data Section
    st.markdown("### Input Your Progress Data")
    with st.form("progress_form"):
        date = st.date_input("Date", value=pd.Timestamp.today())
        weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, step=0.1, value=75.0)
        calories_consumed = st.number_input("Calories Consumed", min_value=500, max_value=5000, step=10, value=2000)
        steps = st.number_input("Steps", min_value=0, max_value=50000, step=100, value=5000)
        submitted = st.form_submit_button("Add Data")

    # Session state to store progress data
    if "progress_data" not in st.session_state:
        st.session_state.progress_data = pd.DataFrame(columns=["Date", "Weight (kg)", "Calories Consumed", "Steps"])

    # Add the data to the DataFrame
    if submitted:
        new_data = {"Date": date, "Weight (kg)": weight, "Calories Consumed": calories_consumed, "Steps": steps}
        st.session_state.progress_data = pd.concat(
            [st.session_state.progress_data, pd.DataFrame([new_data])], ignore_index=True
        )
        st.success("Data added successfully!")

    # Display the current data
    if not st.session_state.progress_data.empty:
        st.markdown("### Current Progress Data")
        st.dataframe(st.session_state.progress_data)

        # Ensure 'Date' is in datetime format
        st.session_state.progress_data['Date'] = pd.to_datetime(st.session_state.progress_data['Date'])

        # Weight Progress Graph
        st.markdown("### Weight Progress")
        fig, ax = plt.subplots()
        ax.plot(
            st.session_state.progress_data["Date"],
            st.session_state.progress_data["Weight (kg)"],
            label="Weight (kg)",
            color="green",
        )
        ax.set_title("Weight Progress Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Weight (kg)")
        ax.legend()
        st.pyplot(fig)

        # Activity Progress (Calories and Steps)
        st.markdown("### Activity Progress")
        st.line_chart(st.session_state.progress_data[["Calories Consumed", "Steps"]])

        # Weekly Summary
        st.markdown("### Weekly Summary")
        weekly_summary = (
            st.session_state.progress_data.set_index("Date").resample("W").mean()
        )
        st.bar_chart(weekly_summary[["Weight (kg)", "Calories Consumed"]])
    else:
        st.info("No progress data available. Please add data above.")

# Run the Streamlit app
if __name__ == "__main__":
    show()
