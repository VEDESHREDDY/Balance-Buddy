from transformers import pipeline

# Example Meal Generator
def generate_meal_plan(dietary_preference, calorie_goal):
    # Simulated response
    return [
        f"Breakfast: Avocado toast with {calorie_goal * 0.2} kcal",
        f"Lunch: Grilled chicken salad with {calorie_goal * 0.4} kcal",
        f"Dinner: Quinoa with vegetables and {calorie_goal * 0.4} kcal"
    ]

# Example Fitness Recommendations
def recommend_workout(fitness_level):
    recommendations = {
        "Beginner": "Start with 20 minutes of walking daily.",
        "Intermediate": "Add strength training 3x per week.",
        "Advanced": "Incorporate high-intensity interval training (HIIT)."
    }
    return recommendations.get(fitness_level, "Custom advice coming soon.")
