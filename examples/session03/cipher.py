import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

cipher_list = list(alphabet)

# This should be a list in order
print(cipher_list)

message_text = "what has dates and sundays but cannot be eaten"

random.shuffle(cipher_list)

# This should be random now
print(cipher_list)

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

# This is what
print(cipher_text)

#new_cipher_text = "eqzergqtgvtqeqgvlqrfwaqa hgecvlvrqpeigtq fz"
decrypt_text = ""

for y in new_cipher_text:
    index = cipher_list.index(y)
    decrypt_char = alphabet_list[index]
    decrypt_text += decrypt_char

print decrypt_text
