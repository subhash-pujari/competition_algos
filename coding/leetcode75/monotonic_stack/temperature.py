from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_map = list()

        output = [0 for i in range(len(temperatures))]

        for i, num in enumerate(temperatures):
            for j, temperature in temperature_map:
                if num > temperature and temperature_map[temperature] is not None:
                    output[temperature_map[temperature]] = (
                        i - temperature_map[temperature]
                    )

                    temperature_map[temperature] = None

            temperature_map.append((num, i))

        return output


# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]

print(temperatures)
print(Solution().dailyTemperatures(temperatures))
