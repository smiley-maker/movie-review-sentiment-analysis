# Classifying Movie Review Sentiment with Naive Bayes

In this repository, I created and trained a Multinomial Naive Bayes model, which predicts the probability of an independent category given a set of features (in this case the TfidfVectorizer output of the original review). The trained model is pickled and used in a Streamlit application that accepts a new movie review and returns a sentiment prediction with a confidence. 

## Prerequisites

Docker must be installed and running on your system for the following steps to work. You should also clone the repository using the following command. 

```[bash]
git clone git@github.com:smiley-maker/movie-review-sentiment-analysis.git && cd movie-review-sentiment-analysis
```

Or if you'd rather use HTTP over SSH to clone the repo: 

```[bash]
git clone https://github.com/smiley-maker/movie-review-sentiment-analysis.git && cd movie-review-sentiment-analysis
```

## How To Run

This project is set up to run smoothly with Docker and a Makefile, which ensures dependencies and environment settings are already handled. To run the code, follow these steps while inside the repository root. 

1. Build the Docker image: 
```[bash]
make build
```

2. Run the Streamlit application from within the Docker container
```[bash]
make run
```

3. To view the app, navigate to http://localhost:8501/. 

4. If you want to remove the Docker container, run:
```[bash]
make clean
```