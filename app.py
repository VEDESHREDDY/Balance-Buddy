import streamlit as st

st.set_page_config(
    page_title="FitFusion - AI for Fitness and Nutrition",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Homepage", "Sign-Up", "Dashboard", "Meal Planner", "Fitness Tracker", "Progress", "About Us"]
selected_page = st.sidebar.radio("Go to", pages)

# Route to different pages
if selected_page == "Homepage":
    import pages.homepage as homepage
    homepage.show()
elif selected_page == "Sign-Up":
    import pages.signup as signup
    signup.show()
elif selected_page == "Dashboard":
    import pages.dashboard as dashboard
    dashboard.show()
elif selected_page == "Meal Planner":
    import pages.meal_plan as meal_plan
    meal_plan.show()
elif selected_page == "Fitness Tracker":
    import pages.fitness_tracker as fitness_tracker
    fitness_tracker.show()
elif selected_page == "Progress":
    import pages.progress as progress
    progress.show()
elif selected_page == "About Us":
    import pages.about as about
    about.show()
