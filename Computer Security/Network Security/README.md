Overview:
  The Network Security Project 3 for ECEN 4133 involves practical exercises and demonstrations in core network protocols, traffic analysis, and various local network attacks. The project provided me with exposure to       network attack methodologies, network traffic analysis, and detecting security threats programmatically.

Objectives:
  - Gain exposure to fundamental network protocols and concepts.
  - Learn offensive techniques used in local network attacks.
  - Apply manual and automated traffic analysis to identify security vulnerabilities.
  
Part 1: Network Attacks:
   This part of the project experiments with network attacks by intercepting an HTTP connection to a controlled website, manipulating its content, and replacing specific data. The task involves manipulating a Python program     (attack.py)    to watch and modify requests to freeaeskey.xyz, altering the AES256 key retrieved by the website's program without modifying the getkey.py script.

Part 2: Anomaly Detection:
  This portion of the project requires the development of a Python program (detector.py) that programmatically analyzes trace data (PCAP files) to identify suspicious behavior related to SYN scans. The goal is to detect       potential port scanning activities by comparing the number of SYN packets sent to the number of SYN+ACK packets received.

Part 1:
  - attack.py: Python script executing the specified network attack.
  
Part 2:
  - detector.py: Python program identifying SYN scan activities in PCAP files.
