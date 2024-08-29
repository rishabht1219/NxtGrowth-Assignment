# Flask Sentiment Analysis App

This Flask application processes uploaded CSV files to analyze text data and identify conflicts between text sentiments and star ratings.

## Table of Contents
- Installation
- Usage
- Endpoints
- Contributing
- License

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask-sentiment-analysis.git
   cd flask-sentiment-analysis

2. **Create and activate a Conda environment:**
   ```bash
   conda create -n sentiment-analysis python=3.8
   conda activate sentiment-analysis

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

## Usage:
1. Run the Flask application:
   ```bash
   python app.py

2. **Upload a CSV file:**
   Navigate to http://127.0.0.1:5000/upload in your web browser.
   Upload a CSV file containing text data and star ratings.
3. **View the results:**
   The application will process the uploaded file and display the shape of the data frame.
   It will also identify and print indices of comments with low ratings but positive sentiments.
4. **Endpoints:**
   /upload: Upload a CSV file and process it.
   /indices: Upload a CSV file and get indices of unmatched comments and low ratings.


## Acknowledgements
* Flask
* Pandas
* NLTK
## Contact:
   If you have any questions or suggestions, feel free to reach out to rishabht1219@gmail.com.
