
from flask import Flask, request, render_template
from numpy import indices
import pandas as pd
from nltk import FreqDist


app = Flask(__name__,template_folder='template')

def test(data):
    column_list = data.columns.values.tolist()
    print(column_list)
    sliced_data = data[["Text","Star"]]
    ratings = [4, 5] 
    high_rating_data = sliced_data.loc[sliced_data['Star'].isin(ratings)] 
    list_of_Text = high_rating_data['Text'].to_list()
    listToStr = ' '.join([str(elem) for elem in list_of_Text])
    a=listToStr.lower()
    words = a.split()
    fdist1 = FreqDist(words)
    sort = sorted([fdist1.most_common()], 
        key=lambda x: x[1])

    sentiments = ['good','nice','best','great','love','excellent','super','awesome','fast','cool','thanks','better','easy','amazing','wow','helpful','perfect','happy','superb']
    ratings = [1, 2]  
    low_rating_data = sliced_data.loc[sliced_data['Star'].isin(ratings)] 
    low_rating_data = low_rating_data.reset_index()
    indices_conflict_ratings = []
    

    for index, row in low_rating_data.iterrows():
        text = row['Text']
        a = text.split()
        for sentiment in sentiments:
            if sentiment in a:
                indices_conflict_ratings.append(index) 
        
                
    print(indices_conflict_ratings)
    return str(indices_conflict_ratings)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        test(df)
        return render_template('upload.html', shape=df.shape)
    return render_template('upload.html')

@app.route('/indices', methods=['POST'] )
def indices():
    df = pd.read_csv(request.files.get('file'))
    return "Indices of the Unmatched comments & Low ratings as found in Uploaded CSV \n" + test(df)

if __name__ == '__main__':
    app.run(debug=True)