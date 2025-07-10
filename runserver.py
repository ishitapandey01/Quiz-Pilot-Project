
import nltk

# Download necessary NLTK data at runtime
required_nltk_packages = ["punkt", "averaged_perceptron_tagger"]
for package in required_nltk_packages:
    try:
        if package == "punkt":
            nltk.data.find("tokenizers/punkt")
        else:
            nltk.data.find(f"taggers/{package}")
    except LookupError:
        nltk.download(package)
        
import os
from src import app


if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 1234
    app.secret_key = "1cd6f35db029d4b8fc98fc05c9efd06a2e2cd1ffc3774d3f035ebd8d"
    app.run(HOST, PORT, debug=True)
