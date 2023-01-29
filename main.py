# Importing required libraries
import secrets
import string

# Defining the parameters from which 
# the password has to be developed from
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Concatenating all onto a single string
alphabet = letters + digits + special_chars

# Password length
pwd_length = 12


# generate password meeting constraints
while True:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))
    # below if block indicates that there should be any special character in 
    # password atleast along with atleast two strings
  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)