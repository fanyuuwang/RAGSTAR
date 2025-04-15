import os
import sys
import glob
import json
import re
import argparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
print(f"ROOT_DIR: {ROOT_DIR}")

from source.icRALM import initiate_TRAG
from source.gte import GTE
from source.rag import initiate_RAG


def read_txt(file_path):
    with open(file_path, "r") as file:
        lines = file.read().split("\n\n")
        lines = [line.strip() for line in lines if line.strip()]
        return [
            line for line in lines
            if
            (len(re.sub(r'[^a-zA-Z\s]+', '', line)) / len(line) > 0.5) and len(re.sub(r'[^a-zA-Z\s]+', '', line)) > 50
        ]


def split_into_three(lst):
    n = len(lst)
    chunk_size = n // 3
    remainder = n % 3
    parts, start = [], 0
    for i in range(3):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        parts.append(lst[start:end])
        start = end
    return parts


def read_text_file(file_pattern):
    total_files_text = []
    total_files_name = []
    for text_file in glob.glob(file_pattern):
        lines = read_txt(text_file)
        parts = split_into_three(lines)
        total_files_text.append(["\n".join(part) for part in parts])
        total_files_name.append(text_file)
    return total_files_text, total_files_name


def get_classes():
    # (Class descriptions remain unchanged for brevity)
    class1 = """Payload ..."""
    class2 = """Platform ..."""
    class3 = """Launch Vehicle ..."""
    class4 = """Orbit-Related Aspects ..."""
    class5 = """On-Board Data Handling ..."""
    class6 = """Reference Operation Scenarios / Observation Characteristics ..."""
    class7 = """Operability / Autonomy Requirements ..."""
    return [class1, class2, class3, class4, class5, class6, class7]


def generate_llm_prompt(scenario: str, additional_requirements: list, domain_standards: list) -> str:
    return f"""
You are a requirements analyst from a satellite communications (SATCOM) company, named Starbound Space Solutions, participating in a SpaceX Rideshare launch. Based on the task description, additional requirements, and domain standards provided, please identify and summarise all information relevant to the following areas.

Scenario Description:
{scenario}

Requirements Description:
{'\n'.join(additional_requirements)}

Domain Standards:
{'\n'.join(domain_standards)}

1. Read the provided Scenario Description carefully and understand the application scenario.
2. Identify related content from the provided Requirements Description and Domain Standards.
3. Structure the response in sections. Make sure to use language that a systems or requirements analyst can directly map to their documentation process.

Your response:
"""


def do_score(emb1, emb2):
    scores = (emb1 @ emb2.T) * 100
    return scores.tolist()


def main():
    parser = argparse.ArgumentParser(description="Generate LLM prompts using scenario and domain documents.")
    parser.add_argument("--docs", required=True, help="Path to the domain document folder (e.g., ./domain_docs/*.txt)")
    parser.add_argument("--mission", required=True, help="Path to the mission requirements text file")
    parser.add_argument("--output", required=True, help="Path to write the generated prompt output")
    args = parser.parse_args()

    trag_model = initiate_TRAG()
    gte = GTE()
    my_rag = initiate_RAG()

    # Example scenario
    application_scenarios = ["""Mechanical Integration Requirements:
Describe all supported mechanical interface types (e.g., circular, 4-point, CubeSat) and plate configurations (e.g., Quarter, Half, XL, CubeSat Plate).
Summarize physical constraints, including payload volume, center of gravity, fastener specs, and interface stiffness.
Indicate which configurations are suitable for 8", 15", or 24" interface payloads."""]

    # Load mission requirements and domain documents
    text_files, files_name = read_text_file(args.docs)
    product_lines = read_txt(args.mission)

    for application_scenario in application_scenarios:
        current_class = trag_model.do_classify(application_scenario)
        class_des = get_classes()[current_class]

        class_embeddings = gte.do_embedding(class_des)
        all_scores = []
        for text_file in text_files:
            s_emb = gte.do_embedding(text_file)
            score = sum(do_score(class_embeddings, s_emb))
            all_scores.append(score)

        sorted_pairs = sorted(zip(all_scores, files_name))
        domain_docs = [doc for _, doc in sorted_pairs][:3]

        related_product_requirements = my_rag.do_rag(application_scenario, product_lines, topk=10)

        file_lines = []
        for file_name in domain_docs:
            file_lines += read_txt(file_name)

        domain_standards = my_rag.do_rag(application_scenario, file_lines, topk=20)

        prompt = generate_llm_prompt(application_scenario, related_product_requirements, domain_standards)

        with open(args.output, "a", encoding="utf-8") as file:
            file.write(prompt + "\n\n" + "=" * 80 + "\n\n")


if __name__ == "__main__":
    main()