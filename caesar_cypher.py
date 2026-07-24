alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"text after encryption : {cipher_text}")


def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            shift_key=(shift_key)%26
            new_position = position-shift_key
            if new_position < 0:
                new_position+=26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print(f"text after decryption : {plain_text}")

continue_programme = True

while continue_programme:

  what_to_do=input("Type 'encrypt' for encryption , type 'decrypt' for decryption:\n ")
  text=input("Type your message : \n")
  shift_key=int(input("Enter the shift key : \n"))

  if what_to_do=="encrypt":
     encryption(text,shift_key)
  elif what_to_do=="decrypt":
     decryption(text,shift_key)
  else:
      print("Invalid Input")

  choice = input("Do you want to continue? (yes/no)\n:")
  if choice == "no":
    continue_programme = False
    print("Thank you for using caesar_cypher")

