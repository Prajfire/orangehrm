# test_payroll.py 
# Written for DeepThought QA Engineer assignment
# I tested the payroll calculation because if the numbers
# are wrong, the daily wage worker gets less money that month.
# That is the real impact so this is where I focused.

def calculate_salary(base_pay, days_worked, overtime_hours, overtime_rate=1.5):
    if days_worked < 0 or overtime_hours < 0:
        raise ValueError("days and overtime cannot be negative")
    if days_worked > 31:
        raise ValueError("days worked cannot exceed 31")
    if base_pay <= 0:
        raise ValueError("base pay must be more than zero")
    daily_rate = base_pay / 26
    regular_pay = daily_rate * days_worked
    overtime_pay = (daily_rate / 8) * overtime_rate * overtime_hours
    return round(regular_pay + overtime_pay, 2)


def test_full_month_attendance_full_salary():
    # worker came all 26 working days, should get full salary
    result = calculate_salary(26000, 26, 0)
    assert result == 26000.0


def test_half_month_attendance_half_salary():
    # 13 days out of 26 should give exactly half
    result = calculate_salary(26000, 13, 0)
    assert result == 13000.0


def test_overtime_makes_salary_higher():
    # overtime should always increase pay above base amount
    result = calculate_salary(26000, 26, 8)
    assert result > 26000


def test_negative_overtime_must_be_rejected():
    # I noticed the form has no check on overtime field
    # someone can type -5 and it would silently reduce salary
    # this test checks that the calculation layer rejects it
    try:
        calculate_salary(26000, 26, -3)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_negative_days_must_be_rejected():
    # same problem exists for days field
    # -5 days should never be accepted
    try:
        calculate_salary(26000, -5, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_worker_who_came_zero_days_gets_zero():
    # absent the whole month means zero salary
    result = calculate_salary(26000, 0, 0)
    assert result == 0.0


def test_days_above_31_must_be_rejected():
    # no month has more than 31 days
    # someone entering 45 days is clearly a mistake
    try:
        calculate_salary(26000, 45, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_zero_base_pay_is_not_allowed():
    # base pay of 0 makes no mathematical sense here
    try:
        calculate_salary(0, 26, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_more_overtime_means_more_pay():
    # basic sanity check — 20 hours OT should earn more than 5 hours
    low = calculate_salary(26000, 26, 5)
    high = calculate_salary(26000, 26, 20)
    assert high > low


def test_result_is_rounded_to_two_decimal_places():
    # payslips show rupees and paise — result must be 2 decimal places
    result = calculate_salary(15000, 17, 3)
    assert result == round(result, 2)


def test_higher_base_pay_gives_higher_salary():
    # two workers different base pay, same attendance — different salaries
    worker_a = calculate_salary(20000, 20, 0)
    worker_b = calculate_salary(35000, 20, 0)
    assert worker_b > worker_a


def test_overtime_without_attendance_still_pays():
    # edge case I thought about — what if worker is marked absent
    # but overtime hours were accidentally entered
    result = calculate_salary(26000, 0, 8)
    assert result > 0
