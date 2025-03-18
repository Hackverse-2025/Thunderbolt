import os
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyCihQiZOBvVGHfPCOiTZPCdoxMpV4xsXE0")

def generate_email_content(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use "gemini-1.5-pro" or "gemini-1.5-flash"
    
    response = model.generate_content(prompt)
    
    return response.text


def formal_professional_email(title, abstract, skills, projects):
    prompt = f"""
    Generate a formal and professional internship request email for a researcher based on the following details:

    Title of the paper: {title}
    Abstract: {abstract}
    Skills: {skills}
    Projects: {projects}

    The email should express interest in the researcher's work, highlight relevant skills and projects, and politely request an internship opportunity. 
    Keep the tone professional and to the point.
    """
    return generate_email_content(prompt)


def enthusiastic_email(title, abstract, skills, projects):
    prompt = f"""
    Generate an enthusiastic and engaging internship request email for a researcher based on the following details:

    Title of the paper: {title}
    Abstract: {abstract}
    Skills: {skills}
    Projects: {projects}

    The email should express excitement about the researcher's work, highlight how the candidate's skills and projects align with the research, and request an internship opportunity.
    Keep the tone energetic and professional.
    """
    return generate_email_content(prompt)


def technical_email(title, abstract, skills, projects):
    prompt = f"""
    Generate a detailed and technically accurate internship request email for a researcher based on the following details:

    Title of the paper: {title}
    Abstract: {abstract}
    Skills: {skills}
    Projects: {projects}

    The email should focus on technical alignment with the research paper, highlight the candidate's relevant technical expertise, and request an internship opportunity.
    Keep the tone technical and research-focused.
    """
    return generate_email_content(prompt)


if __name__ == "__main__":
    # Example data
    title = "Deep Learning for Image Recognition"
    abstract = "This paper explores the use of convolutional neural networks for image classification tasks."
    skills = "Python, TensorFlow, Computer Vision"
    projects = "Image Classification using CNNs, Transfer Learning"

    print("=== Formal & Professional ===")
    print(formal_professional_email(title, abstract, skills, projects))
    print("\n=== Enthusiastic ===")
    print(enthusiastic_email(title, abstract, skills, projects))
    print("\n=== Technical ===")
    print(technical_email(title, abstract, skills, projects))