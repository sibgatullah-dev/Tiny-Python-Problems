'''
CHALLENGE: Write a function that takes a sentence, and returns the longest even-length word in the sentence. Or if it has no even-lengeth word in the words, return "00"
'''


def longest_even(text):
    longest="00"
    for word in text.splite():
        if len(word)%2 == 0 and len(word) >= len(longest):
            longest = word
    return longest

# strings = [
#     "my apple",
#     " ",
#     " hello i am from Bangladesh . i am a php laravel javascript vue web developer i am specialized in php js laravel vue mysql",
#    "a bb cccccsjfiodsj dfg dsfgdfsag"
# ]
# for string in strings:
#     print(f"'{string}'->'{longest_even(string)}'")