from xml.dom.minidom import ProcessingInstruction

courses = ["MIT","Python","Android"]
print(courses)

#Accesing an element
print(courses[0])

#looping through an array
for x in courses:
    print(x)

#adding a new element into an array
courses.append("Java")
print(courses)


#removing an element
courses.remove("Android")
print(courses)