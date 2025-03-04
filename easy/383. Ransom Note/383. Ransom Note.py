from typing import Dict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters: Dict[str, int] = {}

        for letter in magazine:
            if magazine_letters[letter]:
                magazine_letters[letter] = (magazine_letters[letter] or 0) + 1
            else:
                magazine_letters[letter] = 1

        for letter in ransomNote:
            if not magazine_letters[letter] or magazine_letters[letter] < 1:
                return False
            magazine_letters[letter] -= 1

        return True
