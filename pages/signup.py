import streamlit as st

def show():
    st.title("Balance Buddy")

    # Tabs for Sign Up and Sign In
    tab1, tab2 = st.tabs(["Sign Up", "Sign In"])

    # Sign-Up Tab
    with tab1:
        st.header("Sign Up to become our buddy")
        with st.form(key="signup_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            health_goals = st.text_area("Health Goals")
            dietary_preferences = st.text_input("Dietary Preferences")
            fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
            medical_conditions = st.text_input("Medical Conditions")

            # Submit Button
            signup_submit = st.form_submit_button("Sign Up")
            if signup_submit:
                st.success("Thanks for signing up! Check your email for the next steps.")

    # Sign-In Tab
    with tab2:
        st.header("Sign In to FitFusion")
        with st.form(key="signin_form"):
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")

            # Submit Button
            signin_submit = st.form_submit_button("Sign In")
            if signin_submit:
                # Placeholder for authentication logic
                st.success("Welcome back to Balance Buddy!")
