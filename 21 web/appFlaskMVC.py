#!/usr/bin/env python  
# -*- coding: utf-8 -*-
# 从wsgiref模块导入:

print u'---------------------- 使用 MVC 模式改写appFlask.py ------------------------'

# appFlask.py，处理3个URL，分别是：
# GET /：首页，返回Home；
# GET /signin：登录页，显示登录表单；
# POST /signin：处理登录表单，显示登录结果。


# 安装Flask:
# easy_install flask

# Flask默认支持的模板是jinja2，所以我们直接安装jinja2：
# easy_install jinja2


# 模版技术
# 由于在Python代码里拼字符串是不现实的，所以，模板技术出现了。也就是 MVC 模式

# 使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，
# 然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：

# 这个例子中
# Python处理URL的函数就是C：Controller，
# 包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
# Model就是一个dict：{ 'name': 'Michael' }


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

# 然后，开始编写jinja2模板，在templates目录下。
# 一定要把模板放到正确的templates目录下，templates和app.py在同级目录下：


# 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
# 比如循环输出页码：

# {% for i in page_list %}
#     <a href="/page/{{ i }}">{{ i }}</a>
# {% endfor %}

# 如果page_list是一个list：[1, 2, 3, 4, 5]，上面的模板将输出5个超链接。