# Incident Report: Brute-Force Attack

## Summary
Multiple failed authentication attempts were detected from a single IP address,
indicating a possible brute-force attack.

## Timeline
- 10:15:32 – First failed login attempt detected
- 10:15:38 – Multiple failures observed
- 10:16:01 – Successful login detected

## Impact
- Potential unauthorized access to administrative account

## Mitigation
- Blocked source IP address
- Reset affected account password
- Enabled account lockout policies

## MITRE ATT&CK Mapping
- T1110: Brute Force
