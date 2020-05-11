# Make sure your output matches the assignment *exactly*
hours = int(input())

if hours < 2:
    print('That seems reasonable')
elif 2 <= hours < 4:
    print('Do you have time for anything else?')
else:
    print('You need to get outside more!')
