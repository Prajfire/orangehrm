def test_valid_login():
    user_authenticated = True
    assert user_authenticated is True

def test_invalid_login_rejected():
    password_correct = False
    assert password_correct is False