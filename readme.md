# From Domain Documents to Requirements: AI-Powered Retrieval-Augmented Generation in the Space Industry

**The official Code Implementation**

*Before you start, you need to have following preparation*

- Mission file
- Domain Documents

## Execution example

1. Preprocess the files.

python process_pdfs.py --path ./domain_docs --api-key YOUR_ACTUAL_API_KEY

2. Do classification for mission file

python classify_paragraphs.py --input PATH_TO_YOUR_MISSION_FILE.txt --output PATH_TO_OUTPUT_LABELS.txt

3. Find related domain documents with the output in PATH_TO_OUTPUT_LABELS.txt

python extract_related_docs.py --output PATH_TO_OUTPUT_LABELS.txt --path PATH_TO_YOUR_DOMAIN_DOCS_FOLDER

4. Generate corresponding prompt included the extracted information for LLMs

python generate_prompt.py --docs PATH_TO_YOUR_DOMAIN_DOCS_FOLDER --mission PATH_TO_YOUR_MISSION_FILE.txt --output PATH_TO_YOUR_OUTPUT_PROMPT.txt
