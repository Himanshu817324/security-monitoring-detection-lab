# Security Monitoring & Detection Lab

## Overview
This project simulates an enterprise security monitoring environment to detect
and investigate common cyber attacks using SIEM and network monitoring tools.

The lab focuses on log ingestion, alert creation, and incident analysis
similar to a real SOC environment.

## Tools Used
- SIEM: ELK Stack / Splunk
- Network Monitoring: Zeek / Suricata
- Operating Systems: Windows, Linux, Kali Linux
- Visualization: SIEM dashboards

## Lab Architecture
- Windows endpoint generating authentication logs
- Linux server generating system logs
- Network traffic monitored via IDS
- Central SIEM collecting and correlating logs

## Attack Scenarios
- Brute-force authentication attempts
- Malware activity (EICAR test file)
- Suspicious network traffic patterns

## Detections
- Excessive failed logins
- Suspicious outbound traffic
- Malware hash detection


## Key Learnings
- Log correlation across multiple sources
- Writing detection logic
- Identifying attack patterns from logs
- SOC-style incident documentation


## Outcome
Created dashboards and alerts for real-time monitoring.

<img width="1858" height="944" alt="dashboard" src="https://github.com/user-attachments/assets/8119f6b4-db8e-4c87-9f3b-9588ea8c83e6" />
