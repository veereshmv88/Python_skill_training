# ============================================================
# CONDITIONS AND CONTROL FLOW
# ============================================================

s = list(input("Enter the value:"))
print(s)

if s % 2 == 0:
    print('Even')
else:
    print('Odd')

if 'A' <= ch <= 'Z':
    print('true')
else:
    print('false')

num = int(input("Enter:"))
if 100 < num < 999:
    print('true')


# ============================================================
# CHECK RELATIONSHIP BETWEEN TWO NUMBERS
# ============================================================

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")


# ============================================================
# CHECK CHARACTER TYPE
# ============================================================

ch = input("Enter a character:")

if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
elif '0' <= ch <= '9':
    print("Number")
else:
    print("Special character")


# ============================================================
# CHECK WHETHER THE CHARACTER IS A VOWEL
# ============================================================

ch = input("Enter a character:")

if ch in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Not a vowel")


# ============================================================
# CHECK STRING LENGTH
# ============================================================

s = input("Enter a string:")
print("Length of the string is:", len(s))

if len(s) % 2 == 0:
    print("Length is even")
else:
    print("Length is odd")


# ============================================================
# PRINT ALL ELEMENTS INSIDE THE LIST
# ============================================================

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)


# ============================================================
# CONVERT UPPERCASE TO LOWERCASE
# ============================================================

s = input("Enter a string:")
out = ' '

for i in s:
    if 'A' <= i <= 'Z':
        out += i.lower()
    else:
        out += i

print("Converted string is:", out)


# ============================================================
# NESTED FOR LOOP
# ============================================================

for i in range(1, 6):
    for j in range(1, 6):
        print('a', end=' ')
    print()


# ============================================================
# CONVERT FUNCTION
# ============================================================

def convert(s):
    out=