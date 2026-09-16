# Brute Force Login Detection

## Project Overview

This project demonstrates a SOC-style detection and investigation workflow for identifying potential Windows brute-force login activity.

The project analyzes simulated Windows Security Event ID 4625 logs, identifies repeated failed authentication attempts, extracts relevant indicators, and maps the observed behavior to MITRE ATT&CK.

## SOC Workflow

**Monitor → Detect → Triage → Investigate → Map → Document**

## Detection

- Windows Security Event ID: 4625
- Activity: Failed authentication attempts
- Detection focus: Multiple failed logins from the same source IP
- Data source: Simulated Windows Security logs

## Investigation

The investigation focuses on:

- Source IP address
- Target username
- Number of failed attempts
- Event timestamps
- Repeated authentication failures
- Potential brute-force behavior

## MITRE ATT&CK

- T1110 — Brute Force
- T1110.001 — Password Guessing

## Indicators of Compromise (IOCs)

The project records relevant indicators identified during investigation, including:

- Source IP addresses
- Target usernames
- Event IDs
- Suspicious authentication activity

## Project Structure

```text
brute-force-detector/
├── README.md
├── sample_logs/
├── investigation/
├── detection/
├── iocs/
└── mitre/
