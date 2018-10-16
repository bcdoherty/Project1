import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
	file = open(file, 'r') #Input: file name
	lines = file.readlines()
	file.close()

	dictList = []

	for line in lines:
		dic = {}

		values = line.split(":")
		first = values[0]
		last = values[1]
		email = values[2]
		year = values[3]
		DOB = values[4]

		dic["first"] = first
		dic["last"] = last
		dic["email"] = email
		dic["class"] = year
		dic["DOB"] = DOB
		dictList.append(dic)
	return dictList
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	pass


def mySort(data,col):
	lst = []
	itemLst = []
	for x in range(len(data)):
		item = data[col]
		lst.append(item)
		valLst = list(x.values())
		itemLst.append(valLst)
	lst.sort()
	firstItem = lst[0]
	for x in range(len(itemLst)):
		if firstItem in x == True:
			first = x[0]
			last = x[1]
	print(first)