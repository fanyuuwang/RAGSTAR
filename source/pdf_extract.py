import argparse
import pdfplumber
import google.generativeai as genai
import glob
import os

def generate_prompt(extracted_text: str) -> str:
    prompt = f"""
I have extracted text from a PDF file using Python, but the result includes unexpected newline breaks and embedded figure captions that disrupt the content's flow. Please help me refine the extracted text by performing the following tasks:

1. **Remove Unnecessary Newlines:** Detect and remove random newline characters so that sentences and paragraphs are properly formatted.
2. **Filter Out Figure Content:** Identify and remove any lines or sections that refer to figures (e.g., "Figure 1", "Fig.", etc.), unless they are essential for understanding the context.
3. **Reformat and Organize:** Reorganize the text into clear, coherent paragraphs while preserving the original meaning and important details.
4. **Proofread:** Ensure that the final output is grammatically correct and reads naturally.

Here is the raw extracted text for processing:
{extracted_text}
Please directly output the cleaned and formatted text in your response without any prefix answer so that I can directly extract it.
Your response:
"""
    return prompt.strip()

def gemini(prompt):
    contents = [{"role": "user", "parts": prompt}]
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(contents=contents)
    return response.text

def read_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        cleaned_page_text = []
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                cleaned_page = gemini(generate_prompt(page_text))
                cleaned_page_text.append(cleaned_page)
        final_text = "\n\n".join(cleaned_page_text)
    output_path = pdf_path.replace(".pdf", ".txt")
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(final_text)

def main():
    parser = argparse.ArgumentParser(description="Extract and clean text from PDFs using Gemini")
    parser.add_argument("--path", required=True, help="Path to folder containing PDF files")
    parser.add_argument("--api-key", required=True, help="Google Generative AI API Key")
    args = parser.parse_args()

    # Set up Gemini API
    genai.configure(api_key=args.api_key)

    # Process PDFs
    pdf_files = glob.glob(os.path.join(args.path, "*.pdf"))
    if not pdf_files:
        print("No PDF files found in the specified path.")
        return

    for pdf_file in pdf_files:
        try:
            print(f"Processing: {pdf_file}")
            read_pdf(pdf_file)
        except Exception as e:
            print(f"Failed to process {pdf_file} due to: {e}")

if __name__ == "__main__":
    main()