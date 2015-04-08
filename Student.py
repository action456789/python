#!/usr/bin/env python  
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self, name, age, score):
		super(Student, self).__init__()
		self.name = name
		self.age = age
		self.score = score

	#自定义的JSON序列化的函数，也可使用默认的__dict__
	def student2dict(student):
		return {
			'name' : student.name,
			'age' : student.age,
			'score' : student.score
		}

	#自定义的JSON反序列化的函数
	def dict2student(d):
		return Student(d['name'], d['age'], d['score'])

	def __str__(self):
		return 'Student object (name: %s, age: %d, score: %.1f)' %(self.name, self.age, self.score)
