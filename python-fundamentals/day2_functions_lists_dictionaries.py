#Day 2
def is_test_passed(status):
    if status == "passed":
        return True
    else:
        return False
    
print(is_test_passed("passed"))  # Output: True
print(is_test_passed("failed"))  # Output: False


def is_test_passed(status):
    return status == "passed"

print(is_test_passed("passed"))  # Output: True
print(is_test_passed("failed"))  # Output: False



def calculate_pass_percentage(passed, total):
    if total == 0:
        return 0
    else:
        pass_percentage = (passed / total) * 100
        return pass_percentage

print(calculate_pass_percentage(17, 20))  # Output: 80.0


def calculate_pass_percentage(passed, total):
    if total == 0:
        return 0
    pass_percentage = (passed / total) * 100
    return pass_percentage

print(calculate_pass_percentage(17, 20))  


test_results = ["Passed",  "Failed", "Passed", "Passed", "Failed"]

total_passed = 0
total_failed = 0

for result in test_results:
    if result == "Passed":
        total_passed += 1
    else:
        total_failed += 1

print("Total Passed:", total_passed)
print("Total Failed:", total_failed)


def count_results(results):
    total_passed = 0
    total_failed = 0

    for result in results:
        if result == "Passed":
            total_passed += 1
        else:
            total_failed += 1
    return total_passed, total_failed

test_result = ["Passed",  "Failed", "Passed"]
total_passed, total_failed = count_results(test_result)
print("Total Passed:", total_passed)
print("Total Failed:", total_failed)


test_case = {
    "id": "TC_001",
    "name": "Login Test",
    "status": "Passed",
    "priority": "High"
}

#print(test_case["id"], "(", test_case["name"], ") - Status:", test_case["status"], ", Priority:", test_case["priority"])
print(f"{test_case['id']} ({test_case['name']}) - Status: {test_case['status']}, Priority: {test_case['priority']}")



test_suite = [
    {"id": "TC_001", "status": "Passed"},
    {"id": "TC_002", "status": "Failed"},
    {"id": "TC_003", "status": "Passed"}
]

for test_case in test_suite:
    if test_case["status"] == "Failed":
        print(f"{test_case['id']} - Status: {test_case['status']}")
              
def count_by_status(test_suite):
    passed_count = 0
    failed_count = 0
    for test_case in test_suite:
        if test_case["status"] == "Passed":
            passed_count += 1
        else:
            failed_count += 1

    return passed_count, failed_count

passed, failed = count_by_status(test_suite)
print("Total Passed:", passed)
print("Total Failed:", failed)