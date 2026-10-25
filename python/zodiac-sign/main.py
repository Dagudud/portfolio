import interface
import zodiac

def zodiacs():
    day = int(interface.entry1.get())
    month = int(interface.entry2.get())
    index = zodiac.define(day, month)
    name = interface.zodiac_names[index]
    file = interface.zodiac_files[index]
    interface.name.config(text=name)
    interface.gif.config(file=f'img/{file}')
    
interface.button.config(command=zodiacs)

interface.root.mainloop()