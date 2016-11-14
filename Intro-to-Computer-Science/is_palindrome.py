def is_palindrome (word):
    n = len(word)
    if n < 2:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome (word[1:-1])
        else:
            return False

print is_palindrome('abab')

# recursive digui shulie
# iterative chongfu shulie
