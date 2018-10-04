
# importing json module because we have to use the functions associate with reading and writing json to a file
import json

class Task:
    def __init__(self,name,priority):
        self.name = name
        self.priority = priority

    def asDictionary(self):
        return self.__dict__

data = {
    "name" : "john doe"
}

task = Task("Wash the car",10)

tasks = [task.__dict__]


# task_as_a_dictionary = {"name": task.name, "priority": task.priority}

# json.dump can write the following types to a files
# Int, String, Boolean, Dictionary, Array
# Array of Dictionaries

# writing a custom object to a json file
with open("tasks.json","w") as file_object:
    json.dump(task.asDictionary(),file_object)

# writing data to a json file
#with open("tasks.json","w") as file_object:
#    json.dump(data,file_object)

# reading data from a json file
#with open("tasks.json","r") as file_object:
#    task_data = json.load(file_object)
#    print(task_data)
