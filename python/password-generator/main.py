import interface
import generator

def generate():
    interface.listbox.delete(0, 'end')
    for i in range(5):
        lowercase = interface.lowercase.get()
        numbers = interface.numbers.get()
        uppercase = interface.uppercase.get()
        symbols = interface.symbols.get()
        x = generator.generate_password(lowercase, numbers, uppercase, symbols)
        interface.listbox.insert(0, x)

interface.button.config(command=generate)

interface.root.mainloop()