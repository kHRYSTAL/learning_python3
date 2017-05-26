#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
@version: ??
@usage: edit text
@author: kHRYSTAL
@license: Apache Licence 
@contact: khrystal0918@gmail.com
@site: https://github.com/kHRYSTAL
@software: PyCharm
@file: 02_use_tkinter.py
@time: 16/5/24 下午11:36
"""
#输入文本


from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text="Hello",command=self.hello)
        self.alertButton.pack()

    def hello(self):
        #python 中的and从左到右计算表达式，若所有值均为真，
        # 则返回最后一个值，若存在假，返回第一个假值。
        #or也是从左到有计算表达式，返回第一个为真的值。
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, %s' % name)




if __name__ == '__main__':
    app = Application()
    app.master.title('Hello World')
    app.mainloop()