from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import uuid
from paper_retrieval import get_research_papers
from resume_processor import process_resume
from similarity import compute_highest_similarity

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/upload-resume/', methods=['POST'])
def upload_resume():
    """Handles resume uploads and extracts skills & projects."""
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    extracted_data = process_resume(file_path)

    return jsonify({
        "success": True,
        "fileName": file.filename,
        "resumeId": filename,
        "filePath": file_path,
        "extractedData": extracted_data
    })

@app.route('/api/search-researcher/', methods=['POST'])
def search_researcher():
    """Fetches real research papers using Semantic Scholar API."""
    data = request.json
    researcher_name = data.get('researcher', '').strip()

    if not researcher_name:
        return jsonify({"error": "Researcher name is required"}), 400

    print(f"Searching for researcher: {researcher_name}")  # Debug

    papers, researcher_details = get_research_papers(researcher_name)
    
    print(f"Fetched researcher: {researcher_details['researcher']}")  # Debug
    print(f"Fetched papers: {papers}")  # Debug

    matched_papers = []
    if papers:
        matched_papers = [{"title": paper["title"], "abstract": paper["abstract"]} for paper in papers]

    if not papers:
        return jsonify({"error": "No research papers found"}), 404

    return jsonify({
        "researcher": researcher_details["researcher"],
        "papers": papers
    })

@app.route('/api/match-resume/', methods=['POST'])
def match_resume():
    """Matches a resume against research papers using NLP similarity scoring."""
    data = request.json
    resume_id = data.get('resumeId')
    researcher_name = data.get('researcher')

    if not resume_id or not researcher_name:
        return jsonify({"error": "Resume ID and Researcher name are required"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, resume_id)

    if not os.path.exists(file_path):
        return jsonify({"error": "Resume file not found"}), 404

    extracted_data = process_resume(file_path)
    papers, _ = get_research_papers(researcher_name)

    if not papers:
        return jsonify({"error": "No research papers found"}), 404

    highest_similarity = compute_highest_similarity(extracted_data, papers)
    print(f"💡 Highest Similarity Result: {highest_similarity}")  # Debug

    if not highest_similarity:
        return jsonify({"error": "No significant match found"}), 404

    title, abstract, score = highest_similarity

    return jsonify({
        "filePath": file_path,
        "matchedPaper": {
            "title": title,
            "abstract": abstract,
            "similarityScore": round(score, 4)
        }
    })

@app.route('/api/get-email-templates/', methods=['POST'])
def get_email_templates():
    """Returns email templates based on matched research paper."""
    data = request.json
    researcher = data.get('researcher', 'Unknown Researcher')

    email_templates = [
        {
            "type": "Formal & Professional",
            "content": f"Dear {researcher},\n\nI hope this email finds you well. I recently came across your research and was greatly impressed. I have a background in related fields and would love to discuss potential collaboration or internship opportunities.\n\nBest Regards,\n[Your Name]"
        },
        {
            "type": "Enthusiastic & Passionate",
            "content": f"Hello {researcher},\n\nI’m incredibly excited about your work! I’ve been following your research and would be thrilled to contribute and learn from you. My background aligns with your recent projects, and I’d love to explore ways I can assist or intern with you!\n\nLooking forward to hearing from you!\n\nBest,\n[Your Name]"
        },
        {
            "type": "Technical & Research-Oriented",
            "content": f"Dear Prof. {researcher},\n\nYour paper intrigued me due to my own research experience. I believe my prior expertise would be beneficial in extending your findings. I’d love to discuss this further and explore potential collaboration or internship opportunities.\n\nRegards,\n[Your Name]"
        }
    ]

    return jsonify(email_templates)

@app.route('/api/send-email/', methods=['POST'])
def send_email():
    """Mocks sending an email."""
    data = request.json
    researcher_name = data.get('researcher', 'Unknown Researcher')
    template_type = data.get('template', {}).get('type', 'Unknown')

    print(f"Mock email sent to {researcher_name}")
    print(f"Template used: {template_type}")

    return jsonify({
        "success": True,
        "message": f"Mock email successfully sent to {researcher_name}!"
    })

if __name__ == '__main__':
    app.run(port=8000, debug=True)
