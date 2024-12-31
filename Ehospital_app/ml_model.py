# recommendations/ml_model.py

import joblib
import os
from collections import Counter
from .models import Doctor

# Define the path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'doctor_recommendation_model.pkl')

# Load the trained model
model = joblib.load(model_path)

def recommend_doctor(symptoms):
    symptoms_str = ' '.join(symptoms)
    specializations = model.predict(symptoms)  # Here we pass the list of symptoms directly
    # Count the occurrences of each specialization
    specialization_counts = Counter(specializations)
    
    # Get the top five specializations based on occurrence
    top_specializations = [department for department, _ in specialization_counts.most_common(5)]
    print(f"Predicted specializations: {top_specializations}")  # Debugging line
    
    return top_specializations
