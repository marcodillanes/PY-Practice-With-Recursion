# Write code for algorithm 5 below

def palindrome(s):
    return s == s[:: -1]

print(palindrome("dad"))

# below is recursively

def isPalindrome(word):
    if len(word) < 2:
        return True


    else:
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else:
            return False

print(isPalindrome("racecar"))
