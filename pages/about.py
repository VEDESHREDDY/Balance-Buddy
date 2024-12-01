import streamlit as st

def show():
    st.title("About Balance Buddy")
    st.write("This page gives detailed information about FitFusion.")
def display_about():
    about_text = """
Welcome to Balance Buddy, a platform created by three passionate individuals dedicated to helping you live a healthier and more balanced life. 
We aim to make fitness and wellness simple, fun, and accessible for everyone.

Our team combines expertise in technology, fitness, and nutrition to design a platform that supports your health journey. 
From personalized diet plans to workout routines, Balance Buddy provides tools and guidance tailored just for you.

At Balance Buddy, we believe that achieving balance in life shouldn’t feel overwhelming. 
Our mission is to use technology to inspire and motivate you to reach your wellness goals and build lasting healthy habits.

Join us on this journey, and let’s work together to achieve a balanced, healthier lifestyle. 💪✨
    """
    print(about_text)

if __name__ == "__main__":
    display_about()
