""" A brief Python project to better understand dictionaries.
    I created a dictionary with users and their accompanying email address
"""
names = ['Kim', 'John',' Josh']

emails = ['kim@oreilly.com', 'john@abc.com', 'josh@wickedlysmart.com']

users = {'Kim' : 'kim@oreilly.com',
         'John' : 'john@abc.com',
         'Josh' : 'john@wickedlysmart.com'}

users['Avary'] = 'avary@gmail.com' #add a user

del users['John'] #remove a user

if 'Josh' in users:
    print("Josh's email address is:", users['Josh']) #Get the email address for Josh 
