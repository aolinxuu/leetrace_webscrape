from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, template_folder='.')
df = pd.read_csv('clean_res.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    topics = df['Topic'].unique()
    companies = df['Company'].unique()
    selected_topics = request.form.getlist('topic')
    selected_companies = request.form.getlist('company')
    filtered_data = df

    if selected_topics:
        filtered_data = filtered_data[filtered_data['Topic'].isin(selected_topics)]
    if selected_companies:
        filtered_data = filtered_data[filtered_data['Company'].isin(selected_companies)]

    return render_template('index.html', topics=topics, companies=companies, problems=filtered_data.to_html())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

