# recommendations/train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

# Define the path to the data file
data_path = os.path.join(os.path.dirname(__file__), 'data.csv')

# Load the data
data = pd.read_csv(data_path)

# Create a TF-IDF vectorizer and logistic regression pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(max_iter=200))
])

# Train the model
X = data['symptoms']
y = data['department']
pipeline.fit(X, y)

# Save the trained model
model_path = os.path.join(os.path.dirname(__file__), 'doctor_recommendation_model.pkl')
joblib.dump(pipeline, model_path)



