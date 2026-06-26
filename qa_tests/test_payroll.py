def calculate_salary(base_pay, days_worked, overtime_hours, overtime_rate=1.5):
    if days_worked < 0 or overtime_hours < 0:
        raise ValueError("Days and overtime cannot be negative")
    if days_worked > 31:
        raise ValueError("Days worked cannot exceed 31 in a month")
    daily_rate = base_pay / 26
    regular_pay = daily_rate * days_worked
    overtime_pay = (daily_rate / 8) * overtime_rate * overtime_hours
    return round(regular_pay + overtime_pay, 2)

def test_normal_salary():
    result = calculate_salary(26000, 26, 0)
    assert result == 26000.0

def test_partial_month():
    result = calculate_salary(26000, 13, 0)
    assert result == 13000.0

def test_overtime_added():
    result = calculate_salary(26000, 26, 8)
    assert result > 26000

def test_negative_days_rejected():
    try:
        calculate_salary(26000, -5, 0)
        assert False, "Should have raised error"
    except ValueError:
        assert True

def test_negative_overtime_rejected():
    try:
        calculate_salary(26000, 26, -3)
        assert False, "Should have raised error"
    except ValueError:
        assert True

def test_zero_days_zero_salary():
    result = calculate_salary(26000, 0, 0)
    assert result == 0.0

def test_days_exceed_month():
    try:
        calculate_salary(26000, 35, 0)
        assert False, "Should have raised error"
    except ValueError:
        assert True

def test_overtime_only_no_regular():
    result = calculate_salary(26000, 0, 10)
    assert result > 0

def test_high_overtime_increases_pay():
    low = calculate_salary(26000, 26, 5)
    high = calculate_salary(26000, 26, 20)
    assert high > low

def test_salary_is_float():
    result = calculate_salary(26000, 15, 3)
    assert isinstance(result, float)