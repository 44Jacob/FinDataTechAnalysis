import os
import sqlite3
import sqlalchemy
import numpy as np
import pandas as pd
from config import api_key
from textblob import TextBlob
from sqlalchemy.orm import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from flask import Flask, render_template, jsonify
from api_func import get_avg_sentiment_scores, read_data, load_data_to_db, fetch_news, fetch_all_stock_data

app = Flask(__name__)

# get_avg_sentiment_scores()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/api/v1.0/load_data/<tickers>/<start>/<end>')
def load_data(tickers,start='2020-01-01',end='2024-01-01'):
    print(tickers,start,end)
    print('')
    fetch_all_stock_data(eval(tickers),start,end)
    return '<h1>Data has been loaded to the Database</h1>'

@app.route('/api/v1.0/stock_sentiment_score')
def get_sentiment():
    engine = create_engine('sqlite:///stock_market_analysis.sqlite')
    session = Session(engine)

    df1 = pd.DataFrame(session.execute(text('SELECT * FROM Average_Sentiment_Score')).all())

    return df1.to_json(orient='columns')

@app.route('/api/v1.0/stock_history')
def get_data():
    engine = create_engine('sq