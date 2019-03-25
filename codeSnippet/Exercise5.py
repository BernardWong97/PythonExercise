# Loops
primes = [2, 3, 5, 7]
for number in primes:
    print(number)

print("Print range function")
for i in range(5):
    print(i)

print("Print range 3 to 7 inc 2")
for i in range(3, 8, 2):
    print(i)


print("While loop")
count = 0
while count < 5:
    print(count)
    count += 1

print("Break statement")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("Continue statement")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("else")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached maximum")
