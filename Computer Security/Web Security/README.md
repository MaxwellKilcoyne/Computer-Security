Overview:
This project, assigned for ECEN 4133, involves assessing the security vulnerabilities of a web application called BUNGLE! The primary aim is to exploit three common classes of vulnerabilities: SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF) on the provided website. The project also involves testing flawed defenses implemented by the developers to understand their limitations and security implications.

Objectives:

  - Identify and exploit common vulnerabilities (SQL injection, XSS, CSRF) in a web application.
  - Analyze the risks associated with these vulnerabilities and comprehend the shortcomings of inadequate defenses.
  - Gain practical experience in web architecture and programming languages like HTML, JavaScript, and SQL.
  - 
Requirements:

  - Understanding of web application architecture and basic programming skills in HTML, JavaScript, and SQL.
  - Compliance with ethical guidelines, respecting privacy, and adhering to university policies.
  
Target Website: https://project2.ecen4133.org/
  The project focuses on assessing the security of BUNGLE!, a web search engine written in Python using the Bottle web framework. The site includes features like search functionality, user logins, and tracking of search       history in a MySQL database.

Project Parts:

  - SQL Injection: Exploit vulnerabilities in different defense scenarios by executing SQL injection attacks against login forms with varying levels of defenses.
  - Cross-site Scripting (XSS): Demonstrate XSS attacks on the BUNGLE! search box, bypassing different defense mechanisms, and executing specific payloads.
  - Cross-site Request Forgery (CSRF): Exploit CSRF vulnerabilities against login forms to surreptitiously log victims into an attacker-controlled account.

Part 1: SQL Injection
  - sql_0.txt, sql_1.txt, sql_2.txt: These text files contain strings provided by the server when your SQL injection exploits work against different defense levels. Each file corresponds to a different defense level.

Part 2: Cross-site Scripting (XSS)
  - xss_payload.html: Specifically for the "No defenses" level, this file contains the human-readable (non-URL-encoded) payload code used to execute the XSS attack.
  - xss_0.txt, xss_1.txt, xss_2.txt, xss_3.txt: These text files should contain URLs that, when loaded in a browser, immediately execute the specified XSS attack against different defense levels.

Part 3: Cross-site Request Forgery (CSRF)
  - csrf_0.html, csrf_1.html: These HTML files should execute the specified CSRF attacks against different defense levels when loaded in a victim's browser.
