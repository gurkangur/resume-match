# Resume Keyword Matching

This project aims to assess the relevance of resumes based on specified position-related keywords using Natural Language Processing (NLP) techniques. By analyzing resumes in PDF format, the project computes similarity scores for each candidate's keywords against the desired keywords for a job position.

## Features

- Extracts keywords from PDF resumes.
- Utilizes Word2Vec model to calculate cosine similarity between position keywords and candidate keywords.
- Outputs similarity scores along with keyword counts for easy evaluation.

## Requirements

Make sure you have the following libraries installed:

- `gensim`
- `sklearn`
- `PyPDF2`
- `numpy`

You can install these libraries using pip:

```bash
pip install gensim scikit-learn PyPDF2 numpy
```
## Usage

### Step 1: Prepare Resumes

- Create a directory named `resumes`.
- Place the PDF files of candidates' resumes in this directory.

### Step 2: Configure Position Keywords

- Open the script and locate the `position_keywords` list.
- Modify it to include the keywords relevant to the job position you are evaluating. For example:

    ```python
    position_keywords = ["Python", "Java", "Machine Learning", "REST API", "Agile", "Cloud"]
    ```

### Step 3: Run the Script

- Execute the script using Python. You can run it in your terminal or command prompt:

    ```bash
    python resume_keyword_similarity.py
    ```

### Step 4: View Results

- The script will process each PDF resume and print a summary table of keyword similarity scores and counts in the console. The output will look like this:

    ```
    Candidate                                 Keyword                                 Score      Count     
    candidate1.pdf                            Python                                  85.67        5         
    candidate1.pdf                            Java                                    92.12        3         
    candidate2.pdf                            Machine Learning                        78.50        4         
    ...
    ```
