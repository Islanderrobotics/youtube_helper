import math
from itertools import compress
'''this class will allow the dev the ability to sort data with merge sort when the data 
has more then one piece of data paired to it'''

# if you didnt want to use Islander_sort you could just use the sort() method
class Islander_sort:
	def __init__(self, number_list, string_list = None):
		if string_list is None:
			self.data = number_list
			self.both = False
		else:
			self.data = list(zip(number_list,string_list))
			self.both = True

		self.string = []
		self.number = []

	def merging(self, left,right):
		"""this is will combine the two list"""
		new_list = []
		while (min(len(left),len(right))):
			if (left[0]>right[0]):
				to_insert = right.pop(0)
				new_list.append(to_insert)
			elif(left[0]<=right[0]):
				to_insert = left.pop(0)
				new_list.append(to_insert)
		if (len(left)>0):
			for i in left:
				new_list.append(i)
		if (len(right)>0):
			for i in right:
				new_list.append(i)
		return(new_list)

	def MergeSort(self,data):
		"""this is where the recursive decsions will happen"""
		new_list = [] 
		if (len(data)==1):
			new_list = data
		else:
			left = self.MergeSort(data[:math.floor(len(data)/2)])
			right = self.MergeSort(data[math.floor(len(data)/2):])
			new_list = self.merging(left, right)

		return (new_list)

	def split(self):
		if (self.both):
			for i in range(len(self.data)):
				self.string.append(self.data[i][1])
				self.number.append(self.data[i][0])

		else:
			for i in self.data:
				self.number.append(i)

	def drive(self):
		self.data = self.MergeSort(self.data)
		self.split()

new_list = [4,3,0,6,2,7,100,43]
string_list = ["bob", "what","will","you","do","with","that","stuff"]
print("this is islander sort with out a string_list")
data = Islander_sort(number_list = new_list)
data.drive()
print(f"this is the list with out split{data.data}")
print(f"this is the number list as well with out the split {data.number}")
print("\n")
print("this is the data with the string list")
data = Islander_sort(number_list = new_list, string_list = string_list)
data.drive()
print(f"this is the list with split{data.data}")
print(f"this is the number list as well with the split {data.number}")
print(data.string)