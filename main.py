#! /usr/bin/env /usr/bin/python
import tkinter as tk
print('import tk')
import tkinter.filedialog as fd
print('import fd')
import subprocess as sb
print('import sb')
import tkinter.messagebox as msg
import os

base = tk.Tk()
string = tk.StringVar()

dir=''
print(dir)

check='wget -o gitV https://raw.githubusercontent.com/PEANUT-Sh/make-desktop/main/v.txt'

#初期設定

base.geometry("500x500+700+300")


def file():
    dir = fd.askdirectory(
        title = '保存先',
        initialdir = '~/'
        )
    filepath.delete(0, tk.END)
    filepath.insert(tk.END,dir)
    print('opendir => ' + dir)

def ok():
    command = cmdbox.get()
    name = boxname.get()
    dirname = filepath.get()
    #確認のため出力
    print(command)
    print(name)
    print(dirname)
    print('start make.sh')
    sb.run(['./make.sh', name, command, dirname])
    base.destroy()

def about():
    sb.run(['python', './about.py'])
base.title('デスクトップファイル生成')

selectfile = tk.PhotoImage(file='image/file.png')
small_img = selectfile.subsample(16, 16)

#部品の設定
menubar = tk.Menu(base)
menuhhelp = tk.Menu(menubar)
henyu = tk.Menu(menubar)

menubar.add_cascade(label='オプション', menu=henyu)
henyu.add_command(label='インターネットショートカット')
henyu.add_command(label='インターネットショートカット(アプリ風)')

menubar.add_cascade(label='ヘルプ', menu=menuhhelp)
menuhhelp.add_command(label='about', command=about)

title = tk.Label(base, text='make desktop')

boxlabel = tk.Label(base, text='名前')
boxname = tk.Entry(base)

cmdlabel = tk.Label(base, text='コマンド')
cmdbox = tk.Entry(base)

filelabel = tk.Label(base, text='保存先')
filepath = tk.Entry(base)
selfile = tk.Button(base, image=small_img, command=file)

okbutton = tk.Button(base, text='次へ', command=ok)


#配置

base.config(menu=menubar)

boxlabel.place(x=100, y=100, height=30)
boxname.place(x=200, y=100, height=30)

cmdlabel.place(x=100, y=200, height=30)
cmdbox.place(x=200, y=200, height=30)

filelabel.place(x=100, y=300, height=30)
filepath.place(x=200, y=300, width=200, height=30)
selfile.place(x=400, y=300, height=30)

okbutton.place(x=7, y=5)

base.mainloop()