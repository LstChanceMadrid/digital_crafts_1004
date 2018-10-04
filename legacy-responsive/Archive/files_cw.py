# reading and writing files

# w = write if the file does not exist then create it if it does exist then override it
# a = append
# r = reading
# a+ = appending and reading
# w+ = writing and reading

# creating and writing text to a file
#file_object = open("todo.txt","w")
# writing Hello World to the file
#file_object.write("Bye Bye")
# closing the stream
#file_object.close()


# creating file with automatic closing of resources
#with open("todo.txt","w") as file_object:
#    file_object.write("Hello World")

# reading from the file
#with open("todo.txt","r") as file_object:
#    print(file_object.read())

# appending to the file
task_name = input("Enter task name: ")
task_priority = input("Enter task priority: ")

with open("todo.txt","a") as file_object:
    file_object.write(task_name)
    file_object.write(task_priority)
    # write an empty new line
    # \n is the code for new line
    file_object.write("\n")

tasks = []

class Task:
    def __init__(self,name):
        self.name = name

# reading file line by line
with open("todo.txt","r") as file_object:
    lines = file_object.readlines()
    for line in lines:
        task = Task(line)
        tasks.append(task)
