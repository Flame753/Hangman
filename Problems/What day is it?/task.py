offset = int(input())
monday = [-12, -11]
tuesday = [-x-1 for x in range(10)]
tuesday.reverse()
tuesday.extend([x for x in range(14)])
wednesday = [14]

# print(monday, tuesday, wednesday)

if offset in monday:
    print("Monday")
elif offset in tuesday:
    print("Tuesday")
elif offset in wednesday:
    print("Wednesday")
