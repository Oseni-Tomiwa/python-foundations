# Lesson 6: for loops

# A loop repeats code so you don’t write the same line again and again.

# Without a loop:

# print("Study Python")
# print("Study Docker")
# print("Study Azure Functions")

# With a loop:

topics = ["Python", "Docker", "Azure Functions"]

for topic in topics:
    print(f"Study {topic}")

# Python reads that as:

# For every item inside topics, temporarily call it topic, then print it.

# On each pass:

# topic = "Python"
# topic = "Docker"
# topic = "Azure Functions"
# topic is only a temporary variable name. You could call it item, but a meaningful name makes your code easier to read.

# The two rules that matter
# for topic in topics:

# *for starts the loop.
# *in means “take items from.”
# *The : is required.
# *The indented code runs repeatedly.

# for topic in topics:
#     print(topic)

# The four spaces before print are not decoration. They tell Python: “this line belongs inside the loop.”

# range()

# When you want to repeat something a set number of times, use range():

# for day in range(1, 7):
#     print(f"Day {day}: Study AI-200")

for day in range(1, 7000):
    print(f"Day {day}: Study AI-200")