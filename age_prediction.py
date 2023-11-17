from datetime import datetime

# Function to predict age based on birth year
def predict_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Input: Your birth year
birth_year = int(input("Enter your birth year: "))

# Predict and display age
predicted_age = predict_age(birth_year)
print(f"Based on your input, your predicted age is approximately: {predicted_age} years old.")
