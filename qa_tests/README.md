# My QA Test Files

These are the test files I wrote for the DeepThought QA Engineer assignment.

I chose to focus on the payroll calculation and attendance validation
because mistakes in those two areas directly affect what the worker
gets paid at the end of the month. The worker is the most vulnerable
person in this system — they cannot fix a payroll error themselves.

## Files here
- test_payroll.py — 12 tests for salary calculation logic
- test_attendance.py — 8 tests for attendance entry validation

## How to run my tests
pip install pytest
pytest -v

## What I was mainly checking
Does the system reject wrong inputs before they reach the
payslip? Like — what if the site manager types -5 in the
overtime field? What if he enters 35 days for a 30-day month?
The system should catch those, not silently produce a wrong number.

## What I would add next
UI tests using Selenium to test the actual input fields in
the browser, not just the Python logic layer.
