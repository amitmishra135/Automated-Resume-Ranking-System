from flask import Flask, request, jsonify, render_template
from data_processing import process_resume
import joblib
import os

app = Flask(__name__)

model = joblib.load('resume_ranking_model.joblib')

# Ensure a directory exists for temporarily storing uploaded files
UPLOAD_FOLDER = 'temp_uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rank_resume', methods=['POST'])
def rank_resume():
    job_description = request.form['job_description']
    
    # Check if the post request has the file part
    if 'resume' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['resume']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and file.filename.lower().endswith('.pdf'):
        # Save the file temporarily
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        try:
            # Process the resume
            similarity = process_resume(job_description, file_path)
            
            # Use the model to predict the ranking
            ranking = model.predict([[similarity]])[0]
            
            result = {
                'similarity_score': similarity,
                'ranking': int(ranking)
            }
        finally:
            # Clean up: remove the temporary file
            os.remove(file_path)
        
        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid file type. Please upload a PDF.'})

if __name__ == '__main__':
    app.run(debug=True)