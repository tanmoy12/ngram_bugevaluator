word = input("enter a word") 

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
        count += 1
    for index in range(1, len(word)):
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1

print(syllable_count(word))