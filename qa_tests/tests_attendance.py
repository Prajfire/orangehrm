def validate_attendance(worker_id, days_present, overtime_hours):
    if not worker_id or worker_id.strip() == "":
        raise ValueError("worker ID cannot be empty")
    if days_present < 0:
        raise ValueError("days present cannot be negative")
    if days_present > 1:
        raise ValueError("only 1 day per attendance entry")
    if overtime_hours < 0:
        raise ValueError("overtime cannot be negative")
    if overtime_hours > 12:
        raise ValueError("overtime cannot exceed 12 hours per day")
    return True


def test_normal_attendance_entry_works():
    result = validate_attendance("WKR001", 1, 2)
    assert result == True


def test_empty_worker_id_rejected():
    # if worker ID is empty we don't know who this is for
    try:
        validate_attendance("", 1, 0)
        assert False
    except ValueError:
        pass


def test_negative_days_rejected():
    try:
        validate_attendance("WKR001", -1, 0)
        assert False
    except ValueError:
        pass


def test_more_than_one_day_per_entry_rejected():
    # each entry is for a single day — 3 days in one entry is an error
    try:
        validate_attendance("WKR001", 3, 0)
        assert False
    except ValueError:
        pass


def test_negative_overtime_rejected():
    try:
        validate_attendance("WKR001", 1, -2)
        assert False
    except ValueError:
        pass


def test_overtime_over_12_hours_rejected():
    # physically impossible to work 15 overtime hours in one day
    try:
        validate_attendance("WKR001", 1, 15)
        assert False
    except ValueError:
        pass


def test_absent_day_with_zero_overtime_is_valid():
    result = validate_attendance("WKR002", 0, 0)
    assert result == True


def test_present_day_with_zero_overtime_is_valid():
    result = validate_attendance("WKR003", 1, 0)
    assert result == True
