## Postmortem Report: Incident - Blocking Ports 80 and 443

### Incident Summary:

**Duration:** The incident occurred from 10:30 AM to 12:45 PM (EAT).

**Impact:** The incident resulted in the inaccessibility of our websites. Users experienced connection errors, with approximately 80% of our visitors affected.

**Root Cause:** The root cause of the incident was a misconfiguration in our server's firewall settings, blocking incoming traffic on ports 80 and 443.

### Timeline:

- **10:30 AM (EAT):** Issue Detected
  - The issue was initially detected by our monitoring system, which sent alerts about a sudden drop in web server response times.

- **10:35 AM (EAT):** Investigation Initiated
  - Our operations team began investigating the issue, assuming it might be related to server load or network congestion.

- **10:50 AM (EAT):** Misleading Paths
  - Initial investigation showed no signs of excessive server load or network issues, leading to an assumption that the problem might be within the application code.

- **11:15 AM (EAT):** Escalation to the Network Team
  - As the issue remained unresolved, it was escalated to the network team, which began analyzing network logs.

- **11:45 AM (EAT):** Firewall Misconfiguration Detected
  - The network team identified that the server's firewall was incorrectly configured, blocking incoming traffic on ports 80 and 443.

- **12:00 PM (EAT):** Issue Resolution
  - Corrective measures were taken to reconfigure the firewall to allow traffic on ports 80 and 443, and the web server started serving requests normally.

### Root Cause and Resolution:

**Root Cause:** The incident was caused by a misconfiguration in the server's firewall settings, which erroneously blocked incoming traffic on ports 80 and 443. This misconfiguration was likely introduced during recent maintenance.

**Resolution:** The issue was resolved by reconfiguring the server's firewall to allow incoming traffic on ports 80 and 443. Verification tests confirmed that web services were functioning correctly after the configuration change.

### Corrective and Preventative Measures:

**Improvements:**
1. **Automated Testing:** Implement automated testing procedures to periodically validate the firewall settings, ensuring that they align with the desired configurations.

2. **Change Management:** Enhance the change management process to include a thorough review of any system configuration changes to prevent such misconfigurations in the future.

**Tasks:**
1. **Automate Firewall Auditing:** Develop scripts to automatically audit and report on the state of firewall rules, with specific checks for ports 80 and 443.

2. **Documentation Update:** Maintain comprehensive documentation of server configurations, emphasizing firewall settings, for reference during maintenance.

This incident report serves as a learning experience, reinforcing the importance of rigorous change management and automation in maintaining a robust and reliable system.

