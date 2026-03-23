sentence="My name is RETRO"

# String Methods

#upper()
print(f"Upper case : {sentence.upper()}")

#lower()
print(f"Lower case : {sentence.lower()}")

#capitalize()
print(f"Capitalized : {sentence.capitalize()}")

#title()
print(f"Title case : {sentence.title()}")

#swapcase()
print(f"Sentence in swap case : {sentence.swapcase()}")

#find()
print(f"Index of 'RETRO' : {sentence.find('RETRO')}")

#index() - similar to find() but raises ValueError if substring not found
try:
    print(f"Index of 'RETRO' : {sentence.index('ii')}")  
except ValueError:
    print("Substring not found")

# rindex

#rfind
print(f"Last index of 'e' : {sentence.rfind('e')}")
print(f"'e' is found at {sentence.find('e')} position")

print(f"e is repeated for {sentence.count('e')}")

#startswith() and endswith()
print(f"Does the sentence start with 'My'? : {sentence.startswith('My')}")
print(f"Does the sentence end with 'RETRO'? : {sentence.endswith('RETRO')}")

#len() method is used to check the length of the string
print(f"Length of the sentence : {len(sentence)}")

#isalpha
string = "Hello"
str1="helloooo2222"
print(f"Is '{string}' all alphabetic? : {string.isalpha()}")
print(f"Is '{str1}' all alphabetic? : {str1.isalpha()}")

#isdigit() and isdicimal()
str2="12345"
str3="12345.88"
print(f"Is '{str2}' all digits? : {str2.isdigit()}"
)
print(f"Is '{str3}' all decimal? : {str3.isdecimal()}")
print(f"all str1,st2,str3:{str1.isalnum() and str2.isalnum() and str3.isalnum()}")  

#islower() and isupper()
print(f"Is '{string}' all lowercase? : {string.islower()}")
print(f"{'retro'.islower()}")

#strip()
print(f"String with spaces: '   Hello World   '")
print(f"String after strip: '{'   Hello World   '.strip()}'")

# rstrip() and lstrip()
print(f"String with spaces: '   Hello World   '")
print(f"String after rstrip: '{'   Hello World   '.rstrip()}'")
print(f"String after lstrip: '{'   Hello World   '.lstrip()}'")

#replace()
print(f"Original string: {sentence}")
print(f"String after replace: {sentence.replace('RETRO', 'WORLD')}")

#split() and join()
print(f"Original string: {sentence}")
print(f"String after split: {sentence.split()}")#split() returns a list of words in the string,white space is the default separator
print(f"String after split with 'o' as separator: {sentence.split('o')}")#split() with 'o' as separator
name="sai,sanket,sagar,reddy"
print(name.split(" ",2))
print(f"String after join: {'-'.join(sentence.split())}")

