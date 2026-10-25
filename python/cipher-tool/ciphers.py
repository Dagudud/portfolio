alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def ceasar_encrypt(plaintext, key):
    ciphertext = ''
    for i in plaintext.lower():
        if i == ' ':
            ciphertext = ciphertext + ' '
            continue
        index = alphabet.find(i)
        new_index = index + key
        new_index = new_index % len(alphabet)
        new_letter = alphabet[new_index]
        ciphertext = ciphertext + new_letter
    return ciphertext

def atbash(plaintext):
    x = alphabet[::-1]
    ciphertext = ''
    for i in plaintext.lower():
        if i == ' ':
            ciphertext = ciphertext + ' '
            continue
        index = alphabet.find(i)
        ciphertext = ciphertext + x[index]
    return ciphertext