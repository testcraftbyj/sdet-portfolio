#Day 3 - Object-Oriented Programming (OOP) and Classes
class TestCase:
    def __init__(self, test_id, name, status):
        self.test_id = test_id
        self.name = name
        self.status = status

    def summary(self):
        return f"{self.test_id} - {self.name} - Status: {self.status}"

    def retry(self):
        if self.status == "Failed":
            self.status = "Pending"

tc1 = TestCase("TC_001", "Login Test", "Failed")
tc1.retry()
print(tc1.summary())


tc2 = TestCase("TC_002", "Login Test 2", "Passed")
print(tc2.summary())


class TestSuite:
    def __init__(self):
        self.test_cases = []

    def add_test(self, test_case):
        self.test_cases.append(test_case)

    def count_passed(self):
        count_passed = 0
        for test_case in self.test_cases:
            if test_case.status == "Passed":
                count_passed += 1
        return count_passed

suite = TestSuite()
suite.add_test(TestCase("TC_001", "Login Test", "Failed"))
suite.add_test(TestCase("TC_002", "Login Test 2", "Passed"))
suite.add_test(TestCase("TC_003", "Signup Test", "Passed"))
print("Total Passed:", suite.count_passed())