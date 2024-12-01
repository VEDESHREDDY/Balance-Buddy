import streamlit as st

def show():
    # Title and Hero Section
    st.title("Welcome to Balance Buddy! 🌟")
    st.markdown("### Personalized Fitness and Nutrition, Powered by AI")
    st.image("assets/hero_slider.jpg", use_container_width=True, caption="Achieve Your Goals with Balance Buddy")
    
    # Call-to-Action (CTA) Buttons
    st.markdown("#### Get Started Today!")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Join FitFusion 🚀"):
            st.experimental_set_query_params(page="Sign-Up")
            st.success("Redirecting to Sign-Up Page...")
    with col2:
        if st.button("Explore Features 🔍"):
            st.experimental_set_query_params(page="About Us")
            st.success("Redirecting to About Us Page...")

    # Key Features Section
    st.markdown("### 🔑 Key Features")
    features = {
        "Meal Planning": {
            "description": "Personalized meal plans tailored to your goals.",
            "icon": "assets/icons/meal_planning.jpg",
        },
        "Fitness Tracking": {
            "description": "Real-time tracking with wearable devices.",
            "icon": "assets/icons/fitness_tracking.jpg",
        },
        "Health Insights": {
            "description": "AI-driven tips and alerts for a healthier lifestyle.",
            "icon": "assets/icons/health_insights.jpg",
        },
    }
    
    feature_cols = st.columns(len(features))
    for i, (feature, details) in enumerate(features.items()):
        with feature_cols[i]:
            st.image(details["icon"], width=100, caption=feature)
            st.markdown(f"**{feature}**")
            st.write(details["description"])

    
    # Footer Section
    st.markdown("---")
    st.markdown("### Stay Connected")
    st.markdown(
        """
        **Quick Links**  
        - [About FitFusion](#)  
        - [FAQs](#)  
        - [Contact Us](#)  
        - [Privacy Policy](#)
        """
    )
    st.markdown("Connect with us on Social Media:")
    st.image("assets/social_media_icons.jpg", width=1000)  # Social Media Icons Placeholder

# Run the application
if __name__ == "__main__":
    show()
