'''
Create a function that takes a string and censors words over four characters with *.

Examples
censor("The code is fourty")
output = "The code is ******"

censor("Two plus three is five")
output = "Two plus ***** is five"

censor("aaaa aaaaa 1234 12345")
output = "aaaa ***** 1234 *****"
Notes
Don't censor words with exactly four characters.

If all words have four characters or less, return the original string.

The amount of * is the same as the length of the word.
'''

def main(prompt):
    output = censor(input(prompt))
    print(f"Censored sentence: {output}")


def censor(zin: str):
    woorden = zin.split()
    censored = []
    for woord in woorden:
        if len(woord) > 4:
                woord = "*" * len(woord)
                censored.append(woord)
        else:
            censored.append(woord)
    return " ".join(censored)

if __name__ == "__main__":
    main("Please put in your string: ")

