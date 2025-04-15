import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


class InContextClassifier(torch.nn.Module):
    def __init__(self):
        super(InContextClassifier, self).__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Load model & tokenizer
        model_name = "meta-llama/Llama-3.1-8B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(
            self.device)
        self.model.eval()

    #  class1 = """Payload
    # Description: The mission-specific instruments and equipment onboard the spacecraft directly achieve its primary objectives.
    # This includes any sensors, scientific apparatus, or communication equipment that generate mission data or perform the core function of the mission, separate from the support systems.
    # Keywords: scientific instrument, sensor, camera, radar, spectrometer, telescope, communication transponder, experiment module, mission payload"""
    #  class2 = """Platform
    # Description: The supporting spacecraft bus and all its subsystems that ensure the spacecraft’s operation, aside from the payload.
    # The platform provides the infrastructure and services that keep the spacecraft functional, including structural support, power, thermal regulation, attitude/orbit control, propulsion, and communication hardware.
    # Keywords: spacecraft bus, structure, power supply (solar panels, batteries), thermal control (radiators, insulation), attitude determination and control (gyros, reaction wheels, star trackers), propulsion system (thrusters), communications subsystem (antennas, transceivers)"""
    #  class3 = """Launch Vehicle
    # Description: The rocket or launch system that delivers the spacecraft into its intended orbit or trajectory.
    # This category covers all aspects of the launch phase, including the choice of launch vehicle, its performance capabilities (mass, volume, and energy capacity), and the conditions and constraints of launch.
    # It encompasses launch environment factors (vibration, g-forces, acoustic noise) as well as integration and deployment considerations.
    # Keywords: rocket, launcher, launch mass capacity, launch window, launch site, fairing size, lift-off, ascent profile, injection orbit, launch vibrations, g-loads"""
    #  class4 = """Orbit-Related Aspects
    # Description: All characteristics of the spacecraft’s orbit and trajectory in space, defining where and how it travels after launch.
    # This includes the type of orbit (e.g. low Earth orbit, geostationary orbit, etc.), specific parameters (altitude, inclination, period, eccentricity), and any special orbital regimes or maneuvers.
    # It also covers environmental factors such as gravitational conditions, atmospheric drag, radiation exposure, eclipse periods, and station-keeping requirements.
    # Keywords: orbit type (LEO, MEO, GEO, polar, Sun-synchronous, elliptical, Lagrange point), orbital altitude, inclination, orbital period, ground track, transfer orbit, orbital insertion, station-keeping, maneuvers (orbit raising, inclination change), drag, radiation belts, eclipse cycle"""
    #  class5 = """On-Board Data Handling
    # Description: The spacecraft’s internal systems for command execution and data management.
    # This covers how the spacecraft processes, stores, and transmits data, including on-board computers and electronics that handle flight software and data flow.
    # It involves receiving and decoding commands from the ground, collecting and buffering payload data, processing/compressing data, storing it in memory, and preparing telemetry for downlink.
    # Keywords: on-board computer, flight software, command and data handling, data processor, data storage (memory, solid-state recorder), telemetry data, telecommand processing, data bus, on-board data compression, real-time data processing"""
    #  class6 = """Reference Operation Scenarios / Observation Characteristics
    # Description: The typical mission operational scenarios and the characteristics of the spacecraft’s observations or mission output.
    # This category describes how the mission is carried out: the utilization of the payload over time, modes of operation, and the nature of data collection.
    # It includes scheduling of observations, coverage and targeting strategies, and performance parameters such as resolution or revisit frequency.
    # Keywords: concept of operations, mission timeline, observation mode (continuous monitoring, targeted imaging, scan schedule), coverage area, field of view, swath width, spatial resolution, temporal resolution (revisit time, sampling frequency), imaging cadence, operational modes (survey, calibration, standby), target acquisition, pointing strategy"""
    #  class7 = """Operability / Autonomy Requirements
    # Description: The requirements and design features related to how the spacecraft is controlled and the degree to which it can operate independently of ground control.
    # This covers the level of autonomy, the ease of operation, frequency of ground contact, automatic control capabilities, and onboard decision-making or fault management systems.
    # Keywords: ground operations interaction, ground contact frequency (continuous, daily, weekly), teleoperation vs. autonomous operation, on-board autonomy, automated scheduling, intelligent on-board decision-making, fault detection and recovery, fail-safe mechanisms, self-checks, minimal ground intervention, operational simplicity, remote commanding, autonomy level"""
    def get_classes(self):
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

    @torch.inference_mode()
    def evaluate_query_with_docs(self, query: str, topk: int = 1):
        doc_logprobs = []
        docs = self.get_classes()

        for doc_id, doc_text in enumerate(docs):
            doc_text = "\n".join(doc_text)
            query_text = "\n".join(query)
            doc_enc = self.tokenizer.encode(doc_text, truncation=True)
            query_enc = self.tokenizer.encode(query_text, add_special_tokens=False)
            input_ids = doc_enc + query_enc
            input_ids_tensor = torch.tensor([input_ids], device=self.device)
            labels = [-100] * len(doc_enc) + query_enc
            labels_tensor = torch.tensor([labels], device=self.device)

            out = self.model(input_ids_tensor, labels=labels_tensor)
            num_query_tokens = len(query_enc)
            neg_log_likelihood = out.loss.item() * num_query_tokens
            doc_logprobs.append(neg_log_likelihood)

            # Delete tensors to free up memory
            del input_ids_tensor, labels_tensor, out
            torch.cuda.empty_cache()

        ranking = sorted(zip([num for num in range(7)], doc_logprobs), key=lambda x: x[1])
        return ranking[0][0]
    def evaluate_rag(self,
                     query: str,
                     topk: int,
                     ):
        """
        Evaluate a list of queries with each query having its own list of retrieved docs.
        Returns a list of results (one per query).
        """
        res = self.evaluate_query_with_docs(
            query=query,
            topk=topk,
        )
        return res

    def do_classify(self, text, topk=2):
        combined_text = f"""You are provided with the following text describing aspects of a spacecraft mission: {text}"""
        query_results = self.evaluate_rag(combined_text, topk=topk)
        return query_results


def initiate_TRAG(labels=None):
    model = InContextClassifier(labels)
    return model
