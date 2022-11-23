#! /usr/bin/env /usr/bin/python
import tkinter as tk
print('import tk')
import tkinter.filedialog as fd
print('import fd')
import subprocess as sb
print('import sb')
import tkinter.messagebox as msg

base = tk.Tk()
string = tk.StringVar()

dir=''
print(dir)

check='wget -o gitV https://raw.githubusercontent.com/PEANUT-Sh/make-desktop/main/v.txt'

#初期設定



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
def cv():
    print('バージョン確認します...')
    with open('v.txt', encoding='utf-8') as f:
        v = f.readline()
    #オンラインのバージョンを取得
    sb.run(['wget', 'https://raw.githubusercontent.com/PEANUT-Sh/make-desktop/main/v.txt'])

    with open('v.txt.1', encoding='utf-8') as gi:
        g = gi.readline()
    if ( v == g ):
        print('最新バージョン' + g)
        print('ローカルのバージョン' + v)
        print('お使いのバージョンば最新です')
        info = msg.showinfo('バージョン', '最新です' + v)
    else:
        msg.showerror('バージョン', 'お使いのバージョンは最新ではありません。あなたのバージョン=>' + v)

base.title('デスクトップファイル生成')

selectfile = tk.PhotoImage(file='image/file.png')
small_img = selectfile.subsample(16, 16)

#部品の設定
menubar = tk.Menu(base)
menuhhelp = tk.Menu(menubar)
menubar.add_cascade(label='ヘルプ', menu=menuhhelp)
menuhhelp.add_command(label='バージョン',command=cv)

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

title.grid(row=1, column=1)
boxlabel.grid(row=2, column=2)
boxname.grid(row=2, column=3)

cmdlabel.grid(row=4, column=2)
cmdbox.grid(row=4, column=3)

filelabel.grid(row=5, column=2)
filepath.grid(row=5, column=3)
selfile.grid(row=5, column=4)

okbutton.grid(row=7, column=5)

base.mainloop()

