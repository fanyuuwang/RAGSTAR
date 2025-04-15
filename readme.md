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

## Example output


You are a requirements analyst from a satellite communications (SATCOM) company, named Starbound Space Solutions, participating in a SpaceX Rideshare launch. Based on the task description, additional requirements, and domain standards provided, please identify and summarise all information relevant to the following areas.

Scenario Description:
Verification and Testing Requirements:
List the test types required (e.g., vibration, acoustic, shock), and specify what testing is mandatory versus advised.
Explain expectations for CubeSats vs. MicroSats.
Identify conditions for reworking fasteners or modifying post-integration designs.

Requirements Description:
6.7.11 REWORKED FASTENERS
Purpose: To ensure that any rework conducted post environmental test verification does not compromise the structural integrity of the Payload or the safety of other Co-Payloads.
Verification: Customers are required to provide details on all reworked fasteners in the final verification test report. Reworked fasteners that comply with Section 5.2.1 do not require prior SpaceX approval for rework, but need to be reported in the test report. Customers should provide the following information:
• Overview of all post-test rework, clearly separating out and indicating which reworked fasteners are compliant to this User Guide and which are not (SpaceX approval required)
• For each, or group of, reworked fasteners installed in a blind hole, provide: fastener diameter, hole depth measurement, fastener length measurement during installation, a close-up photo of the reworked fastener(s), secondary retention method(s), and schematic or photo showing general location of reworked fastener(s)
• For each, or group of, reworked fasteners installed in a through hole, provide: fastener diameter, grip length and protrusion measurement, a close-up photo of the reworked fastener(s), and accompanying schematic or photo showing general location of reworked fastener on the Payload
The following fasteners are exempt from the rework criteria set out above and do not count towards the number of fasteners reworked (best practices on secondary retention features and installation methods still apply): Fasteners used to reattach access panels mounted on fully containerized CubeSats; Fasteners securing non-structural components that are fully containerized within the Payload or an enclosure.
*   **Quasi Static Load:** REQUIRED. Level: Min 1.1 times the limit load in each of 3 axes per Table 6-4 and Table 6-5.
*   **Sine Vibration:** Advised. Level: Limit Levels x 1.0. Duration: 4 oct./minute sweep rate in each of 3 axes.
*   **Acoustic:** Advised. Level: MPE. Duration: 1 minute.
*   **Shock:** Advised. Level: MPE. Not Required.
*   **Random Vibration:** REQUIRED. Level: MPE. Duration: 1 minute in each of 3 axes. Verification that the power inhibit system functions as intended during random vibe.
*   **Electromagnetic Compatibility:** Advised. Not Required.
*   **Thermal Vacuum & Thermal Cycle:** Advised. Level: Acceptance ±10 °C. Duration: 20 cycles total.
*   **Integrated Leak Test:** REQUIRED. Level: MEOP per Table 6-10. Duration: 5 min.
*   **Quasi Static Load:** REQUIRED. Level: Min 1.25 times the limit load in each of 3 axes per Table 6-4 and Table 6-5.
*   **Sine Vibration:** Advised. Level: Limit Levels x 1.25. Duration: 2 oct./minute sweep rate in each of 3 axes.
*   **Acoustic:** Advised. Level: MPE + 6 dB. Duration: 2 minutes.
*   **Shock:** Advised. Level: MPE + 6 dB. Actuations: 3 times in each of 3 orthogonal axes.
*   **Random Vibration:** REQUIRED. Level: MPE + 6 dB. Duration: 2 minutes in each of 3 axes. Verification that the power inhibit system functions as intended during random vibe.
*   **Electromagnetic Compatibility:** Advised. By test: 6 dB EMISM OR By analysis: 12 dB EMISM.
*   **Thermal Vacuum & Thermal Cycle:** Advised. Level: Envelope of MPT and min. range (-24 to 61°C). Duration: 27 cycles total.
*   **Integrated Leak Test:** REQUIRED. Level: MEOP per Table 6-10. Duration: 5 min.
Customer to provide to SpaceX final environmental verification test and/or analysis results for independently tested CubeSats (if applicable) in order to show compliance to Section 6 and in accordance with the SpaceX approved Payload environmental test approach. Customer must use the Payload environmental verification report template provided by SpaceX to summarize data into a single report.
Limited disassembly of the Payload for functional checkouts after the integrated test is allowed without retest, as long as disassembly/rework falls in one or more of the following categories: Fastened joints that meet the criteria in Section 5.2.1; Deployment mechanisms that are deployed and reset using fastener-free resettable devices, such as pin pullers; Deployment mechanisms that are re-assembled after testing and that demonstrate similar workmanship insensitivity to fasteners, have redundant workmanship controls, or undergo post-reassembly proof testing; Installation of add-before-flight items, such as fill/drain line caps, connectors and plugs, as long as these items were present during environmental testing, and suitable secondary retention is demonstrated; Installation of MLI; Replacement of CubeSat mass dummies with CubeSat flight units in CubeSat dispensers; and Fully containerized CubeSats only: all of the above, plus the replacement and resetting of burn wires. Burn wires must be identical and installed in the same way, and integrated testing must show that the original burn wire did not fail as a result of environmental testing.
6.7.4 ACOUSTIC
Purpose: To ensure Payloads are compatible with acoustic environments inside the Launch Vehicle fairing. Note that most Rideshare sized Payloads are driven by structure-borne random vibration (Section 4.1.6) and not by direct acoustic impingement.
Verification: Testing is ADVISED to the acoustic test levels and durations defined in Table 6-1 in accordance with the MPE defined in Section 4.1.4.
*   **Quasi Static Load:** Must be performed on each fully integrated Payload assembly. REQUIRED. Level: Min 1.25 times the limit load in each of 3 axes per Table 6-4 and Table 6-5.
*   **Sine Vibration:** Must be performed on each fully integrated Payload assembly. Advised. Level: Limit Levels x 1.25. Duration: 4 oct./minute sweep rate in each of 3 axes.
*   **Acoustic:** Advised. Level: MPE + 3 dB. Duration: 1 minute.
*   **Shock:** Advised. Level: MPE + 3 dB. Actuations: 2 times in each of 3 orthogonal axes.
*   **Random Vibration:** REQUIRED. Level: MPE + 3 dB. Duration: 1 minute in each of 3 axes. Verification that the power inhibit system functions as intended during random vibe.
*   **Electromagnetic Compatibility:** Advised. Not Required.
*   **Thermal Vacuum & Thermal Cycle:** Advised. Level: Acceptance ±5 °C. Duration: 14 cycles total.
*   **Integrated Leak Test:** REQUIRED. Level: MEOP per Table 6-10. Duration: 5 min.
1.  Static load testing can be achieved through either a sine-burst test or sine vibration (sweep) test. See Section 6.7.2 for further guidance on test load factors and axes. These levels contain some load combination.
2.  Random vibration must be conducted as a standalone test (not combined with static load testing).
3.  Power inhibits must be verified at an integrated level as part of random vibe testing, see Section 6.7.7.
4.  EMISM (6 dB by test, 12 dB by analysis) is already included in Table 4-9.
5.  Thermal cycles can be accrued as a combination of thermal cycling in air and thermal vacuum. It is recommended to include at least four cycles of thermal vacuum unless strong rationale exists that the Payload is not sensitive to vacuum.
6.  Additional requirements apply to individual pressure vessels and systems, see Section 5.5 and 6.8. Pressure Systems that do not meet material compatibility requirements specified in Section 5.5.5 must contact SpaceX for specific leak testing requirements.
One Payload One Volume rule (Standard Offering):
* Each individual Payload volume may only contain one (1) Payload (MicroSat or CubeSat Dispenser).
* Each Payload (excluding CubeSat Dispensers) may only have one (1) deployment channel (exceptions are allowed for 4-point spacecraft).
* Each CubeSat Dispenser may have up to four (4) deployment channels.

Domain Standards:
a. The supplier shall develop and document, for each requirement of the software item in RB (including IRD), a set of tests, test cases (inputs, outputs, test criteria) and test procedures including:
1. testing against the mission data and scenario specified by the customer in 5.2.3.1
2. testing with stress, boundary, and singular inputs;
3. testing the software product for its ability to isolate and reduce the effect of errors;
NOTE: For example: This reduction is done by graceful degradation upon failure, request for operator assistance upon stress, boundary and singular conditions.
4. testing that the software product can perform successfully in a representative operational and non‐intrusive environment.
5. external interface testing including boundaries, protocols and timing test;
6. testing HMI applications as per ECSS‐E‐ST‐10‐11.
b. Validation shall be performed by test.
c. If it can be justified that validation by test cannot be performed, validation shall be performed by either analysis, inspection or review of design.
1. the unit tests are consistent with detailed design and requirements;
2. the unit tests are traceable to software requirements, design and code. NOTE The trace to requirements is used to design the unit test cases in order to predict meaningful expected results.
3. software integration and testing are feasible;
4. operation and maintenance are feasible;
5. all activities defined in clause 5.5.3 are performed;
6. test results conform to expected results;
7. test results, test logs, test data, test cases and procedures, and test documentation are maintained under configuration management;
8. normal termination (i.e. the test end criteria defined in the unit test plan) is achieved;
9. abnormal termination of testing process (e.g. incorrect major fault, out of time) is reported;
10. abnormal termination condition is documented in summary section of the unit test report, together with the unfinished testing and any uncorrected faults.
a. The supplier shall develop and document, for each requirement of the software item in TS (including ICD), a set of tests, test cases (inputs, outputs, test criteria) and test procedures including:
5.2.3.1 Verification and validation process requirements
a. The customer shall specify the requirements needed for planning and setting up the system verification and validation process related to software.
EXPECTED OUTPUT: Verification and validation process requirements [RB, SSS; SRR].
c. Environmental constraints, including the operating environment (e.g. drop, shock, vibration, extreme temperature, noise, exposure to toxic substances, confined space, fire, electrostatic discharge, lightning, electromagnetic effects, and ionizing and non-ionizing radiation).
a. Software unit tests traceability matrices [DJF, SVR; CDR];
b. Software unit testing verification report [DJF, SVR; CDR].
ECSS‐E‐ST‐40C
6 March 2009
<4.8> Risks
a. The SValP shall state (or refer to the SDP) all the identified risks to the software validation campaign.
b. Contingency plans shall be also included.
<5> Software validation tasks identification
a. The SValP shall describe the software validation tasks to be performed for the identified software items.
b. The SValP shall list which are the tasks and the items under tests, as well as the criteria to be utilized for the testing activities on the test items associated with the plan.
c. The SValP shall list the testing activities to be repeated when testing is resumed.
d. The SValP shall describe for each validation tasks the inputs, the outputs as well as the resources to be used for each task.
e. The detailed information and the data for the testing procedures shall be provided in the software validation testing specifications.
<6> Software validation approach
a. The SValP shall describe the overall requirements applicable to the software validation testing activities, providing for definition of overall requirements, guidelines on the kinds of tests to be executed.
b. The SValP shall describe the selected approach to accomplish validation of those software specification requirements to be validated by inspection and analysis or review of design.
c. The SValP shall define the regression testing strategy.
<7> Software validation testing facilities
a. This SValP shall describe the test environment to execute the software validation testing activity and the non–testing validation activities whose approach is defined by this plan.
b. The SValP shall describe the configuration of selected validation facilities in terms of software (e.g. tools and programs, and simulation), hardware (e.g. platforms and target computer), test equipment (e.g. bus analyser), communications networks, testing data and support software (e.g. simulators).
NOTE Reference to other documentation describing the facility can be done.
c. If the validation testing against the requirements baseline and the validation testing against the technical specification use different environments, this shall be clearly stated and described.
132
a. After completion of the software requirement analysis and architectural design, and the verification and validation processes implementation, a preliminary design review (PDR) shall take place.
AIM: To review compliance of the technical specification (TS) with the requirements baseline, to review the software architecture and interfaces, to review the development, verification and validation plans.
EXPECTED OUTPUT: Approved technical specification and interface, architecture and plans [TS, DDF, DJF, MGT; PDR].
Typical objectives of the software test readiness review (TRR) are: baseline of the testing, analysis, inspection or review of design (e.g. Software Validation Specification w.r.t. the technical specification or requirement baseline); baseline of the design documents; review of the integration and TS/RB‐validation facilities; review of the Unit Test Results; review of the testing facilities configuration; verify that software documentation, software code, procured software and support software and facilities are under proper configuration control; baseline the testing configuration; review the quality assurance reports; review the status of all SPRs and NCRs; and evaluation of readiness to proceed to testing.
2. Feasibility, presenting in gathering all the specific verification reports that have been planned to be provided w.r.t. the SVerP, including e.g.: o Software detailed design verification as per 5.8.3.4 o Design model checking (including behavioural verification as per 5.8.3.13b.) o Software code verification as per 5.8.3.5a. o Structural code coverage achievement. o Deactivated code verification as per ECSS‐Q‐ST‐80 6.2.6.5 o Configurable code verification as per ECSS‐Q‐ST‐80 6.2.6.6 o Source code robustness verification o Verification of software unit testing as per 5.8.3.6 o Verification of software integration as per 5.8.3.7 o Verification of software documentation as per 5.8.3.10 o Others specific inspections, analyses or review of design report (e.g. technical risks analysis, evaluation of reuse potential) o Others specific verification related to RAMS requirements (e.g. analysis reports using HSIA, SFTA, SFMECA).
<4.3.2> Feasibility
a. The SVR shall present in gathering all the specific verification reports that have been planned to be provided w.r.t. the SVerP, including e.g.:
⎯ Software requirements verification as per 5.8.3.2.
⎯ HMI evaluation by e.g. mock‐up as per ECSS‐E‐ST‐10‐11
⎯ Behavioural verification of the logical model and architectural design verification as per 5.8.3.13a. and b.
⎯ Verification of the software architectural and interface design as per 5.8.3.3.
⎯ Architectural design behavioural model checking
⎯ Verification of software documentation as per 5.8.3.10.
⎯ Other specific inspections, analyses or review of design report (e.g. numerical accuracy , technical risks analysis, evaluation of reuse potential)
⎯ Others specific verification related to RAMS requirements (e.g. analysis reports using HSIA, SFTA, SFMECA)
b. Requirements applicable to the following items shall be included:
1. software standards (e.g. applicable coding standards, and development standards);
2. design requirements;
3. specific design methods to be applied to minimize the number of critical software components (see ECSS‐Q‐ST‐80 6.2.2.4);
4. requirements relevant to numerical accuracy management;
5. design requirements relevant to the “in–flight modification” of the software item;
6. specific design requirements to be applied if the software is specified to be designed for intended reuse;
7. specific constraints induced by reused software (e.g. COTS, free software and open source).
NOTE 8 Typical objectives of the software qualification review (QR) are:
• To verify that the software meets all of its specified requirements, and in particular that verification and validation process outputs enable transition to ”qualified state” for the software products.
• Review of the RB‐validation test, analysis, inspection or review of design results, including as‐run procedures.
• Verification that all the Requirements Baseline and interfaces requirements have been successfully validated and verified (including technical budgets and code coverage).
• Review the software release document.
• Review of the acceptance facilities configuration.
1. The system model philosophy (e.g. proto‐flight model, versus utilization of engineering qualification model)
2. The system verification and qualification approach and constraints
3. The capability to baseline the system design at system CDR, by knowing enough information about software design, in particular consolidated sizing and timing budgets, consistent hardware design and software design.
5.2.2.2 Identification of observability requirements
a. The customer shall specify all software observability requirements to monitor the software behaviour and to facilitate the system integration and failure investigation.
EXPECTED OUTPUT: System and software observability requirements [RB, SSS; SRR].
5.3.5.2 Test review board
a. The test review board (TRB) shall approve test results at the end of test activities, as defined in the software development plan.
EXPECTED OUTPUT: Approved test results[DJF; TRB]
a. As support to the verification of the software requirements, the supplier shall verify the software behaviour using the behavioural view of the logical model produced in 5.4.2.3c.
EXPECTED OUTPUT: Software behaviour verification [DJF, SVR; PDR].
— To review the design justification file, including the completeness of the software unit testing, integration and validation with respect to the technical specification.
EXPECTED OUTPUT: Approved design definition file and design justification file [DDF, DJF; CDR].
5.10.6.5 Notification of transition to migrated system
a. When the scheduled migration takes place, notification shall be sent to all parties involved.
EXPECTED OUTPUT: Migration notification [MF, ‐ ; ‐ ].
b. All associated old environment’s documentation, logs, and code shall be placed in archives.
EXPECTED OUTPUT: Migration notification [MF, ‐ ; ‐ ].
5.2.4.7 Development of software to be reused
a. The customer shall specify the reusability requirements that apply to the development, to enable the future reuse of the software (including models used to generate the software), or customization for mission (e.g. in a family of spacecraft or launcher). EXPECTED OUTPUT: Requirements for ’software to be reused’ [RB, SSS; SRR].

1. Read the provided Scenario Description carefully and understand the application scenario.
2. Identify related content from the provided Requirements Description and Domain Standards.
3. Structure the response in sections. Make sure to use language that a systems or requirements analyst can directly map to their documentation process.
