def calculate_pass_percentage(passed, total):
    if total == 0:
        return 0
    return (passed / total) * 100

def test_pass_percentage_normal():
    assert calculate_pass_percentage(8, 10) == 80.0

def test_pass_percentage_zero_total():
    assert calculate_pass_percentage(0, 0) == 0

def test_pass_percentage_all_passed():
    assert calculate_pass_percentage(5, 5) == 100.0

def test_pass_percentage_partial():
    assert calculate_pass_percentage(3, 4) == 75.0

def test_pass_percentage_none_passed():
    assert calculate_pass_percentage(0, 10) == 0.0