"""
Problem: https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75
"""

from typing import List


def collide(stack, past, new):
    if past * new < 0:
        if past < 0 and new > 0:
            stack.append(past)
            stack.append(new)
        else:
            if abs(past) > abs(new):
                stack.append(past)
            elif abs(past) < abs(new):
                if len(stack):
                    past = stack.pop()
                    collide(stack, past, new)
                else:
                    stack.append(new)
    else:
        stack.append(past)
        stack.append(new)


class SolutionOur:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        past = None

        for asteroid in asteroids:
            if len(stack):
                past = stack.pop()
                collide(stack, past, asteroid)
            else:
                stack.append(asteroid)

        return stack


print(SolutionOur().asteroidCollision([5, 10, -5]))
print(SolutionOur().asteroidCollision([8, -8]))
print(SolutionOur().asteroidCollision([10, 2, -5]))
