# Indicators of Compromise (IOCs)

## Observed Indicators

| Indicator | Value | Significance |
|---|---|---|
| Source IP | 10.10.10.50 | Generated repeated failed login attempts |
| Event ID | 4625 | Windows failed logon event |
| Target Account | Administrator | Privileged account targeted |
| Failed Attempts | 7 | Exceeded the detection threshold |

## IOC Assessment

The source IP `10.10.10.50` is the primary indicator identified in this simulated investigation.

The repeated Event ID 4625 failures from the same source IP indicate suspicious authentication activity.

> **Note:** The data in this project is simulated for learning and demonstration purposes. The IP address is not treated as a confirmed malicious indicator without additional investigation.
