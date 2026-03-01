#User inputs
user_name= input("What is your name? ")
user_age= input("What is your age?(Please insert only numoric values) ")
user_city= input("Which city are you from? " )
user_occupation= input("What is your occupation? ")

#calculations
age= int(user_age)
current_year= 2026
birth_year= current_year - age

#Results/summery
print("---Personal Information---" )
print("Name: "+user_name )
print("Age: "+user_age )
print("City: "+user_city )
print("Occupation: "+user_occupation)
print("------------")
print(user_name +", You were born in "+ str(birth_year))
print("Welcome to the " + user_city )
print("Hope you are progressing as a "+ user_occupation)
