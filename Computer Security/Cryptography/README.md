ECEN 4133 - Computer Security Fundamentals Project
Cryptography
This project was completed as part of the course ECEN 4133, focusing on exploring vulnerable applications of cryptography. Divided into two main parts, the project delves into various cryptographic concepts, attacks, and techniques.

Project Objectives
  - Understand common pitfalls in cryptographic implementations.
  - Investigate vulnerabilities in hash functions such as MD5 and SHA-1.
  - Explore the length extension vulnerability in hash functions.
  - Conduct cryptanalysis using frequency analysis on a Vigenère Cipher.
  - Exploit a padding oracle attack in Cipher-Block Chaining (CBC) mode.

The project comprises two major parts:

  Part 1: Cryptographic Vulnerabilities
    - Length Extension: Demonstrates the vulnerability in hash functions and explores how to exploit length extension attacks.
    - Hash Collisions: Investigates MD5 collisions and the potential vulnerabilities they pose.
    - Vigenère Cipher Analysis: Utilizes frequency analysis to break a Vigenère Cipher.
    
  Part 2: Cryptanalysis Techniques
    - Solving Vigenère Ciphers: Implements a program to decrypt Vigenère ciphers using known cryptanalysis techniques.

Files Included
  - len_ext_attack.py: Script to exploit length extension vulnerability.
  - good.py and evil.py: Programs demonstrating MD5 hash collisions.
  - vigenere.py: Script to decrypt Vigenère ciphers.
  - padding_oracle.py (Graduate Students): Script to exploit padding oracle attacks.
