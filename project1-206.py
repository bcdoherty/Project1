import os
import filecmp
import operator
import re
from dateutil.relativedelta import *
from datetime import date

#test
def getData(file):
# get a list of dictionary objects from the file
	file = open(file, 'r') #Input: file name
	lines = file.readlines()
	file.close()

	dictList = []

	for line in lines:
		dic = {}

		values = line.split(",")
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
		dic = data[x]
		item = dic[col]
		lst.append(item)
		valLst = list(dic.values())
		itemLst.append(valLst)
	lst.sort()
	firstItem = lst[0]
	for x in range(len(data)):
		#lst1 = []
		dic = data[x]
		vals = list(dic.values())
		bl = firstItem in vals
		if bl == True:
			name = dic['first'] +" " +dic['last']
			return name

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
	oops = 0
	for x in range(len(data)):
		dic = data[x]
		year = dic['class']
		if year == 'Senior':
			sr = 1 + sr
		elif year == 'Junior':
			jr = 1 + jr
		elif year == "Sophomore":
			so = 1 + so
		elif year == "Freshman":
			fr = 1 + fr
		else:
			oops = oops + 1
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
	return lst
	# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#pass

def findMonth(a):
	lst = []
	jan = 0
	feb = 0
	mar = 0
	apr = 0
	may = 0
	jun = 0
	jul = 0
	aug = 0
	sep = 0
	octob = 0
	nov = 0
	dec = 0
	oops = 0
	for x in range(len(a)):
		dic = a[x]
		DOB = dic['DOB']
		lst.append(DOB)
	months = []
	for x in range(len(lst)):
		date = lst[x]
		monthLst = re.findall(r'^1?[0-9]',date)
		if len(monthLst) > 0:
			month = monthLst[0]
			months.append(month)
	for x in range(len(months)):
		month = months[x]
		if month == '1':
			jan = jan + 1
		elif month == '2':
			feb = feb + 1
		elif month == '3':
			mar = mar + 1
		elif month == '4':
			apr = apr + 1
		elif month == '5':
			may = may + 1
		elif month == '6':
			jun = jun + 1
		elif month == '7':
			jul = jul + 1
		elif month == '8':
			aug = aug + 1
		elif month == '9':
			sep = sep + 1
		elif month == '10':
			octob = octob + 1
		elif month == '11':
			nov = nov + 1
		elif month == '12':
			dec = dec + 1
		else:
			oops = oops + 1
	mode = max(jan,feb,mar,apr,may,jun,jul,aug,sep,octob,nov,dec)
	if mode == jan:
		print('1')
	if mode == feb:
		print('2')
	if mode == mar:
		print('3')
	if mode == apr:
		print('4')
	if mode == may:
		print('5')
	if mode == jun:
		print('6')
	if mode == jul:
		print('7')
	if mode == aug:
		print('8')
	if mode == sep:
		print('9')
	if mode == octob:
		print('10')
	if mode == nov:
		print('11')
	if mode == dec:
		print('12')
	# Find the most common birth month form this data
	# Input: list of dictionaries
	# Output: Return the month (1-12) that had the most births in the data

def mySortPrint(a,col,fileName):
	lst = []
	itemLst = []
	for x in range(len(a)):
		dic = a[x]
		item = dic[col]
		lst.append(item)
		valLst = list(dic.values())
		itemLst.append(valLst)
	lst.sort()
	firstItem = lst[0]
	for x in range(len(a)):
		#lst1 = []
		dic = a[x]
		vals = list(dic.values())
		bl = firstItem in vals
		if bl == True:
			first = dic['first']
			last = dic['last']
			email = dic['email']
			string = first + ", " + last + ", " + email
	outFile = open(fileName, "w")
	outFile.write(string)
	outFile.close()



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'first'),'Abbot Le',25)
	total += test(mySort(data2,'first'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'last'),'Elijah Adams',25)
	total += test(mySort(data2,'last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'email'),'Hope Craft',25)
	total += test(mySort(data2,'email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	#print("\nTest of extra credit: Calcuate average age")
	#total += test(findAge(data), 40, 5)
	#total += test(findAge(data2), 42, 5)

	#print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
