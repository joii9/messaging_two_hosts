
import tkinter
import tkinter as tk

from tkinter import *


class MainWindow():

    def __init__(self):

        self.win=tkinter.Tk()
        self.win.title("Telegram by Joel")
        self.win.configure() #bg="#D49FFF"
        self.win.geometry("500x400")

    def create_greeting(self, greeting):

        label= tk.Label(self.win, text=greeting) #font=("Helvetica", 15), fg="#4D4D4D"
        label.configure() #bg="#D49FFF"
        label.pack()

    def create_viewer_text(self):

        self.viewer_text = tk.Text(self.win, wrap="word", width=60, height=18)
        file_path= "X:\\test_messaging\\logs_messages.txt"
        content = open(file_path, 'r')
        self.viewer_text.insert(tk.END, content.read())
        self.viewer_text.pack()
        
    def create_inbox_message(self):
        
        frame=LabelFrame(self.win, text="Tu mensaje va aquí")
        frame.config()#bg = "#D49FFF"
        frame.pack(side="bottom",anchor=S, fill="both") #expand=True, padx=10, pady=10
        self.message = Entry(frame) #Invocamos la función entry_box dentro de la funcion busqueda, en el frame. Tener cuidado con el nombre de las variables de los frames, ya que en los argumentos del frame lo colocara en frame correspondiente
        self.message.config(width=70) #state='readonly', width=30
        self.message.grid(padx = 5)
        send_button= Button(frame, text= "Enviar", command=self.getting_text_inbox_message) 
        send_button.grid(row= 0, column= 3, padx = 5, pady = 10)
        
    def getting_text_inbox_message(self):
        
        message=self.message.get()
        print(message)
        message_sent= message+"\n"
        textfile= open("X:\\test_messaging\\logs_messages.txt", "a") 
        textfile.write(message_sent)
        textfile.close()
        self.message.delete(0, END)
        self.viewer_text.destroy()
        self.create_viewer_text()        
    
    def show(self):
        self.win.mainloop()



#main_window = MainWindow()
#main_window.create_greeting("Iniciaste un chat con ... por favor saluda")
#main_window.create_inbox_message()
#main_window.create_viewer_text()
#main_window.show()


