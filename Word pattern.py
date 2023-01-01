def wordPattern(self, pattern: str, s: str) -> bool:
    record = {}
    s = s.split(' ')
    if len(s) != len(pattern) or s == '' or pattern == '':
        return False
    else:
        for letter in range(len(pattern)):
            if pattern[letter]  not in record:
                if s[letter] in record.values():
                    return False
                record[pattern[letter]] = s[letter]
            else:
                data = record[pattern[letter]]
                if data != s[letter]:
                    return False
    return True




# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true


# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false