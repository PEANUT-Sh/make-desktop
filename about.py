#! /usr/bin/env /usr/bin/python
import tkinter as tk
base = tk.Tk()

base.geometry("500x450+700+300")
base.title('about this application')

title = tk.Label(text='デスクトップファイル生成', font=("20"))
v = tk.Label(text='1.0.1')
sentence = tk.Label(text='.desktopファイルを生成するpythonで書かれたプログラム')

title.pack()
v.pack()
sentence.pack()
base.mainloop()