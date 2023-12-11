def prime_and_sum(n):
    for i in range(2, int(n)):
        if n % i == 0:
            return -1

    return sum(range(n+1))

while True:
    
    try:
        num = int(input("Enter a number:\t"))
        break
        
    except ValueError:
            print("Invalid input! Please enter a valid value in integer.")

result = prime_and_sum(num)
if result == -1:
    print(f"{num} is not a prime number (-1)")

else:
    print(f"The number is prime number and sum of all numbers from 0 to {num} is {result}")


