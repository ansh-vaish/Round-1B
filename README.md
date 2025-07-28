# 📄 Relevant Section Extractor

This repository contains a script that extracts the **most relevant sections** from a collection of documents (PDFs) based on a defined **persona** and **task**. It uses **semantic similarity** to identify which sections of each document are most aligned with the task at hand.

---

## 🚀 Overview

The script works by:
1. Parsing and processing documents using helper functions.
2. Computing semantic similarity scores between each section of the document and a query constructed from the persona and task.
3. Ranking the sections by relevance.
4. Selecting the **top-k** most relevant sections, ensuring **only one section per document** is chosen to increase diversity.
5. Saving a structured JSON output with metadata, section rankings, and full text of the top sections.

---

## 🧠 Approach

### 🔹 Step 1: Preprocessing
- Input consists of a JSON config and a directory of PDFs.
- The function `process_input_documents()` (from `processor.py`) parses PDFs and extracts page-wise text.

### 🔹 Step 2: Embedding and Similarity
- We use the [SentenceTransformers](https://www.sbert.net/) model `all-MiniLM-L6-v2` to convert text into embeddings.
- The similarity score is computed using **cosine similarity** between:
  - The embedding of the query: `"persona: task"`
  - The embedding of each section of text from the PDFs.

### 🔹 Step 3: Scoring and Ranking
- Each section is scored based on its relevance to the query.
- Titles are cleaned using `clean_section_title()` from `utils.py`.
- The highest-scoring section from each document is considered until the `top_k` threshold is met.

### 🔹 Step 4: Output Generation
- The output JSON includes:
  - Metadata (input docs, persona, task, timestamp)
  - A ranked list of relevant sections
  - The refined full text for each selected section

---

## 📂 File Structure

.
├── extractor.py # Main script
├── processor.py # PDF + input processor (not shown here)
├── utils.py # Title cleaner utility (not shown here)
├── challenge1b_input.json # Input JSON (config)
├── pdf/ # Folder containing PDF files
└── challenge1b_output.json # Output with selected sections

yaml
Copy
Edit

---

## 📥 Input Format

`challenge1b_input.json` should include:
```json
{
  "persona": "HR Manager",
  "job_to_be_done": "Find the best fit for a leadership role",
  "documents": [
    {"filename": "resume1.pdf"},
    {"filename": "resume2.pdf"}
  ]
}
