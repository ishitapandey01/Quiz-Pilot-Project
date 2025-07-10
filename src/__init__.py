# src/views.py or src/__init__.py
import nltk

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

from flask import Flask

app = Flask(__name__)
app.secret_key = "iSh1ta_S3cr3t_2025"
import src.views
