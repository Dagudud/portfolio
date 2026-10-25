import interface
from ciphers import ceasar_encrypt
from ciphers import atbash

def encrypt():
    plaintext = interface.plaintextbox.get()
    key = int(interface.keybox.get())
    x = ceasar_encrypt(plaintext, key)
    interface.text4.config(text=x)
    y = atbash(plaintext)
    interface.text6.config(text=y)
interface.button.config(command=encrypt)

interface.root.mainloop()