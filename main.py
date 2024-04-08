import atbash
import caesar
import check_input

'''
Cipher decoder
3/13/2024
A program to encrypt and decrypt atbash and caesar ciphers
'''
def main():
  print("Secret Decoder Ring:")
  print("1. Encrypt")
  print("2. Decrypt")

  choice = check_input.get_int_range("", 1, 2)
  if choice == 1:
    print("Enter encryption type:")
    print("1. Atbash")
    print("2. Caesar")

    encryption_choice = check_input.get_int_range("", 1, 2)
    message = input("Enter message to encrypt: ")
    
    if encryption_choice == 1:
      cipher = atbash.AtbashCipher()
    else:
      shift = check_input.get_positive_int("Enter shift value: ")
      cipher = caesar.CaesarCipher(shift)

    encrypted_message = cipher.encrypt_message(message)
    print('Encrypted message saved to "message.txt".')

    with open("message.txt", "w") as file:
      file.write(encrypted_message)

  else:
    print("Enter decryption type:")
    print("1. Atbash")
    print("2. Caesar")
  
    decryption_choice = check_input.get_int_range("", 1, 2)

    if decryption_choice == 1:
      cipher = atbash.AtbashCipher()
    else:
      shift = check_input.get_int_range("Enter shift value: ", 0, 25)
      cipher = caesar.CaesarCipher(shift)

    try:
      with open("message.txt", "r") as file:
        encrypted_message = file.read().strip()
        decrypted_message = cipher.decrypt_message(encrypted_message)
        print('Reading encrypted message from "message.txt".')
        print("Decrypted message:", decrypted_message)
    except FileNotFoundError:
      print("No encrypted message found.")
              
              
  

main()