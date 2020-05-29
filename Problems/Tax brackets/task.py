income = int(input())
if 0 <= income <= 15527:
    percent = 0
elif 15528 <= income <= 43707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
elif 132407 <= income:
    percent = 28
calculated_tax = round(income * percent / 100)

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")