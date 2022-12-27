#! /usr/bin/env /usr/bin/python
print('######################################')
print('#                                    #')
print('#   #   #   #### #    #      ####    #')
print('#   #   #   #    #    #     #    #   #')
print('#   #####   ###  #    #     #    #   #')
print('#   #   #   #    #    #     #    #   #')
print('#   #   #   ###  #### ####   ####    #')
print('#                                    #')
print('######################################')
print('')

import tkinter as tk
print('import tk')
import tkinter.filedialog as fd
print('import fd')
import subprocess as sb
print('import sb')
import tkinter.messagebox as msg
import os
from PIL import Image, ImageTk

base = tk.Tk()
string = tk.StringVar()

dir=''
iconimage=''
print(dir)

#バージョン取得
local_v = open('virsion', 'r')
v = local_v.read()
print(v)

check='wget -o gitV https://raw.githubusercontent.com/PEANUT-Sh/make-desktop/main/v.txt'

#初期設定

base.geometry("500x460+700+300")

#aboutウインドウ
def about():
    about = tk.Toplevel()
    about.title('情報')
    about.mainloop()

#ファイルパス
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
    iconimage = iconpath.get()
    #確認のため出力
    print(command)
    print(name)
    print(dirname)
    print(iconimage)
    print('start make.sh')
    sb.run(['./make.sh', name, command, dirname, iconimage])
    base.destroy()



def selicon():
    iconimage = fd.askopenfilename(
        title='アイコンを選択',
        filetypes=filet,
        initialdir = '~/'
    )
    iconpath.delete(0, tk.END)
    iconpath.insert(tk.END,iconimage)
    print('icon => ' + iconimage)

def help():
    sb.run(['chromium-browser', 'https://peanut-sh.github.io/about-my-project/'])
base.title('デスクトップファイル生成')



selectfile = tk.PhotoImage(file='image/file.png')
small_img = selectfile.subsample(16, 16)

#部品の設定
menubar = tk.Menu(base)
menuhhelp = tk.Menu(menubar)
henyu = tk.Menu(menubar)

filet=[("画像","*.png")]

menubar.add_cascade(label='オプション', menu=henyu)
henyu.add_command(label='インターネットショートカット')
henyu.add_command(label='インターネットショートカット(アプリ風)')

menubar.add_cascade(label='ヘルプ', menu=menuhhelp)
menuhhelp.add_command(label='about', command=about)
menuhhelp.add_command(label='ヘルプ', command=help)

title = tk.Label(base, text='make desktop')

boxlabel = tk.Label(base, text='名前')
boxname = tk.Entry(base)

cmdlabel = tk.Label(base, text='コマンド')
cmdbox = tk.Entry(base)

filelabel = tk.Label(base, text='保存先')
filepath = tk.Entry(base)
selfile = tk.Button(base, image=small_img, command=file)

iconlabel = tk.Label(base, text='アイコンの場所')
iconpath = tk.Entry(base)
iconsel = tk.Button(base, image=small_img, command=selicon)

okbutton = tk.Button(base, text='次へ', command=ok)


#配置

base.config(menu=menubar)


boxlabel.place(x=100, y=60, height=30)
boxname.place(x=200, y=60, height=30)

cmdlabel.place(x=100, y=160, height=30)
cmdbox.place(x=200, y=160, height=30)

filelabel.place(x=100, y=260, height=30)
filepath.place(x=200, y=260, width=200, height=30)
selfile.place(x=400, y=260, height=30)

iconlabel.place(x=100, y=360, height=30)
iconpath.place(x=200, y=360, width=200, height=30)
iconsel.place(x=400, y=360, height=30)

okbutton.place(x=400, y=400)

base.mainloop()
