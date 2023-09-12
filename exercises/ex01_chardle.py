"""EX01 - Chardle - A cute step toward Wordle"""
__author__ = "730585444"
# initializing variables
word: str = input("Enter a 5-character word: ")
#i made a big conditional here because I couldn't remember not equal to but it works lol
if (len(word)) == 5:

    single: str = input("Enter a single character: ")
    if len (single) != 1:
        print ("Error: Character must be a single character.")
        exit()
    count: int = 0
    print ("Searching for " + single + " in " + word)

    #Searching for letter
    if str (word[0])== str(single):
        print(str(single) + " found at index 0")
        count = count+1
    if str (word[1])== str(single):
        print(str(single) + " found at index 1")
        count = count+1
    if str (word[2]) == str(single):
        print(str(single) + " found at index 2")
        count = count+1
    if str (word[3]) == str(single):
        print(str(single) + " found at index 3")
        count= count + 1
    if str(word[4]) == str(single):
        print(str(single) + " found at index 4")
        count= count + 1
    if count ==0:
        print ("No instances of " + single + " found in " + word)
    else:
        print (str(count) + " instances of " + single + " found in " + word)
else:
    print ("Error: Word must contain 5 characters")
    exit()


    

