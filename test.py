for hour in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hour, ':', minutes, ':', seconds)

num = int(input())
if num % 2 == 0:
    print("Число четное")
else:
    print("Число не четное")