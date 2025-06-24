# analyzer.py

def analyze_email_header(header_text):
    print("Analyzing email header...\n")

    # Check SPF and DKIM results
    if "spf=fail" in header_text.lower():
        print("Warning: SPF check failed – this could be a spoofed sender.")
    if "dkim=fail" in header_text.lower():
        print("Warning: DKIM check failed – the sender's identity may not be verified.")

    # Extract all 'Received: from' entries to show mail server hops
    print("\nMail servers used in the delivery path:")
    for line in header_text.splitlines():
        if line.lower().startswith("received: from"):
            print("  -", line.strip())

    print("\nAnalysis complete.")

if __name__ == "__main__":
    try:
        with open("sample-header.txt", "r") as file:
            header_content = file.read()
            analyze_email_header(header_content)
    except FileNotFoundError:
        print("Error: sample-header.txt not found.")
