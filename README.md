# Email Header Analyzer

This project is a simple tool for analyzing raw email headers. It is designed to help SMEs and beginner security teams identify possible phishing attempts by:

- Detecting failed SPF and DKIM checks
- Displaying the email delivery path via mail server hops

## How to Use

1. Copy the full email header from any suspicious email and paste it into a file named `sample-header.txt`.
2. Run the Python script using the command:

   python analyzer.py

3. Review the output in the terminal to see any warnings or anomalies.

## Example Output

- SPF or DKIM failure warnings
- Mail servers the email passed through

## Requirements

- Python 3.x installed
- No additional packages needed

## Author

Victor Ekere – Cybersecurity Analyst and Founder of Secure Path  
https://secure-path.io
on analyzer.py
