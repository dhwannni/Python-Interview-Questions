#1- remove a given character from string
#using replace() + input from user 
str = input("Please enter a word: ")
cha = input("Please enter a character: ")
print(str.replace(cha, ""))
#using translate() + no input from user
mystr = "Python is awesome!"
newstr = mystr.translate({ ord("o"): None })
print(newstr)

#2- occurence of given characters in a string
mystr = "dog cat dog cat dog cat"
substr = "dog"
dogcount = mystr.count(substr)
print(dogcount)
#occurence of one character using loops 
name = "python is awesome"
count = 0 
for i in range (len(name)):
    if name[i] == "o":
        count+=1
print(count)

#5- if a given character is a vowel or consonant
xyz = input("Enter a letter: ")
if xyz == "a" or xyz == "e" or xyz == "i" or xyz == "o" or xyz == "u":
    print("This letter is a vowel: ", xyz)
else: 
    print("This letter is a consonant: ", xyz)

#10- convert lowercase char to uppercase
str = input("Enter an ALL lowercase phrase: ")
print(str.upper())
#convert one character from a string 
str= "i love my python"
print(str.capitalize())

#11-convert lowercase vowel to uppercase in string
string = input("Enter a word: ")
vowels = "aeiou"
for char in string:
    if char in vowels:
        upper_char = char.upper()
        string = string.replace(char, upper_char)
print("Updated string:", string)

#12-delete vowels in a given string
str = "Python is awesome"
newstr = str.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(newstr)

#13-occurence of vowels and consonants in a string
vowels = 0 
con = 0 
str = "Python is a very common coding language"
for i in str:
    if i in ("a", "e", "i","o","u", "A", "E", "I","O","U" ):
        vowels +=1
    elif i.isalpha():
        con+=1
print("The amount of vowels is: ", vowels)
print("The amount of consonants is:", con)

#14- highest frequency char in a string
test = "Python"
freq_all = {}

for i in test:
    if i in freq_all:
        freq_all[i] += 1 
    else: 
        freq_all [i]=  1
print("The count of all characters in Python is: " + str(freq_all))

#21-remove repeated character in a string
def removedup(i):
    uchar= set()
    str =""
    for char in i:
        if char not in uchar:
            uchar.add(char)
            str+=char
    return str
inp = input("enter a string: ")
print(removedup(inp))