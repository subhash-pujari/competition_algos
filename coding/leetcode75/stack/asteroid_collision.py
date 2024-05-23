# import numpy as np

asteroids = [5,10,-5]


stack = list()

for asteroid in asteroids:

    if len(stack):
        while :
            if item * asteroid < 0:
                if abs(item) > abs(asteroid):
                    break
                else:
                    stack.pop(item)
                    stack.append(asteroid)
    else:
        stack.append(asteroid)

print(stack)
