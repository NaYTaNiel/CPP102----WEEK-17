# Test Cases – Simulated Device Monitoring and Alert System
 
**Tested by:** Nathaniel Sios-e Panganiban        **Date:** October 17, 2026.
 
| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29. | Five readings displayed correctly | Pass. |
| TC02 | Choose 2, enter 33 | “Reading added successfully.” | Reading added successfully | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged. | Rejected; list unchanged | Pass. |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged. | Rejected; list unchanged | Pass. |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged. | Rejected; list unchanged | Pass. |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING. | 30 °C -> WARNING | Pass. |
| TC07 | Choose 3 | 35 °C -> WARNING | 35 °C -> WARNING | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED. | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Pass. |
| TC09 | Enter 9 | Error message; menu shown again. | Error message; menu shown again | Pass. |
| TC10 | Choose 5 | Exit message; program ends. | Exit message; program ends | Pass. |
 
## Bugs Found and Fixed
- **Boundary Condition Bug:** Initially, a boundary check evaluated values strictly with `<` instead of `<=`, causing 35 °C to fall into the critical category instead of warning. This was fixed by updating `classify_reading` to use `<= 35`.
- 
