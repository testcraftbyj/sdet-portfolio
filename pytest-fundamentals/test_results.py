import pytest


@pytest.fixture
def test_suite():
    return [
        {"id": "TC_001", "status": "Passed"},
        {"id": "TC_002", "status": "Failed"},
        {"id": "TC_003", "status": "Passed"}
    ]

def test_suite_length(test_suite):
    assert len(test_suite) == 3

def test_count_passed(test_suite):
    passed_count = sum(1 for test in test_suite if test["status"] == "Passed")
    assert passed_count == 2

def test_all_have_ids(test_suite):
    for test in test_suite:
        assert "id" in test
