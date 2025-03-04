from collections import deque
from typing import Deque, List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines: List[str] = []

        # for word in words:
        #     last_line = lines[-1]
        #     if len(last_line) + len(word) + 1 <= maxWidth:
        #         lines[-1] += f"{word} "
        #     else:
        #         remain = maxWidth - len(last_line)
        #         lines[-1] += " " * remain
        #         lines.append(f"{word} ")

        def run(words_remains: Deque[str]) -> None:
            if not words_remains:
                last_remain = maxWidth - len(lines[-1])
                lines[-1] += " " * last_remain
                return

            word = words_remains.popleft()
            if len(word) == maxWidth:
                lines.append(word)
            else:
                if not lines:
                    lines.append("")

                if len(lines[-1]) + len(word) == maxWidth:
                    lines[-1] += word
                elif len(lines[-1]) + len(word) < maxWidth:
                    lines[-1] += f"{word} "
                else:
                    lines[-1] += " " * (maxWidth - len(lines[-1]))
                    lines.append(f"{word} ")

            run(words_remains)

        run(deque(words))

        def justify_text(divorced_line: List[str]) -> str:
            total_word_length = sum(len(word) for word in divorced_line)
            total_spaces = maxWidth - total_word_length
            gaps = len(divorced_line) - 1

            if gaps == 0:
                return divorced_line[0] + " " * total_spaces

            spaces_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps

            result = []
            for i, word in enumerate(divorced_line):
                result.append(word)
                if i < gaps:
                    result.append(
                        " " * (spaces_per_gap + (1 if i < extra_spaces else 0))
                    )

            return "".join(result)

        for i in range(len(lines) - 1):
            lines[i] = justify_text(lines[i].split())

        return lines


solution = Solution()
print(solution.fullJustify(words=["a", "b", "c", "d", "e"], maxWidth=1))

print(
    solution.fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    )
)

print(
    solution.fullJustify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
    )
)

print(
    solution.fullJustify(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
    )
)
