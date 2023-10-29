t = int(input())

def decrypt(plaintext, shift):
    encrypted_text = ""
    shift_amount = shift % 26

    for char in plaintext:
        if char.isalpha():
            encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

def encrypt(ciphertext, shift):
    return decrypt(ciphertext, -shift)

for _ in range(t):
    n = int(input())
    s = input().strip()
    ss = s.split(" ")

    # if s[:4] == "the " or " the " in s or s[-4:] == " the":
    #     print(encrypt(s, n))
    # else:
    #     print(encrypt(s, -n))

    if "the" in ss:
        print(encrypt(s, n))
    else:
        print(encrypt(s, -n))