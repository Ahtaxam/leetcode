def detectCapitalUse(self, s: str) -> bool:
    if s.isupper():
        return True
    elif s[0].isupper() and s[1:].islower():
        return True
    elif s.islower():
        return True
    else:
        return False



# Input: word = "USA"
# Output: true

# Input: word = "FlaG"
# Output: false