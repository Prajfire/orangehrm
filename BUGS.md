## Bug #1: System accepts negative overtime hours

**Severity:** High
**Found in:** Attendance entry form

### I noticed this while going through the attendance entry form as a site manager - there is no check stopping someone from typing a negative number in the overtime field.
**Steps to reproduce:**
1. Login as Site Manager
2. Go to Attendance Entry
3. Enter -5 in the Overtime Hours field
4. Click Save

**Expected result:** System should reject the input and show error "Overtime cannot be negative"
**Actual result:** System saves -5 overtime hours without any error
**Impact:** Worker's salary will be calculated as LESS than actual, causing underpayment. Worker loses money.

---

## Bug #2: No validation when days worked exceeds month length

**Severity:** High
**Found in:** Monthly attendance summary

### I was checking monthly attendance and realised nothing stops you from entering 35 days worked for a month that only has 30 days.
**Steps to reproduce:**
1. Login as HR
2. Open attendance for any worker
3. Manually enter 35 days worked for a 30-day month
4. Save

**Expected result:** Error - "Days worked cannot exceed 30 for this month"
**Actual result:** System accepts 35 days and calculates inflated salary
**Impact:** Company overpays worker due to data entry error. Financial loss.

---

## Bug #3: Payslip generated for deactivated worker

**Severity:** Medium
**Found in:** Payroll generation

### I deactivated a test worker and then ran payroll, and was surprised to see a payslip still got generated for them.
**Steps to reproduce:**
1. Deactivate a worker from the system
2. Run monthly payroll
3. Check generated payslips

**Expected result:** No payslip should be generated for deactivated workers
**Actual result:** Payslip is still generated for the deactivated worker
**Impact:** Ghost payroll - company might pay someone who no longer works there.

---

## Bug #4: Overtime rate is not configurable - hardcoded as 1.5x

**Severity:** Medium
**Found in:** Payroll settings

### I looked for a place to change the overtime multiplier in settings and couldn't find one - it seems the 1.5x rate is just hardcoded in.
**Steps to reproduce:**
1. Login as Admin
2. Go to Payroll Settings
3. Try to change overtime multiplier

**Expected result:** Admin should be able to set overtime rate (some companies pay 2x)
**Actual result:** No setting exists - overtime is always 1.5x, non-configurable
**Impact:** Companies with different overtime policies cannot use this system correctly.

---

## Bug #5: No audit log when attendance is edited after submission
**Severity:** High
**Found in:** Attendance management

### I edited an attendance entry after it was submitted and there was no record of who changed it or when - the change just happened silently.
**Steps to reproduce:**
1. Site Manager submits attendance for a worker
2. HR edits the attendance after submission
3. Check audit/history log

**Expected result:** Full audit trail showing who changed what and when
**Actual result:** No change history recorded - edits happen silently
**Impact:** If a worker is underpaid due to edited attendance, there is no way to prove who made the change. Legal and ethical risk.
