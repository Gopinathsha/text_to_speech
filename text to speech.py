import pyttsx3
import tkinter as tk

def speak_text():
    engine = pyttsx3.init()
    engine.say(text_entry.get("1.0", tk.END))
    engine.setProperty('rate', 100)  
    engine.setProperty('volume', 1.0)
    engine.runAndWait()

root = tk.Tk()
root.resizable(False,False)
root.config(bg="cyan")
root.geometry("500x500")

root.title("Text-to-Speech")

text_label = tk.Label(root, text="Enter text:",font=("varanda",10))
text_label.pack()

text_entry = tk.Text(root, height=5, width=50,bg="cyan")
text_entry.pack()

speak_button = tk.Button(root, text="Speak", command=speak_text,bg="yellow",font=("varanda",10),)
speak_button.pack()

root.mainloop()
