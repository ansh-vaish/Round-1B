import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from processor import process_input_documents
from utils import clean_section_title

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_relevance_score(text: str, persona: str, task: str) -> float:
    query = f"{persona}: {task}"
    query_embedding = model.encode([query])
    section_embedding = model.encode([text])
    return cosine_similarity(query_embedding, section_embedding)[0][0]

def extract_relevant_sections(input_json_path, pdf_dir, output_json_path, top_k=5):
    input_data, extracted_pages, persona, task = process_input_documents(input_json_path, pdf_dir)

    section_candidates = []
    seen_titles = set()
    seen_docs = set()

    for filename, pages in extracted_pages.items():
        for i, text in enumerate(pages):
            if not text.strip():
                continue

            title = clean_section_title(text.strip().split('\n')[0])
            if title.lower() == "untitled section" and filename in seen_docs:
                continue  # avoid duplicate untitleds per document

            score = compute_relevance_score(text, persona, task)
            section_candidates.append({
                "document": filename,
                "section_title": title,
                "score": score,
                "page_number": i + 1,
                "refined_text": text.strip()
            })

            seen_docs.add(filename)

    section_candidates.sort(key=lambda x: x['score'], reverse=True)

    selected_docs = set()
    top_sections = []
    for sec in section_candidates:
        if sec["document"] not in selected_docs:
            top_sections.append(sec)
            selected_docs.add(sec["document"])
        if len(top_sections) >= top_k:
            break

    output = {
        "metadata": {
            "input_documents": [doc['filename'] for doc in input_data['documents']],
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [
            {
                "document": sec["document"],
                "section_title": sec["section_title"],
                "importance_rank": rank + 1,
                "page_number": sec["page_number"]
            }
            for rank, sec in enumerate(top_sections)
        ],
        "subsection_analysis": [
            {
                "document": sec["document"],
                "refined_text": sec["refined_text"],
                "page_number": sec["page_number"]
            }
            for sec in top_sections
        ]
    }

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"Output written to {output_json_path}")

if __name__ == "__main__":
    extract_relevant_sections(
        input_json_path="challenge1b_input.json",
        pdf_dir="pdf",
        output_json_path="challenge1b_output.json",
        top_k=5
    )
