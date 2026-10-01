mode = int(input("Encryption or Decryption (1 or 2):"))
shift = int(input("Spicify ur shift:"))

# print(plaintext)

def encrypt(plaintext , shift):  #we use ord() to give the number in asci code , we use chr() to give the character from the ascicod e
    encrypted_text = ""
    for char in plaintext:
        position = ord(char) - ord('A')
        new_position = (position + shift ) % 26 
        new_char = chr(new_position + ord('A'))
        encrypted_text= encrypted_text + new_char
        
    return encrypted_text
        


def decrypt(cipher_text , shift ):
    decrypted_text = ""
    for  char in cipher_text:
        position = ord(char) - ord('A')
        new_position = (position - shift ) % 26 
        new_char = chr(new_position + ord('A'))
        decrypted_text = decrypted_text + new_char
    return decrypted_text    

if mode == 1:
         plain_text = input("Write ur message to be  Encrypted:").upper()
         cipher_text= encrypt(plain_text , shift)
         print(cipher_text)
elif mode == 2:
         cipher_text = input("Write ur message to b decrupted:").upper()
         plain_text = decrypt(cipher_text , shift)
         print(plain_text)
else:
      print("invalid string")



