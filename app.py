import math

# print("Hello, World!")

# print("*" * 10)

# x = 1
# y = 2
# unit_price = 3

# student_count = 1000
# rating = 4.99
# is_published = False
# course_name = "Python Programming"
  
# print("Student count:", student_count)
# print("Rating:", rating)
# print("Is published:", is_published)
# print("Course name:", course_name)

#Strings
# course = "Python Programming"
# print(len(course))
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])

#Escape Sequences
#\"
# \'
#\\
#\n

# course = "Python \"Programming"
# print (course)

#Formatted Strings
# first_name = "Mavery"
# last_name = "Maverick"
# #full_name = first_name + " " + last_name
# full_name = f"{first_name} {last_name}"
# print(full_name)

# #string methods
# course = "   python programming"

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("Pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)

# #Numbers
# # x = 1
# x = 1.1
# x = 1 + 2j #a + bi

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x +  3
# x += 3


#working with numbers`
# print(round(2.9))   #round() is used for rounding off the number to the nearest integer
# print(abs(-2.9))    #abs() is used to get the absolute value of a number

# math.ceil(2.9)   #ceil() is used to round up the number to the nearest integer
# math.floor(2.9)  #floor() is used to round down the number to the nearest integer

#Type Conversion
x = input("x: ")
y = int(x) + 1

print(f"x: {x}, y: {y}")
# print(type(x))