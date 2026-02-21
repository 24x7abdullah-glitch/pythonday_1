print("i am learning python")
print("lets get to know you")

#user input
name=input("what is your name? ")
age= input("how old are you? ") 
city=input("where do you live? ")
job=input("What do you do? ")

# create a sammary 
print("You summed up")
print("Name "+ name)
print("Age "+ age)
print("city "+ city)
print("job "+ job)
print("............")

# calculate birth year(approx)
from datetime import datetime   
current_year = datetime.now().year
birth_year = current_year - int(age) 

print(name+" you are probably born in "+ str(birth_year))
print("welcome to the "+ city +" city, hope you can be a good "+job )