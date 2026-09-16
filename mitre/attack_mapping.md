# MITRE ATT&CK Mapping

## Observed Technique

| Technique | ID | Evidence |
|---|---|---|
| Brute Force | T1110 | Multiple failed login attempts from the same source IP |
| Password Guessing | T1110.001 | Repeated authentication failures targeting the Administrator account |

## Analysis

The simulated security logs show repeated failed authentication attempts against the Administrator account.

Seven Event ID 4625 events were generated from the same source IP address within a short period.

This behavior is consistent with the MITRE ATT&CK **Brute Force (T1110)** technique.

The activity may also align with **Password Guessing (T1110.001)** because repeated authentication attempts were observed against an account.

## Analyst Note

MITRE ATT&CK mapping describes the observed behavior. It does not by itself confirm that the activity was malicious.

Additional evidence should be reviewed before confirming an attack.
