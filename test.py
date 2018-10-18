import os
import filecmp
import operator
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

	#pass


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

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
	lst = []
	sr = 0
	jr = 0
	so = 0
	fr = 0
	for x in range(len(data)):
		year = x['class']
		if year == 'Senior':
			sr = 1 + sr
		elif year == 'Junior':
			jr = 1 + jr
		elif year == "Sophomore":
			so = 1 + so
		else:
			fr = 1 + fr
	#make tuples
	srCount = ("Senior", sr)
	jrCount = ("Junior", jr)
	soCount = ("Sophomore", so)
	frCount = ("Freshman", fr)

	lst.append(srCount)
	lst.append(jrCount)
	lst.append(soCount)
	lst.append(frCount)

	lst.sort(key = operator.itemgetter(1), reverse=True)
	# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#pass

	def findMonth(a):
		lst = []
		mode = 0
		for x in range(len(a)):
			DOB = a['DOB']
			DOBlst = list(DOB)
			month = DOBlst[0]
			lst.append(month)
		for x in range(1,13):
			count = lst.count(x)
			if count > mode:
				mode = count
		return mode
	# Find the most common birth month form this data
	# Input: list of dictionaries
	# Output: Return the month (1-12) that had the most births in the data

	data = getData(P1DataB.csv)
	print(data)
