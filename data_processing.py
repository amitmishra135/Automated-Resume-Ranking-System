import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

def preprocess_text(text):
    # Convert to lowercase and remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    return text

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_features(job_description, resume_text):
    # Preprocess texts
    job_description = preprocess_text(job_description)
    resume_text = preprocess_text(resume_text)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the job description and resume
    tfidf_matrix = vectorizer.fit_transform([job_description, resume_text])

    return tfidf_matrix

def calculate_similarity(tfidf_matrix):
    # Calculate cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity

def process_resume(job_description, resume_file):
    resume_text = extract_text_from_pdf(resume_file)
    tfidf_matrix = extract_features(job_description, resume_text)
    similarity = calculate_similarity(tfidf_matrix)
    return similarity