raw_username = "MAVERY.dev"
course_name = "azure ai cloud developer"
email = "mavery@example.com"

username = raw_username.strip().lower()
formatted_course = course_name.title()

print(username)
print(formatted_course)
print(email.upper())
print(len(username))
print("azure" in course_name)
print(course_name.replace("cloud", "AI cloud"))