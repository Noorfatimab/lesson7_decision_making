# decision_checker.py
# Lesson 7: Making Decisions with if / elif / else

def check_number(num):
    if num > 0:
        return "The number is positive"
    elif num < 0:
        return "The number is negative"
    else:
        return "The number is zero"

def main():
    num = int(input("Enter a number: "))
    result = check_number(num)
    print(result)

main()
 
