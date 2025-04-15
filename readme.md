# From Domain Documents to Requirements: AI-Powered Retrieval-Augmented Generation in the Space Industry

**The official Code Implementation**

*Before you start, you need to have following preparation*

- Mission file
- Domain Documents

1. Preprocess the files.
python process_pdfs.py --path ./domain_docs --api-key YOUR_ACTUAL_API_KEY

2. Do classification for mission file
python classify_paragraphs.py --input ./data/mission.txt --output ./results/labels.txt

3. Find related domain documents with the output in ./results/labels.txt
python extract_related_docs.py --output ./results/labels.txt --path ./domain_docs/

4. Generate corresponding prompt included the extracted information for LLMs
python generate_prompt.py --docs "./domain_docs/*.txt" --mission "./mission_data/mission.txt" --output "./generated_prompts/output_prompt.txt"
