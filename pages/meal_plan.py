import streamlit as st
from streamlit_extras.colored_header import colored_header

# Mock Meal Plan Data with Nutritional Details
def get_meal_plan():
    return {
        "Monday": [
            {"meal": "Breakfast: Oatmeal and Fruits", "calories": 250, "carbs": 40, "fat": 5, "protein": 6},
            {"meal": "Lunch: Grilled Chicken Salad", "calories": 350, "carbs": 15, "fat": 10, "protein": 40},
            {"meal": "Dinner: Salmon with Veggies", "calories": 400, "carbs": 20, "fat": 25, "protein": 35},
        ],
        "Tuesday": [
            {"meal": "Breakfast: Smoothie Bowl", "calories": 300, "carbs": 50, "fat": 5, "protein": 10},
            {"meal": "Lunch: Turkey Wrap", "calories": 400, "carbs": 40, "fat": 12, "protein": 30},
            {"meal": "Dinner: Stir-fried Tofu", "calories": 350, "carbs": 25, "fat": 15, "protein": 20},
        ],
        "Wednesday": [
            {"meal": "Breakfast: Yogurt and Granola", "calories": 200, "carbs": 30, "fat": 5, "protein": 8},
            {"meal": "Lunch: Veggie Pasta", "calories": 450, "carbs": 60, "fat": 10, "protein": 15},
            {"meal": "Dinner: Grilled Chicken and Quinoa", "calories": 400, "carbs": 30, "fat": 10, "protein": 40},
        ],
        "Thursday": [
            {"meal": "Breakfast: Avocado Toast", "calories": 280, "carbs": 35, "fat": 12, "protein": 8},
            {"meal": "Lunch: Lentil Soup", "calories": 320, "carbs": 40, "fat": 5, "protein": 20},
            {"meal": "Dinner: Baked Fish with Brown Rice", "calories": 380, "carbs": 30, "fat": 8, "protein": 35},
        ],
        "Friday": [
            {"meal": "Breakfast: Pancakes with Berries", "calories": 300, "carbs": 50, "fat": 5, "protein": 10},
            {"meal": "Lunch: Beef Stir-fry", "calories": 450, "carbs": 30, "fat": 15, "protein": 35},
            {"meal": "Dinner: Veggie Burger", "calories": 400, "carbs": 40, "fat": 15, "protein": 20},
        ],
        "Saturday": [
            {"meal": "Breakfast: Scrambled Eggs with Spinach", "calories": 250, "carbs": 10, "fat": 15, "protein": 20},
            {"meal": "Lunch: Chicken Wrap", "calories": 400, "carbs": 40, "fat": 12, "protein": 35},
            {"meal": "Dinner: Shrimp Stir-fry", "calories": 350, "carbs": 30, "fat": 10, "protein": 30},
        ],
        "Sunday": [
            {"meal": "Breakfast: French Toast", "calories": 300, "carbs": 45, "fat": 8, "protein": 10},
            {"meal": "Lunch: Quinoa Salad", "calories": 350, "carbs": 40, "fat": 10, "protein": 15},
            {"meal": "Dinner: Roast Chicken with Vegetables", "calories": 450, "carbs": 25, "fat": 15, "protein": 40},
        ],
    }

def show():
    # Header Section
    st.title("🌿 Balance Buddy Meal Planner")
    st.markdown(
        "Plan your meals with **HealthOptima** and achieve your health goals. Here's a personalized meal plan for you!"
    )
    
    # Weekly Meal Plan Section
    colored_header(label="Your Weekly Meal Plan", description="Select a day to view meals and their nutritional details.", color_name="green-70")

    meal_plan = get_meal_plan()
    day = st.selectbox("📅 Select a Day", list(meal_plan.keys()), index=0)

    st.markdown(f"### 🍽️ **Meals for {day}**")
    for meal in meal_plan[day]:
        st.markdown(
            f"""
            #### {meal['meal']}
            - **Calories**: {meal['calories']} kcal  
            - **Carbs**: {meal['carbs']} g  
            - **Fat**: {meal['fat']} g  
            - **Protein**: {meal['protein']} g  
            """
        )
        st.divider()

    # Customize Meal Plan Section
    st.markdown("### ✨ Customize Your Meal Plan")
    st.info("Add a custom meal with its nutritional details to tailor your plan.")

    with st.form(key="meal_plan_form"):
        custom_meal = st.text_area("🍴 Enter Meal Name")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            custom_calories = st.number_input("Calories (kcal)", min_value=0, step=1)
        with col2:
            custom_carbs = st.number_input("Carbs (g)", min_value=0, step=1)
        with col3:
            custom_fat = st.number_input("Fat (g)", min_value=0, step=1)
        with col4:
            custom_protein = st.number_input("Protein (g)", min_value=0, step=1)

        add = st.form_submit_button("Add Meal ➕")
        if add:
            st.success(f"**{custom_meal}** added to your meal plan! (Database not implemented)")

    # Footer Section
    st.markdown("---")
    st.markdown(
        "💡 *Tip: Stay consistent with your meals and track your progress for better results.*"
    )

# Run the application
if __name__ == "__main__":
    show()
