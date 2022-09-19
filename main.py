from pytube import YouTube
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

def path():
    selected = filedialog.askdirectory()
    label_selected_path.config(text=selected, fg='grey')

def Download():
    url = input.get()
    get_path = label_selected_path.cget('text')

    if url == "":
        url_error.config(text='Link is not defined', fg='red')
    elif get_path == "":
        label_selected_path.config(text='Please select a path', fg='red')
    else:
        try:
            Youtube_url = YouTube(url)
            Youtube_url.streams.get_highest_resolution().download(get_path)
            url_error.config(text='Download completed', fg='green')

        except:
            url_error.config(text='Connection Error or Invalid Link', fg='red')

screen = Tk()

screen.resizable(False, False)
title = screen.title("Youtube Download")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

logo = ImageTk.PhotoImage(Image.open('logo.png').resize((200, 50)))
label =  Label(screen, text='Enter Download Link: ')
url_error =  Label(screen, text='')
input = Entry(screen, width=50)
label_selected_path = Label(screen, text='')
selectPath_btn = Button(screen, text='Select path for download', command=path)
download_btn = Button(screen, text='Download', command=Download, background='green', fg='white')

canvas.create_image(250,40, image=logo)
canvas.create_window(250, 120, window=label)
canvas.create_window(250, 150, window=url_error)
canvas.create_window(250, 180, window=input)
canvas.create_window(250, 220, window=label_selected_path)
canvas.create_window(250, 260, window=selectPath_btn)
canvas.create_window(250, 300, window=download_btn)

screen.mainloop()
