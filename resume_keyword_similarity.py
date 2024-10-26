import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import PyPDF2
import os

model = api.load("word2vec-google-news-300")

position_keywords = ["Python", "Java", "Machine Learning", "REST API", "Agile", "Cloud"]

def extract_keywords_from_pdf(pdf_path):
    keywords = {}
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                words = text.split()
                for word in words:
                    keywords[word] = keywords.get(word, 0) + 1
    return keywords

def calculate_similarity(position_keywords, candidate_keywords, model):
    similarity_scores = {}
    for pos_word in position_keywords:
        if pos_word in model:
            pos_vector = model[pos_word]
            max_similarity = 0
            count = candidate_keywords.get(pos_word, 0)
            for cand_word, cand_count in candidate_keywords.items():
                if cand_word in model:
                    cand_vector = model[cand_word]
                    similarity = cosine_similarity([pos_vector], [cand_vector])[0][0]
                    if similarity > max_similarity:
                        max_similarity = similarity
            similarity_scores[pos_word] = (max_similarity * 100, count)
        else:
            similarity_scores[pos_word] = (0, candidate_keywords.get(pos_word, 0))

    return similarity_scores

candidates_dir = r'resumes'
candidate_scores = {}

for pdf_file in os.listdir(candidates_dir):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(candidates_dir, pdf_file)
        candidate_keywords = extract_keywords_from_pdf(pdf_path)
        score = calculate_similarity(position_keywords, candidate_keywords, model)
        candidate_scores[pdf_file] = score


print(f"{'Candidate':<40} {'Keyword':<40} {'Score':<10} {'Count':<10}")
for candidate, scores in candidate_scores.items():
    for keyword, (score, count) in scores.items():
        print(f"{candidate:<40} {keyword:<40} {score:<10.2f}  {count:<10}")