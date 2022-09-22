# dictonary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["year"])

#List
thisdict2 = ["Ford","Mustang","1964"]
thisdict2.append("Hello2")
thisdict2.insert(1,24)
print(thisdict2)
index = int(input("Enter The Number "))
number = int(input("Enter the Number you want to insert "))
thisdict2.insert(index,number)
print(thisdict2)

#Tuple
thisdict3 = ("Ford","Mustang","1964")
print(thisdict3)
print(thisdict3[2])


#Set
thisdict4 = {"Ford","Mustang","1964"}
print(thisdict4)
#print(thisdict4[2])
#thisdict4[3] = "hello"
