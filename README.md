# My QA Test Suite
I forked this OrangeHRM repository for my QA assignment. I created a new folder called qa_tests and wrote custom Python tests to make sure the payroll calculations calculate salaries properly and the attendance entry handles wrong or negative values correctly. I also documented 5 functional bugs I discovered in BUGS.md.
---

## Files
- test_payroll.py - 12 tests for salary calculation logic
- test_attendance.py - 8 tests for attendance entry validation

## How to run
pip install pytest
pytest -v

## What I was checking
Mainly: does the system reject wrong inputs before they reach the payslip calculation? Things like negative overtime, days exceeding the month, zero base pay, empty worker IDs.

## What I would add with more time
UI-level tests using Selenium to test the actual form fields in the browser, not just the backend calculation logic.