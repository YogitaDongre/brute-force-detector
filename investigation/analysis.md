# Brute-Force Investigation

## Alert Summary

A possible brute-force login attack was identified from repeated Windows failed login events.

- **Event ID:** 4625
- **Source IP:** 10.10.10.50
- **Target Account:** Administrator
- **Failed Attempts:** 7
- **Data Source:** Windows Security Event Log
- **Status:** Possible brute-force activity

## Investigation

The security log was reviewed for repeated Event ID 4625 failures.

Seven failed login attempts were observed from the same source IP address, targeting the Administrator account.

The repeated failures occurred within a short time period, which is consistent with possible password-guessing or brute-force activity.

## Analyst Assessment

The activity is considered **suspicious** based on:

1. Multiple failed authentication attempts.
2. Same source IP generating the failures.
3. Same privileged account being targeted.
4. Repeated Event ID 4625 events within a short period.

Further investigation would be required to determine whether the activity was malicious or legitimate.

## Recommended Investigation Steps

- Check whether the source IP belongs to an authorized system.
- Review successful login events following the failures.
- Check other accounts targeted by the same source IP.
- Review endpoint and network activity from the source system.
- Determine whether account lockout occurred.
- Escalate if malicious activity is confirmed.
