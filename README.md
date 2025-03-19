# 📄 **ResearchReach: A Researc Email writer**  

This project is a web-based tool that matches research papers to a candidate’s resume by utilizing Sentence-BERT (SBERT) and cosine similarity. The tool analyzes the candidate's skills, experience, and projects, then identifies the most relevant research papers based on the alignment between the resume and research paper content. By leveraging advanced natural language processing techniques, it enhances the process of finding research papers that best match a candidate’s qualifications, making the search more efficient and accurate.
---  

## 🚀 **Introduction**  
Finding relevant research papers based on a resume is a challenging task. This tool automates the process by:  
✅ Extracting skills and projects from the resume  
✅ Converting both the resume and research papers into vector embeddings  
✅ Computing similarity scores using cosine similarity  
✅ Returning the most relevant paper based on the highest similarity score  

---

## 🔍 **How It Works**  
The matching process follows a **4-step pipeline**:  

### 1️⃣ **Resume Data Extraction**  
- The system extracts key details from the candidate's resume, including:  
   - ✅ **Skills** (e.g., Machine Learning, NLP)  
   - ✅ **Projects** (e.g., Fake News Detection using BERT)  

✅ Example:  
```python
Skills = ["Machine Learning", "Natural Language Processing", "Deep Learning", "Python"]  
Projects = ["Fake News Detection using BERT", "Text Summarization with LSTM"]  
```
This information is concatenated into a single text input:
```python
"Machine Learning Natural Language Processing Deep Learning Python Fake News Detection using BERT Text Summarization with LSTM" 
```

# 🔍 **Research Paper Matching System**

## 🛠️ **Tech Stack**
| Component              | Tool                                      |
|----------------------- |------------------------------------------|
| **Frontend**            | React.js                                  |
| **Backend**             | Flask                                     |
| **Embedding Model**     | Sentence-BERT (all-MiniLM-L6-v2)         |
| **Paper Retrieval**     | Semantic Scholar API                      |
| **Similarity Calculation** | Cosine Similarity (Scikit-learn)         |
| **Email Generation**     | Gemini API                                |
| **Paper Download**       | Unpaywall API                             |

---

## 🏆 **Features**
✅ Fast and Efficient: Handles large datasets quickly using SBERT.  
✅ Accurate Matching: High similarity scoring using cosine similarity.  
✅ Automated Paper Retrieval: Uses Semantic Scholar to find relevant papers.  
✅ Secure Data Handling: Ensures data privacy and integrity.  
✅ Email Automation: Automatically generates internship request emails based on the matching paper.  

---

## 🚀 **Process Overview**
1. **Resume Parsing and Skill Extraction**  
2. **Research Paper Retrieval**  
3. **Convert to Sentence Embeddings**  
4. **Compute Cosine Similarity**  
5. **Generate and Send Email**  

<div style="display: flex; justify-content: center; gap: 20px;">  
<img src="step1.png" alt="Step 1" width="200"/>  
<img src="step2.png" alt="Step 2" width="200"/>  
<img src="step3.png" alt="Step 3" width="200"/>  
<img src="step4.png" alt="Step 4" width="200"/>  
</div>  

---

## 📝 **1️⃣ Resume Parsing and Skill Extraction**
The system extracts skills and projects from the resume using `pdfplumber`, `spaCy`, and `KeyBERT`.

**Example Skills:**  
`Machine Learning, Natural Language Processing, Deep Learning, Python, Fake News Detection using BERT, Text Summarization with LSTM`

---

## 📜 **2️⃣ Research Paper Retrieval**
The system retrieves research papers using the **Semantic Scholar API**.

**Example papers:**  

**📜 Paper 1:**  
**Title:** "A Deep Learning Approach to Fake News Detection"  
**Abstract:** "We propose a model based on BERT for detecting fake news articles. Our approach achieves state-of-the-art performance in text classification tasks."  

**📜 Paper 2:**  
**Title:** "Efficient Image Classification with CNNs"  
**Abstract:** "We present an optimized CNN model for image classification. The model reduces computational cost while maintaining accuracy."  

---

## 🔎 **3️⃣ Convert to Sentence Embeddings**
The system converts text into high-dimensional vector embeddings using **Sentence-BERT** (`all-MiniLM-L6-v2`):

```python
from sentence_transformers import SentenceTransformer  

embed_model = SentenceTransformer('all-MiniLM-L6-v2')  
resume_embedding = embed_model.encode(resume_text)  
paper_1_embedding = embed_model.encode(paper_1_text)  
paper_2_embedding = embed_model.encode(paper_2_text)  
```
## ✅ Example vector embeddings:
```css
Resume Embedding → [0.12, -0.08, ..., 0.32]  
Paper 1 Embedding → [0.11, -0.07, ..., 0.30]  
Paper 2 Embedding → [0.02, 0.45, ..., -0.12]  
```
---
## 📈 4️⃣ Compute Cosine Similarity  
Cosine similarity measures how similar two vectors are:

\[
\text{Cosine Similarity} = \frac{A \cdot B}{||A|| \cdot ||B||}
\]

---

✅ **Example calculation:**  
```python
from sklearn.metrics.pairwise import cosine_similarity  

similarity_1 = cosine_similarity([resume_embedding], [paper_1_embedding])  
similarity_2 = cosine_similarity([resume_embedding], [paper_2_embedding])  
```

| **Pair**               | **Similarity Score** | **Result**              |
|-----------------------|----------------------|-------------------------|
| **Resume & Paper 1**  | **0.92**              | ✅ High Similarity       |
| **Resume & Paper 2**  | **0.34**              | ❌ Low Similarity        |

---

## 💡 5️⃣ Final Output  
The paper with the highest similarity score is selected as the most relevant match.

✅ **Most Relevant Paper Found!**  
**Title:** *"A Deep Learning Approach to Fake News Detection"*  
**Abstract:** *"We propose a model based on BERT for detecting fake news articles. Our approach achieves state-of-the-art performance in text classification tasks."*  
**Similarity Score:** **0.92**  

---

## ✉️ 6️⃣ Email Generation  
Once a matching paper is found, the system generates an internship request email using the **Gemini API**.

### **Template Options:**  
✅ Formal & Professional  
✅ Technical & Research-Oriented  
✅ Enthusiastic & Passionate  

---
## 🤝 **Contributors**  
We would like to extend our heartfelt gratitude to everyone who contributed to this project. Your hard work and dedication made this possible!  

<table>
  <tr>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/125748305?v=4" width="80" height="80" alt="Your Name">
      <br>
      <a href="https://github.com/Srujanrana07"><b>Srujan Rana</b></a>
      <br>
      🏆 Project Lead, Backend Developer
    </td>
    <td align="center">
      <img src="https://avatars.githubusercontent.com/u/119315259?v=4" width="80" height="80" alt="Contributor 1">
      <br>
      <a href="https://github.com/contributor1"><b>Contributor 1</b></a>
      <br>
      💻 Frontend Developer  
      🌐 API Integration
    </td>
  </tr>
</table>

🌟 **Want to contribute?**  
We welcome contributions from the community! If you'd like to improve the project or report issues, feel free to fork the repo and submit a pull request.  

