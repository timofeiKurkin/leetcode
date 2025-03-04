from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return len(chars)

        writeIndex = 0  # Индекс, куда мы записываем результат
        index = 0  # Индекс для прохода по chars

        while index < len(chars):
            currentChar = chars[index]  # Текущий элемент
            count = 0  # Количество повторяющихся элементов

            while (
                index < len(chars) and chars[index] == currentChar
            ):  # Подсчет одинаковых букв. Т.к. они отсортированы, проходимся линейно
                count += 1
                index += 1

            chars[writeIndex] = currentChar  # Запись текущего символа в массив
            writeIndex += 1  # Изменение

            if count > 1:
                for digit in str(count):
                    chars[writeIndex] = digit
                    writeIndex += 1

        return writeIndex


solution = Solution()

print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(solution.compress(["a"]))
print(
    solution.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
)
