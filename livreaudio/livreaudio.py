#bibliotheque de convertion de text en audio meme offline
import pyttsx3
import PyPDF2

def say(txt):
    droid = pyttsx3.init() 
    voice = droid.getProperty('voices') 
    droid.setProperty('voice', voice[3].id) 
    droid.say(txt) 
    droid.runAndWait() 

#livre = open('Batouala - Rene Maran.pdf','rb')
livre = open('les_9_lois_de_la_richesse.pdf','rb')

reader = PyPDF2.PdfReader(livre)
pages = len(reader.pages)
for i in range(1,pages):
    debutlecture = reader.pages[i]
    texte = debutlecture.extract_text()
    print(i)
    say(texte)
    if i == 6:
        pass
        
        
    