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

Create and activate a Conda environment:
conda create -n sentiment-analysis python=3.8
conda activate sentiment-analysis

Install the required packages:
pip install -r requirements.txt

Usage
Run the Flask application:
python app.py

Upload a CSV file:
Navigate to http://127.0.0.1:5000/upload in your web browser.
Upload a CSV file containing text data and star ratings.
View the results:
The application will process the uploaded file and display the shape of the DataFrame.
It will also identify and print indices of comments with low ratings but positive sentiments.
Endpoints
/upload: Upload a CSV file and process it.
/indices: Upload a CSV file and get indices of unmatched comments and low ratings.
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Flask
Pandas
NLTK
Contact
For any questions or suggestions, feel free to reach out to yourname@example.com.
