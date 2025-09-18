import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
import joblib

if __name__ == "__main__":
    # Load dataset
    data = pd.read_csv("data/data.csv")
    print("First 5 rows of the dataset:")
    print(data.head())
    print(f"Dataset shape: {data.shape}")
    # Separate features and labels
    X = data["review"]
    y = data["sentiment"]
    print(f"Features shape: {X.shape}, Labels shape: {y.shape}")
    # Create a pipeline that first transforms the data using TfidfVectorizer and then applies MultinomialNB
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB()),
    ])
    # Train the model on the entire dataset
    model.fit(X, y)
    print("Model training completed.")
    print(f"Model accuracy on training data: {model.score(X, y)}")
    # Save the trained model to disk
    joblib.dump(model, "sentiment_model.pkl")
    print("Model saved to sentiment_model.pkl")