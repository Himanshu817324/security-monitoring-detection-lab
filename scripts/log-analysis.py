# Simple log analysis script to detect brute-force activity

failed_attempts = {}
threshold = 5

with open("sample-logs.txt", "r") as file:
    for line in file:
        if "Failed login attempt" in line:
            ip = line.split("from")[-1].strip()
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"[ALERT] Possible brute-force attack from {ip} ({count} attempts)")
