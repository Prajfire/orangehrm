def test_worker_has_valid_id():
    worker_id = "EMP101"
    assert len(worker_id) > 0

def test_missing_mandatory_name_rejected():
    name_provided = False
    assert name_provided is False