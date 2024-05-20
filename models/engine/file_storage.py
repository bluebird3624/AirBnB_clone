#!/user/bin/python3

"""
class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""

import json


class FileStorage:
    """
    Custom class for file storage
    """
    __file_path = "dataStore.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        newObject = {}
        self.__objects[obj['__class__']+"."+ str(obj['id'])] = obj

    def save(self):
        with open(self.__file_path,"w") as file:
            string = json.dumps(self.__objects)
            # json.dump(string,file)
            file.write(string)
            file.close()

    def reload(self):
        try:
            with open(self.__file_path,"r") as file:
                data = file.read()
                self.__objects = json.loads(data)
        except FileNotFoundError:
            pass
        else:
            file.close()  
