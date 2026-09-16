import csv
from collections import Counter

# Read the security log file
with open("sample_logs/security_events.csv", "r") as file:
    logs = csv.DictReader(file)

    # Store failed login attempts
    failed_logins = []

    for log in logs:
        if log["event_id"] == "4625":
            failed_logins.append(log)

# Count failed login attempts from each IP address
ip_counts = Counter(log["source_ip"] for log in failed_logins)

# Detection threshold
THRESHOLD = 5

print("=== Brute Force Detection Report ===")

for ip, count in ip_counts.items():
    if count >= THRESHOLD:
        print("\nALERT: Possible brute-force activity detected")
        print(f"Source IP: {ip}")
        print(f"Failed login attempts: {count}")
        print("Event ID: 4625")
