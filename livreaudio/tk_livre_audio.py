#bibliotheque de convertion de text en audio meme offline
from tkinter import *
from tkinter import filedialog
import pyttsx3
import PyPDF2

root = Tk()
root.title('MON LECTEUR PERSO')

root.configure(background="orange")

#root.iconbitmap()
root.geometry("500x500")

#CREATE TEXTBOX
my_text_box = Text(root,height=400,width=300)
my_text_box.pack(pady=10)
#my_text_box.insert(1.0,"Ouvrir un fichier pdf pour afficher le Text ici")


def say(txt):
    droid = pyttsx3.init() 
    voice = droid.getProperty('voices') 
    droid.setProperty('voice', voice[3].id) 
    droid.say(txt) 
    droid.runAndWait() 
    
def clear_text_box():
    my_text_box.delete(1.0, END)

def open_pdf():
    open_file = filedialog.askopenfilename(
        title="Ouvrir un Fichier PDF",
        filetypes=(
            ("PDF Files","*.pdf"),
            ("All Filles","*.*")
        )
    )
    
    if open_file:
        reader = PyPDF2.PdfReader(open_file)
        pages = len(reader.pages)
        # pages = len(reader.pages)
        for i in range(1,pages):
            debutlecture = reader.pages[i]
            texte = debutlecture.extract_text()
            print(i)
            #my_text_box.delete(1.0, END)
            my_text_box.insert(1.0,texte)
            say(texte)
           
            
#Creation du menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Ajouter une list deroulante
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Fichier",menu=file_menu,background='#5D1725')
file_menu.add_command(label="Ouvrir",command=open_pdf)
file_menu.add_command(label="Vider",command=clear_text_box)
file_menu.add_separator(background="Blue")
file_menu.add_command(label="Quiter",command=root.quit)

       
root.mainloop() 
    