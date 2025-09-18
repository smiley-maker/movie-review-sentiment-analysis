import joblib
import streamlit as st

# --- Page Setup ---
title = "Movie Review Sentiment Analysis"
st.set_page_config(page_title=title)
st.title(title)
description = "Sentiment analysis of movie reviews using a Multinomal Naive Bayes classifier."
st.write(description)

# --- Load Model (Cached) ---
@st.cache_resource
def load_model():
    """Loads the sentiment analysis model from pickel file."""
    model = joblib.load("sentiment_model.pkl")
    return model

model = load_model()

# --- User Input ---
# Assigns the text_area's output to a variable.
input_text = st.text_area("Enter your movie review here:", height=150)

# --- Button and Prediction Logic ---
# Use the return value of st.button() to control when the prediction is made.
if st.button("Analyze Sentiment"):
    # If no review is entered, show a warning.
    if input_text.strip() == "":
        st.warning("Please enter a movie review to analyze.")
    else:
        # Perform prediction
        prediction = model.predict([input_text])[0]
        # Get prediction probability
        prediction_proba = model.predict_proba([input_text])[0]
        # prediction_proba is an array like [0.3, 0.7] for [negative, positive]
        # We take the max probability for confidence about the selected class
        confidence = max(prediction_proba) * 100
        
        # Display result
        st.subheader("Predicted Sentiment:")
        if prediction == 'positive':
            st.success(f"The sentiment of the review is **positive**.", icon="😀")
            st.balloons()
        else:
            st.error(f"The sentiment of the review is **negative**.", icon="😞")
            st.snow()
        st.write(f"With a confidence of **{confidence:.2f}%**.")

# --- Footer with link to Github ---
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.markdown("Developed by Jordan Sinclair")
with col2:
    st.link_button("GitHub Repository", "https://github.com/smiley-maker/movie-review-sentiment-analysis")