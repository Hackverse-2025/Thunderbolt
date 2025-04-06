import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API Key
genai.configure(api_key=os.getenv("api_key"))

def get_default_skills():
    """Returns a list of AI/ML-related skills."""
    return "Machine Learning, Deep Learning, Computer Vision, Natural Language Processing, Python, TensorFlow, PyTorch, Data Analysis"

def get_default_projects():
    """Returns a list of AI/ML-related projects."""
    return "AI-powered Fraud Detection, Image Super-Resolution using GANs, NLP-based Chatbot, Reinforcement Learning for Game AI, Anomaly Detection in IoT Data"

def generate_email_content(prompt, skills, projects):
    """Generates an email using Gemini API with provided prompt."""
    model = genai.GenerativeModel("gemini-1.5-pro")  # or "gemini-1.5-flash"
    
    response = model.generate_content(prompt)
    
    # Ensure skills and projects are explicitly included
    email_text = response.text
    if "Skills:" not in email_text or "Projects:" not in email_text:
        email_text += f"\n\nAdditionally, my skills in {skills} and experience with {projects} align perfectly with this research."

    return email_text

def formal_professional_email(title, abstract, researcher):
    """Generates a formal and professional internship request email."""
    skills = get_default_skills()
    projects = get_default_projects()
    
    prompt = f"""
    Generate a **formal and professional** internship request email for Dr. {researcher}.

    **Details:**
    - **Title of the Paper:** {title}
    - **Abstract:** {abstract}
    - **Skills:** {skills}
    - **Projects:** {projects}

    **Email Structure:**
    - **Subject Line:** Request for Internship Opportunity in [Research Area]
    - **Greeting:** Address Dr. {researcher} formally.
    - **Introduction:** Express strong interest in their research and connect it to the provided paper.
    - **Technical Fit:** Clearly highlight the candidate’s **skills** ({skills}) and explain how they are **relevant** to the research.
    - **Experience:** Emphasize past **projects** ({projects}) and how they demonstrate expertise in this field.
    - **Closing:** Politely request an internship opportunity and express willingness to contribute.

    **Ensure that the email is concise, respectful, and professional.**
    """
    return generate_email_content(prompt, skills, projects)

def enthusiastic_email(title, abstract, researcher):
    """Generates an enthusiastic and engaging internship request email."""
    skills = get_default_skills()
    projects = get_default_projects()
    
    prompt = f"""
    Generate an **enthusiastic and engaging** internship request email for Dr. {researcher}.

    **Details:**
    - **Title of the Paper:** {title}
    - **Abstract:** {abstract}
    - **Skills:** {skills}
    - **Projects:** {projects}

    **Email Structure:**
    - **Subject Line:** Excited to Explore Internship Opportunities in [Research Area]
    - **Greeting:** Address Dr. {researcher} warmly.
    - **Introduction:** Express excitement about their research and its impact.
    - **Technical Fit:** Clearly highlight the candidate’s **skills** ({skills}) and enthusiasm for applying them.
    - **Experience:** Showcase past **projects** ({projects}) and how they align with the research.
    - **Closing:** Politely request an internship opportunity and express eagerness to contribute.

    **Ensure that the tone is energetic, professional, and shows passion for the research.**
    """
    return generate_email_content(prompt, skills, projects)

def technical_email(title, abstract, researcher):
    """Generates a technically detailed and research-focused internship request email."""
    skills = get_default_skills()
    projects = get_default_projects()
    
    prompt = f"""
    Generate a **detailed and technically accurate** internship request email for Dr. {researcher}.

    **Details:**
    - **Title of the Paper:** {title}
    - **Abstract:** {abstract}
    - **Skills:** {skills}
    - **Projects:** {projects}

    **Email Structure:**
    - **Subject Line:** Technical Inquiry Regarding Internship in [Research Area]
    - **Greeting:** Address Dr. {researcher} formally.
    - **Introduction:** Express interest in their research and technical aspects of the paper.
    - **Technical Fit:** Provide a clear explanation of **how the candidate’s skills ({skills}) align technically** with the research.
    - **Experience:** Discuss past **projects ({projects}) in detail**, showcasing technical depth.
    - **Closing:** Politely request an internship and mention a willingness to engage in research discussions.

    **Ensure the tone is research-focused, professional, and technically sound.**
    """
    return generate_email_content(prompt, skills, projects)

# Run an example test
if __name__ == "__main__":
    title = "Deep Learning for Image Recognition"
    abstract = "This paper explores the use of convolutional neural networks for image classification tasks."
    researcher = "Dr. John Doe"

    # Generate emails
    print("---- Formal Email ----")
    print(formal_professional_email(title, abstract, researcher))
    
    print("\n---- Enthusiastic Email ----")
    print(enthusiastic_email(title, abstract, researcher))
    
    print("\n---- Technical Email ----")
    print(technical_email(title, abstract, researcher))
