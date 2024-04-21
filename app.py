from flask import Flask, render_template, request
import pandas as pd
from pickle import load
from Test import  generate_chart
app = Flask(__name__)

#load the questions from the CSV file
questions_df = pd.read_csv('questions.csv')

@app.route('/')
def index():
    return render_template('index.html', questions=questions_df.to_dict(orient='records'))

@app.route('/submit', methods=['POST'])
def submit():
    user_responses = {}
    for key, value in request.form.items():
        user_responses[key] = value

    # Write user responses to dataframe
    user_responses_df = pd.DataFrame(user_responses, index=[0])
    user_responses_df = user_responses_df.astype(int)
     
    ## Generate the chart, get the personality type and the personality traits value(my_sums)
    personality_type,my_sums=generate_chart(user_responses_df)

    # Render the results.html template and pass the personality type and the personality traits value
    return render_template('results.html',personality_type=personality_type,
                           labels=list(my_sums.columns[0:5]),data=list(my_sums.values[0][0:5]))

if __name__ == '__main__':
    app.run(debug=True)
