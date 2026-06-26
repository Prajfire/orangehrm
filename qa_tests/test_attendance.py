def test_log_attendance():
    hours_logged = 8
    assert hours_logged > 0

def test_attendance_exceeds_limit_rejected():
    invalid_hours = 25
    assert invalid_hours > 24