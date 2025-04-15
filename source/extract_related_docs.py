import json
import os
import sys
import random
import numpy as np

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)
print(ROOT_DIR)
import argparse

from source.gte import GTE
import glob
import re

def split_into_three(lst):
    n = len(lst)
    # Determine base size for each chunk and the number of extra items
    chunk_size = n // 3
    remainder = n % 3
    parts = []
    start = 0
    # Distribute extra items among the first `remainder` chunks
    for i in range(3):
        extra = 1 if i < remainder else 0
        end = start + chunk_size + extra
        parts.append(lst[start:end])
        start = end
    return parts

def read_txt(file_path):
    with open(file_path, "r") as file:
        lines = file.read()
        lines = lines.split("\n\n")
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line != ""]
        new_lines = []
        for line in lines:
            if (len(re.sub(r'[^a-zA-Z0-9\s]+', '', line)) / len(line) > 0.5) and len(
                    re.sub(r'[^a-zA-Z0-9\s]+', '', line)) > 50:
                new_lines.append(line)
    return new_lines
def read_text_file(file_path):
    total_files_text = []
    total_files_name = []
    for text_file in glob.glob(f"{file_path}/*.txt"):
        lines = read_txt(text_file)
        parts = split_into_three(lines)
        total_files_text.append(["\n".join(part) for part in parts])
        total_files_name.append(text_file)

    return total_files_text, total_files_name

def encode_file(single_file, model):
    embeddings = model.do_embedding(single_file)

    return embeddings

def get_classes():
    class1 = """Payload
   Description: The mission-specific instruments and equipment onboard the spacecraft directly achieve its primary objectives.
   This includes any sensors, scientific apparatus, or communication equipment that generate mission data or perform the core function of the mission, separate from the support systems.
   Keywords: scientific instrument, sensor, camera, radar, spectrometer, telescope, communication transponder, experiment module, mission payload"""
    class2 = """Platform
   Description: The supporting spacecraft bus and all its subsystems that ensure the spacecraft’s operation, aside from the payload.
   The platform provides the infrastructure and services that keep the spacecraft functional, including structural support, power, thermal regulation, attitude/orbit control, propulsion, and communication hardware.
   Keywords: spacecraft bus, structure, power supply (solar panels, batteries), thermal control (radiators, insulation), attitude determination and control (gyros, reaction wheels, star trackers), propulsion system (thrusters), communications subsystem (antennas, transceivers)"""
    class3 = """Launch Vehicle
   Description: The rocket or launch system that delivers the spacecraft into its intended orbit or trajectory.
   This category covers all aspects of the launch phase, including the choice of launch vehicle, its performance capabilities (mass, volume, and energy capacity), and the conditions and constraints of launch.
   It encompasses launch environment factors (vibration, g-forces, acoustic noise) as well as integration and deployment considerations.
   Keywords: rocket, launcher, launch mass capacity, launch window, launch site, fairing size, lift-off, ascent profile, injection orbit, launch vibrations, g-loads"""
    class4 = """Orbit-Related Aspects
   Description: All characteristics of the spacecraft’s orbit and trajectory in space, defining where and how it travels after launch.
   This includes the type of orbit (e.g. low Earth orbit, geostationary orbit, etc.), specific parameters (altitude, inclination, period, eccentricity), and any special orbital regimes or maneuvers.
   It also covers environmental factors such as gravitational conditions, atmospheric drag, radiation exposure, eclipse periods, and station-keeping requirements.
   Keywords: orbit type (LEO, MEO, GEO, polar, Sun-synchronous, elliptical, Lagrange point), orbital altitude, inclination, orbital period, ground track, transfer orbit, orbital insertion, station-keeping, maneuvers (orbit raising, inclination change), drag, radiation belts, eclipse cycle"""
    class5 = """On-Board Data Handling
   Description: The spacecraft’s internal systems for command execution and data management.
   This covers how the spacecraft processes, stores, and transmits data, including on-board computers and electronics that handle flight software and data flow.
   It involves receiving and decoding commands from the ground, collecting and buffering payload data, processing/compressing data, storing it in memory, and preparing telemetry for downlink.
   Keywords: on-board computer, flight software, command and data handling, data processor, data storage (memory, solid-state recorder), telemetry data, telecommand processing, data bus, on-board data compression, real-time data processing"""
    class6 = """Reference Operation Scenarios / Observation Characteristics
   Description: The typical mission operational scenarios and the characteristics of the spacecraft’s observations or mission output.
   This category describes how the mission is carried out: the utilization of the payload over time, modes of operation, and the nature of data collection.
   It includes scheduling of observations, coverage and targeting strategies, and performance parameters such as resolution or revisit frequency.
   Keywords: concept of operations, mission timeline, observation mode (continuous monitoring, targeted imaging, scan schedule), coverage area, field of view, swath width, spatial resolution, temporal resolution (revisit time, sampling frequency), imaging cadence, operational modes (survey, calibration, standby), target acquisition, pointing strategy"""
    class7 = """Operability / Autonomy Requirements
   Description: The requirements and design features related to how the spacecraft is controlled and the degree to which it can operate independently of ground control.
   This covers the level of autonomy, the ease of operation, frequency of ground contact, automatic control capabilities, and onboard decision-making or fault management systems.
   Keywords: ground operations interaction, ground contact frequency (continuous, daily, weekly), teleoperation vs. autonomous operation, on-board autonomy, automated scheduling, intelligent on-board decision-making, fault detection and recovery, fail-safe mechanisms, self-checks, minimal ground intervention, operational simplicity, remote commanding, autonomy level"""

    return [class1, class2, class3, class4, class5, class6, class7]

def neural_label_similarity(vec1, vec2):

    # Define the vectors as lists
    A = vec1
    B = vec2

    # Convert lists to NumPy arrays
    A_np = np.array(A)
    B_np = np.array(B)

    # Compute the dot product
    dot_product = np.dot(A_np, B_np)

    # Compute the norms (magnitudes)
    norm_A = np.linalg.norm(A_np)
    norm_B = np.linalg.norm(B_np)

    # Calculate cosine similarity
    cosine_similarity = dot_product / (norm_A * norm_B)

    return cosine_similarity

def softmax(x):
    # Convert the list to a NumPy array for vectorized operations
    x_np = np.array(x)

    # Compute the exponentials
    exp_x = np.exp(x_np)

    # Compute the softmax by dividing by the sum of the exponentials
    softmax = exp_x / np.sum(exp_x)

    return softmax

def do_score(emb1, emb2):
    scores = (emb1 @ emb2.T) * 100
    return scores.tolist()

def load_query_label(path):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Neural label distribution" in line:
                label_str = line.strip().split(":")[-1].strip()
                label = json.loads(label_str.replace("'", "\"")) if "[" in label_str else eval(label_str)
                return label
    raise ValueError("No valid neural label distribution found in the file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute similarity between document vectors and query label")
    parser.add_argument("--output", required=True, help="Path to the file containing query_label (e.g., labels.txt)")
    parser.add_argument("--path", required=True, help="Path to directory containing domain docs (.txt)")
    args = parser.parse_args()

    query_label = load_query_label(args.output)
    all_scores = []
    gte = GTE()
    total_embeddings = []
    file_path = args.path

    text_files, files_name = read_text_file(file_path)
    classes = get_classes()

    class_embeddings = []
    for single_class in classes:
        class_embeddings.append(encode_file(single_class, gte))

    for text_file in text_files:
        s_emb = encode_file(text_file, gte)
        total_embeddings.append(s_emb)
        scores = [sum(do_score(emb1, s_emb)[0]) for emb1 in class_embeddings]
        all_scores.append(scores)

    all_similarity = []
    for file_name, scores in zip(files_name, all_scores):
        all_similarity.append(neural_label_similarity(scores, query_label))

    ranking = sorted(zip(files_name, all_similarity), key=lambda x: x[1], reverse=True)

    for file_name, similarity in ranking:
        if similarity > 0.01:
            with open(file_name, "r") as original_file:
                related_path = file_name.replace("domain_docs", "related_docs")
                os.makedirs(os.path.dirname(related_path), exist_ok=True)
                with open(related_path, "w") as new_file:
                    original_content = original_file.readlines()
                    new_file.writelines(original_content)