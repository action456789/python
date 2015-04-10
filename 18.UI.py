#!/usr/bin/env python  
# -*- coding: utf-8 -*-

print u'-------------------------图形界面------------------------------'

# 这里介绍使用 Tkinter 创建图片界面，python自带，无需安装
# Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写。

from Tkinter import *
import tkMessageBox

# 在GUI中，每个Button、Label、输入框等，都是一个Widget。

# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。


# 1. 从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)

		#pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
		self.pack()

		self.createWidgets()

	def createWidgets(self):
		# 创建一个Label
		self.helloLable = Label(self, text='Hello, world!')
		self.helloLable.pack()

		# 创建一个输入框
		self.nameInput = Entry(self)
		self.nameInput.pack()

		# 创建一个按钮，点击触发hello函数
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()

		#创建一个按钮，点击触发self.quit
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()

	def hello(self):
		# 获取用户输入文本
		name = self.nameInput.get() or 'world' 

		# 弹出消息对话框
		tkMessageBox.showinfo('Message', 'Hello, %s' % name) 

# 2. 实例化Application，并启动消息循环：
app = Application()

# 设置窗口标题:
app.master.title('Hellp=o, world')

# 主消息循环:
app.mainloop()

