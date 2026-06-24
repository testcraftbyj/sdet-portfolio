#Day 1
#Problem 1:
name= "Jay"
years_of_experience = 13
job_searching = True

print("Name:", name)
print("Years of Experience:", years_of_experience)
print("Job Searching:", job_searching)

test_case_id = "TC_001"
status = "Passed"

print("Test Case", test_case_id, "status:", status)


#Problem 2:
total_tests = int(input("Enter total number of tests: "))
passed_tests = int(input("Enter number of passed tests: "))

if total_tests== 0:
    print("Error: Total tests cannot be zero.")
else:
    pass_percentage = (passed_tests / total_tests) * 100
    print("Pass Percentage:", pass_percentage, "%")
    if pass_percentage >= 80:
        print("Build: PASSED")
    else:    
        print("Build: FAILED")


status = input("Enter test status (Passed/Failed): ")
if status == "Passed":
    print("Test passed!")
elif status == "Failed":
    print("Test  failed - investigate")
else:    
    print("Invalid status entered")



#Loops

test_cases = ["TC_101", "TC_102", "TC_103", "TC_104", "TC_105"]

for test_case in test_cases:
    print("Running test case:", test_case)



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



attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print("Retry attempt:", attempts + 1)
    attempts += 1

print("Max retries reached - marking as failed")

