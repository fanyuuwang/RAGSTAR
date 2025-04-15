import os
import sys
import re
import argparse
from source.icRALM import initiate_TRAG

def split_text_into_paragraphs(text):
    # Assuming paragraphs are separated by two newlines
    paragraphs = [para.strip() for para in text.split("\n\n") if para.strip()]
    return paragraphs

def main():
    parser = argparse.ArgumentParser(description="Classify paragraphs using TRAG model")
    parser.add_argument("--input", required=True, help="Path to the input text file")
    parser.add_argument("--output", required=True, help="Path to the output result file")
    args = parser.parse_args()

    trag_model = initiate_TRAG()

    with open(args.input, "r", encoding="utf-8") as file:
        raw_text = file.read()

    lines = split_text_into_paragraphs(raw_text)

    # Filter: only keep lines with more than 50 alphanumeric characters and > 50% are alphanumeric
    new_lines = [
        line for line in lines
        if (len(re.sub(r'[^a-zA-Z0-9\s]+', '', line)) / len(line) > 0.5)
        and len(re.sub(r'[^a-zA-Z0-9\s]+', '', line)) > 50
    ]

    neural_label = [0, 0, 0, 0, 0, 0, 0]
    class_label = []

    for text in new_lines:
        current_label = trag_model.do_classify(text)
        if current_label == 7:
            continue
        neural_label[current_label] += 1
        class_label.append(current_label)

    with open(args.output, "a", encoding="utf-8") as file:
        file.write(f"Neural label distribution: {neural_label}\n")
        file.write(f"Individual labels: {class_label}\n")

if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(ROOT_DIR)
    print(f"Project Root: {ROOT_DIR}")
    main()