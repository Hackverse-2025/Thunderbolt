import React, { useState, useEffect } from "react";
import {
  Upload,
  Search,
  Mail,
  Edit3,
  Send,
  Loader2,
  ChevronRight,
} from "lucide-react";
import axios from "axios";
import "./temp.css";

function App() {
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [selectedTemplate, setSelectedTemplate] = useState(null);
  const [file, setFile] = useState(null);
  const [researcher, setResearcher] = useState("");
  const [researcherData, setResearcherData] = useState(null);
  const [emailTemplates, setEmailTemplates] = useState([]);
  const [apiConnected, setApiConnected] = useState(false);
  
  const [currentIndex, setCurrentIndex] = useState(0);
  
  useEffect(() => {
    const checkApiStatus = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/status/");
        if (response.status === 200) {
          setApiConnected(true);
        }
      } catch (error) {
        setApiConnected(false);
      }
    };

    checkApiStatus();
  }, []);

  const handleFileUpload = async (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    setLoading(true);
    setFile(selectedFile);

    const formData = new FormData();
    formData.append("resume", selectedFile);

    try {
      await axios.post("http://localhost:8000/api/upload-resume/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setStep(2);
    } catch (error) {
      console.error("Error uploading resume:", error);
    } finally {
      setLoading(false);
    }
  };


  const nextPaper = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex < researcherData.length - 1 ? prevIndex + 1 : prevIndex
    );
  };  

  const prevPaper = () => {
    setCurrentIndex((prevIndex) => (prevIndex > 0 ? prevIndex - 1 : prevIndex));
  };


  const handleResearcherSearch = async (e) => {
    e.preventDefault();
    if (!researcher.trim()) return;
    console.log("heheh", researcher);
    setLoading(true);
    try {
      const response = await axios.post(
        "http://localhost:8000/api/search-researcher/",
        {
          researcher: researcher,
        }
      );

      if (response.data.error) {
        alert(response.data.error);
        setResearcherData(null);
      } else {
        
        setResearcherData(response.data.papers); // Store first matching researcher
        setStep(3);
      }
    } catch (error) {
      console.error("Error searching researcher:", error);
      alert("Error fetching researcher data.");
    } finally {
      setLoading(false);
    }
  };

  const handleFetchEmails = async () => {
    if (!researcherData) return;
    console.log("heheh  e ",researcherData);

    // const dataaa = researcherData.map()
    setLoading(true);
    try {
      const response = await axios.post(
        "http://localhost:8000/api/get-email-templates/",
        {
          researcher: researcher,
        }
      );
     
      setEmailTemplates(response.data);
      setStep(4);
    } catch (error) {
      console.error("Error fetching email templates:", error);
      alert("Failed to fetch email templates.");
    } finally {
      setLoading(false);
    }
  };

  const handleSendEmail = async () => {
    if (!selectedTemplate) return;

    setLoading(true);
    try {
      await axios.post("http://localhost:8000/api/send-email/", {
        template: selectedTemplate,
        researcher: researcher,
        resumeId: file?.name || "test_resume.pdf",
      });
      alert("Email sent successfully!");
    } catch (error) {
      console.error("Error sending email:", error);
      alert("Failed to send email. Please try again.");
    } finally {
      setLoading(false);
    }
  };


  


  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="nav-content">
          <button className="logo" onClick={() => setStep(1)}>
            <Mail className="icon" />
            <span className="title">ResearchReach</span>
          </button>

          {/* API Status Indicator */}
          <div className="status-indicator">
            <div
              className={`${apiConnected ? "status-dot-g" : "status-dot-r"}`}
            ></div>
            <span className="status-text">
              {apiConnected ? "APIs Connected" : "APIs Disconnected"}
            </span>
          </div>
        </div>
      </nav>

      <main
        className={`${selectedTemplate ? "main-content-4" : "main-content"}`}
      >
        <div className="header-section">
          <h1 className="main-title">Research Internship Email Generator</h1>
          <div className="step-indicator">
            <span className="current-step">Step {step}</span>
            <span className="separator">/</span>
            <span className="total-steps">4</span>
          </div>
        </div>

        <div className="card">
          <div className={`step-container ${step !== 1 ? "hidden" : ""}`}>
            <div className="step">
              {loading?<Loader2 className="loading-icon" />:<Upload className="step-icon" />}
              <h2 className="step-title">Upload Your Resume</h2>
              <p className="step-description">
                We'll analyze your experience to find relevant research matches.
              </p>
              <label className="file-upload-label">
                <input
                  type="file"
                  className="file-input"
                  accept=".pdf,.doc,.docx"
                  onChange={handleFileUpload}
                />
                <div className="upload-area">
                  <Upload className="upload-icon" />

                  <span className="upload-text">
                    Upload Resume (PDF, DOC, DOCX)
                  </span>
                </div>
              </label>
            </div>
          </div>

          {/* Step 2: Researcher Search */}
          <div className={`step-container ${step !== 2 ? "hidden" : ""}`}>
            <div className="step">
              <Search className="step-icon" />
              <h2>Find a Researcher</h2>
              <p>Search for the researcher you'd like to contact</p>
              <form onSubmit={handleResearcherSearch} className="search-form">
                <div className="search-group">
                  <input
                    type="text"
                    value={researcher}
                    onChange={(e) => setResearcher(e.target.value)}
                    placeholder="Enter researcher name or institution"
                    className="search-input"
                  />
                  <button type="submit" className="btn">
                    {loading?"Loading...":"Search"}
                  </button>
                </div>
              </form>
            </div>
          </div>

          {/* Step 3: Display Research Papers */}
          <div className={`step-container ${step !== 3 ? "hidden" : ""}`}>
            <div className="step">
              <Edit3 className="step-icon" />
              <h2>Matching Research Papers</h2>
              <p>These papers match your profile</p>

              {loading ? (
                <p>
                  <Loader2 className="loading-icon" /> Generating Email...
                </p>
              ) : researcherData && researcherData.length > 0 ? (
                <div className="research-list">
                  <h3>{researcherData[currentIndex].researcher}</h3>
                  <div className="paper-item">
                    <strong>{researcherData[currentIndex].title}</strong>
                    <p>
                      {researcherData[currentIndex].abstract ||
                        "No abstract available."}
                    </p>
                    <button
                      onClick={() =>
                        window.open(
                          researcherData[currentIndex].link,
                          "_blank",
                          "noopener,noreferrer"
                        )
                      }
                      className="view-paper-button"
                    >
                      View Paper
                    </button>
                  </div>

                  <div className="navigation">
                    <button onClick={() => setCurrentIndex(0)}>1</button>{" "}
                    {currentIndex + 1 < researcherData.length && (
                      <button onClick={() => nextPaper()}>
                        {currentIndex + 2}
                      </button>
                    )}{" "}
                    <span>...</span>{" "}
                    <button
                      onClick={() => setCurrentIndex(researcherData.length - 1)}
                      disabled={currentIndex === researcherData.length - 1}
                    >
                      {researcherData.length}
                    </button>
                  </div>
                </div>
              ) : (
                <p>No research papers found.</p>
              )}

              <button onClick={handleFetchEmails} className="btn">
                Proceed to Email Templates
              </button>
            </div>
          </div>

          {/* Step 4: Email Templates */}
          <div className={selectedTemplate ? "Fixer" : ""}>
            <div className={`step-container ${step !== 4 ? "hidden" : ""}`}>
              <div className={`${selectedTemplate ? "step-4" : "step"}`}>
                <Edit3 className="step-icon" />
                <h2>Choose Your Email Template</h2>
                <p>Select and customize your preferred email style</p>

                <div className="templates-grid">
                  {emailTemplates.map((template, index) => (
                    <div
                      key={index}
                      className={`template-card ${
                        selectedTemplate?.type === template.type
                          ? "selected"
                          : ""
                      }`}
                      onClick={() => setSelectedTemplate(template)}
                    >
                      <h3>{template.type}</h3>
                      <p>{template.content.substring(0, 100)}...</p>
                    </div>
                  ))}
                </div>
              </div>
              {selectedTemplate && (
                <div className="email-editor">
                  <textarea
                    className="email-content"
                    value={selectedTemplate.content}
                    onChange={(e) =>
                      setSelectedTemplate({
                        ...selectedTemplate,
                        content: e.target.value,
                      })
                    }
                  />
                  <button onClick={handleSendEmail} className="btn send-button">
                    <Send className="btn-icon" />
                    Send Email
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;













