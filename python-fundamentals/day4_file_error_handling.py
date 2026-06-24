"""
ValueError      # wrong type conversion ("abc" → int)
TypeError       # wrong type in operation ("text" + 5)
FileNotFoundError  # file doesn't exist
ZeroDivisionError  # dividing by zero
KeyError        # dictionary key doesn't exist
IndexError      # list index out of range
"""

try:
    value = int(input("Enter number of test cases: "))
    print("Test cases:", value)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")



def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: 0



try:
    numbers = [1, 2, 3]
    print(numbers[5])
    print("This line runs")
except IndexError:
    print("Index out of range")
finally:
    print("Always runs")



with open("test_results.txt", "w") as file:
    file.write("TC_001: Passed\n")
    file.write("TC_002: Failed\n")
    file.write("TC_003: Passed\n")
with open("test_results.txt", "r") as file:
    content = file.read()
    print(content)





try:
    with open("missing.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")



def log_result(test_id, status):
    try:
        with open("test_log.txt", "a") as file:
            file.write(f"{test_id}: {status}\n")
            
    except Exception as e:
        print("Error writing to file:", e)

log_result("TC_001", "Passed")
log_result("TC_002", "Failed")        
log_result("TC_003", "Passed")

with open("test_log.txt", "r") as file:
    print(file.read())