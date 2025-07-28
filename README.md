# Adobe India Hackathon - Round 1B

This project is part of **Round 1B** of the Adobe India Hackathon. It performs **Persona-Driven Document Intelligence** using sentence transformers to extract meaningful section titles from PDFs and generate structured output.

---

## 🧩 Project Structure
├── challenge1b_input.json # Input configuration with file names and personas
├── challenge1b_output.json # Output file with extracted section titles
├── pdf/ # Folder containing all source PDFs
│ ├── *.pdf
├── extract.py # Main runner script
├── processor.py # Logic for processing pages and sections
├── utils.py # Helper functions (embedding, scoring, etc.)
├── requirements.txt # Python dependencies
└── dockerfile # Docker container setup

---


---

## 🚀 Features

- ✅ Clean PDF text extraction using PyMuPDF
- ✅ Sentence embedding using `sentence-transformers`
- ✅ Section title selection based on cosine similarity
- ✅ Persona relevance filtering
- ✅ Fully offline-capable processing
- ✅ Dockerized for reproducibility and portability

---

## 🔧 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/ansh-vaish/Adobe-Hackathon.git
cd "Adobe-Hackathon/Round - 1B"

2. Install Python dependencies
Make sure you have Python 3.9+ installed.
pip install -r requirements.txt

3. Run the extractor
python extract.py
🔁 It reads from challenge1b_input.json and writes to challenge1b_output.json.

🐳 Run via Docker (Recommended)

1. Build the Docker image
docker build -t round1b-extractor .

2. Run the extraction in a container
docker run --rm -v "${PWD}:/app" round1b-extractor python extract.py
✅ Output will be saved in your local folder as challenge1b_output.json.

📥 Input Format (challenge1b_input.json)
[
  {
    "file_name": "sample1.pdf",
    "persona": "student"
  },
  {
    "file_name": "sample2.pdf",
    "persona": "working professional"
  }
]

📤 Output Format (challenge1b_output.json)
[
  {
    "file_name": "sample1.pdf",
    "extracted_sections": [
      "Introduction",
      "Key Learnings",
      "Conclusion"
    ]
  },
  {
    "file_name": "sample2.pdf",
    "extracted_sections": [
      "Executive Summary",
      "Career Opportunities"
    ]
  }
]

🔍 Persona-Aware Intelligence
The model extracts candidate sections and scores them for semantic similarity to persona-specific queries like:

For student: "overview for students", "learning section", "academic relevance"

For professional: "summary for professionals", "business insights", "career impact"

These reference queries are embedded and matched using cosine similarity with section candidates.

⚖️ License
This code is developed as part of the Adobe India Hackathon 2025 and is intended for submission/review only. Please do not reuse or distribute without permission.

