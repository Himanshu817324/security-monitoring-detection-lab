# Detection Rules

## Brute-Force Authentication Detection
Trigger an alert when:
- More than 5 failed login attempts
- From the same IP address
- Within a 2-minute window

## Malware Activity Detection
Trigger an alert when:
- Known malware hash or EICAR test file is detected
- Endpoint antivirus generates an alert

## Suspicious Network Traffic
Trigger an alert when:
- Outbound connections to known malicious IPs
- Unusual traffic volume outside business hours
