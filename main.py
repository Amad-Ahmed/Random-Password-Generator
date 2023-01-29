# Importing required libraries
import secrets
import string

# Defining the parameters from which 
# the password has to be developed from
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Password length input prompt
pwd_length = 0

pwd_length = input("Kindly, enter length of password to be generated :: ")
pwd_length = int(pwd_length)



# Removing user-specified special characters
removal_special_chars = ""
removal_special_chars = input("Kindly specify any special characters to be not used for password generation :: ")
for i in range(len(removal_special_chars)):
    special_chars = special_chars.replace(removal_special_chars[i],"")

# Removing user-specified letters
removal_letter = ""
removal_letter = input("Kindly specify any letters to be not used for password generation :: ")
for i in range(len(removal_letter)):
    letters = letters.replace(removal_letter[i],"")

# Removing user-specified digits
removal_digits = ""
removal_digits = input("Kindly specify any digits to be not used for password generation :: ")
for i in range(len(removal_digits)):
    digits = digits.replace(removal_digits[i],"")

# Concatenating all onto a single string
alphabet = letters + digits + special_chars

# Number of special characters to be included in password
num_of_special_chars = 0
num_of_special_chars = int(input("Maximum number of special chars to be included in :: "))

# Number of digits to be included in password atleast 
# Must not be greater than length and comprise half of length
num_of_digits = 0
while True:
    num_of_digits = int(input("Number of digits to be included in (Least number):: "))
    if (num_of_digits < int(pwd_length/2) ):
        break



# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))
    # below if block indicates that there should be any special character in 
    # password atleast along with atleast two strings
  if (sum(char in special_chars for char in pwd)<=num_of_special_chars and 
      sum(char in digits for char in pwd)>=num_of_digits):
          break

print("Your Password is :: ")
print(pwd)