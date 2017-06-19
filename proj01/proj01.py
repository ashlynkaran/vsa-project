# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

print "Hello world!"

age = int(raw_input("Enter your age: "))
name = raw_input("Enter your name: ")

if age == 10:
    print "you're 10"
    if name == "Matthew":
        print "Matthew's great!"

elif age == 20:
    print "you're 20"
else:
    print "you're not 10 or 20."
