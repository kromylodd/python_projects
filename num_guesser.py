def is_valid(n, left, right):
    if n == guess:
        return True
    elif n >= left and n <= right:
        return True
    else:
        return False
import random
guess = random.randint(1,100)
left = 1
right = 100
n = 0
cnr = 0
print("sup, thats a number guesser!")
print(f"take a gueess {left}-{right}")
while n != guess:
    n = int(input())
    cnr += 1
    while not is_valid(n, left, right):
        print(f"take a gueess {left}-{right} beach")
        n = int(input())
    if n == guess:
        print(f"u got me, num was {guess}, number of tries - {cnr}")
    elif n > guess:
        right = n - 1
        print(f"a lil lower unc ({left}-{right})")
    elif n < guess:
        left = n + 1
        print(f"a bigger one now ({left}-{right})")
