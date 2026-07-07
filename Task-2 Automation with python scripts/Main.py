import re

# Open and read the input file
with open("input.txt", "r") as file:
    text = file.read()

# Regular expression to find email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extract all email addresses
emails = re.findall(email_pattern, text)

# Save the extracted emails to a new file
with open("extracted_emails.txt", "w") as file:
    if emails:
        for email in emails:
            file.write(email + "\n")
    else:
        file.write("No email addresses found.")

# Display the result
print("===== Email Address Extractor =====")

if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)

    print("\nTotal Emails Extracted:", len(emails))
    print("Saved successfully to extracted_emails.txt")
else:
    print("No email addresses found.")