
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def calculate_match(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return round(similarity * 100, 2)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    job_description = request.form["job_description"]

    if resume.filename == "":
        return "Please upload a resume."

    file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(file_path)

    resume_text = extract_text(file_path)

    match_score = calculate_match(
        resume_text,
        job_description
    )

    return render_template(
        "result.html",
        score=match_score,
        resume_text=resume_text[:3000]
    )


if __name__ == "__main__":
    app.run(debug=True)
