def reverseVowels(s):
    vowels=""
    not_vowels=""
    reversed_vowels=""
    for letter in s:
        if letter.upper() in "AEIOU":
            vowels += letter
        else:
            not_vowels += letter
    i=len(vowels)-1
    j=0
    for letter in s:
        if letter.upper() in "AEIOU":
            reversed_vowels += vowels[i]
            i -= 1
        else:
            reversed_vowels += not_vowels[j]
            j += 1
    return(reversed_vowels)

print(reverseVowels("leetcode"))
