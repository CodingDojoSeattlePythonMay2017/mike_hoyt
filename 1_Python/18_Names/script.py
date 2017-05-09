# -*- python -*-

# Assignment: Names
# Write the following function.

# Part I
# Given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Create a program that outputs:
#
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def print_students( l ):
    for i in l:
        print "{} {}".format( i['first_name'], i['last_name'] )

print "Testing print_students ..."
print_students( students )
print "End testing print_students"


# Part II
# Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

# Create a program that prints the following format
# (including number of characters in each combined name):
#
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def print_users( d ):
    for user_t in ["Students", "Instructors"]:
        print user_t
        for i in range(0, len( d[user_t] ) ):
            user = d[user_t][i]
            user_name_length = len( user['first_name'] ) + len( user['last_name'] )
            print "{} - {} {} - {}".format( (i+1), user['first_name'].upper(), user['last_name'].upper(), user_name_length )

print "Testing print_users ..."
print_users( users )
print "End testing print_users"

# Note: The majority of data we will manipulate as web developers will be hashed
# in a dictionary using key-value pairs. Repeat this assignment a few times to
# really get the hang of unpacking dictionaries, as it's a very common requirement
# of any web application.
