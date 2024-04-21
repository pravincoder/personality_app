from flask import Flask, render_template, request
import pandas as pd
from pickle import load
from Test import predict_personality, generate_chart
import plotly.express as px
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

    # Write user responses to CSV file
    user_responses_df = pd.DataFrame([user_responses])
   
    # Get prediction from the perdict_personality function
    personality_type = predict_personality(user_responses_df)
    
    ## Results Options
    results ={
        '[1]':'extroversion',
        '[2]':'neurotic',
        '[3]':'agreeable',
        '[4]':'conscientious',
        '[5]':'open',
    }
    personality_type = results[str(personality_type)]
    

    ## Generate the bar chart
    generate_chart(predict_personality(data = user_responses_df),user_responses_df)

    return render_template('results.html', personality_type=personality_type)

if __name__ == '__main__':
    app.run(debug=True)
