class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = [] # Adds a friends list variable to the Person class
        self.greeting_count = 0

    def __repr__(self):
        return "%s's information: %s %s" % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print "\nHello %s, I am %s!" % (other_person.name, self.name)
        self.greeting_count += 1

    def print_contact_info(self):
        print "\n%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print "\n%s has %d friends" % (self.name, len(self.friends))

# 1. Instantiate an instance object of Person
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

# 2. Instantiate another Person
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# 3. Have sonny greet jordan using the greet method
sonny.greet(jordan)

# 4. Have jordan greet sonny using the greet method
jordan.greet(sonny)

# 5. Write a print statement to print the contact info (email and phone) of Sonny.
print "\n%s's email is: %s and phone is: %s" % (sonny.name, sonny.email, sonny.phone)

# 6. Write another print statement to print the contact info of Jordan.
print "\n%s's email is: %s and phone is: %s" % (jordan.name, jordan.email, jordan.phone)

# Print out the contact info for a object instance of Person
sonny.print_contact_info()

# Add a friend to a person using list's append method.  Person class was modified by adding a friends instance variable(attribute) to it
# jordan.friends.append(sonny) # Commented so it doesn't add the friend in this manner
# sonny.friends.append(jordan) # Commented so it doesn't add the friend in this manner

# Get the number of friends a person has by using the len function on his friends
print "\n%s has %d friends" % (jordan.name, len(jordan.friends))

# Add friends using the add_friend method
jordan.add_friend(sonny)
# print "\n%s has %d friends" % (jordan.name, len(jordan.friends))

# Return the number of friends the person currently has using the num_friends method
jordan.num_friends()

# Each time the greet method is called, we'll increment greeting_count by 1
print "\n%s's greeting count: %d" % (sonny.name, sonny.greeting_count)
sonny.greet(jordan)
print "%s's greeting count: %d" % (sonny.name, sonny.greeting_count)
sonny.greet(jordan)
print "%s's greeting count: %d" % (sonny.name, sonny.greeting_count)
