# Classifying Movie Review Sentiment with Naive Bayes

In this repository, I created and trained a Multinomial Naive Bayes model, which predicts the probability of an independent category given a set of features (in this case the TfidfVectorizer output of the original review). The trained model is pickled and used in a Streamlit application that accepts a new movie review and returns a sentiment prediction with a confidence. 

To setup and run the code: 

- Clone the repository:
```[bash]
git clone git@github.com:smiley-maker/movie-review-sentiment-analysis.git
```
- cd into the repository directory:
```[bash]
cd movie-review-sentiment-analysis
```
- (Optional) Create a virtual environment or conda environment to ensure no conflicts arise.
```[bash]
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# Conda environment (my personal favorite)
conda create --name moviesentiment python=3.9
conda activate moviesentiment
```
- Install the requirements: 
```[bash]
pip install -r requirements.txt
```
- If you want to rerun the training:
```[bash]
python train_model.py
```
- Run the streamlit application to test it out!
```[bash]
streamlit run app.py
```
