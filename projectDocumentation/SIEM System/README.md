# Continuous Threat Monitoring System

## Project Overview
This project, designed as part of the course **CS4612 - 01**, implements a **Continuous Threat Monitoring System**. It simulates monitoring and detection of multiple types of cyberattacks through real-time analysis of user input (text or files). The system detects patterns associated with common attacks and generates logs for any detected threats.

## Features
- **Continuous Monitoring**: The system continuously monitors user input, simulating potential cyberattacks.
- **Attack Detection**: The following attack types are monitored:
  - Buffer Overflows
  - Heap Overflows
  - Libc Attacks
  - Race Conditions
  - Shellshock Vulnerabilities
  - SQL Injection
  - String Format Attacks
  - Web-Based Attacks
- **Threat Classification**: The system classifies threats as either *suspicious activity* or an actual *attack* based on predefined patterns.
- **Logging**: Results are logged into a `log.txt` file, highlighting any suspicious or malicious activity.

## How It Works
The program operates in an infinite loop to simulate continuous monitoring. Users can input:
- **Text**: Simulates user-entered data, such as usernames or passwords.
- **Files**: Allows the user to input a file, which is then analyzed for suspicious activity or potential attacks.

Each cycle introduces a 5-second delay to mimic real-world continuous monitoring systems.

## Setup Instructions

### Requirements
- Java Development Kit (JDK) 8 or higher
- A terminal or command line interface

### How to Run
1. Clone or download the repository.
2. Compile the Java file:
    ```bash
    javac ContinuousMonitor.java
    ```
3. Run the program:
    ```bash
    java ContinuousMonitor
    ```
4. Follow the on-screen prompts to either:
   - Input a text string.
   - Provide a file path for file-based input.

### Files in the Project
- **Main Code**: `ContinuousMonitor.java`
- **Alert and Suspicious Files**: 
  - `BufferAlerts.txt`, `BufferSuspicious.txt`
  - `HeapAlerts.txt`, `HeapSuspicious.txt`
  - `LibcAlerts.txt`, `LibcSuspicious.txt`
  - `RaceAlerts.txt`, `RaceSuspicious.txt`
  - `ShellshockAlerts.txt`, `ShellshockSuspicious.txt`
  - `SQLAlerts.txt`, `SQLSuspicious.txt`
  - `StringFormatAlerts.txt`, `StringFormatSuspicious.txt`
  - `WebAlerts.txt`, `WebSuspicious.txt`

These files contain predefined patterns to identify suspicious activities or potential attacks based on the type of vulnerability.

## Log File
- **log.txt**: This file stores the results of the analysis, where:
  - Clean entries are marked as "Clean".
  - Suspicious activity or potential attacks are flagged with descriptions.

## Future Enhancements
- Integration of a more robust threat detection mechanism.
- Adding support for real-time web monitoring.
- Implementing advanced AI-based anomaly detection.
