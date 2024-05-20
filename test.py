#!/user/bin/python3
# from uuid import uuid4
# from datetime import datetime


# class BaseModel:
#     def __init__(self, *args, **kwargs):
        
#         DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

#         if not kwargs:
#             self.id = str(uuid4())
#             self.created_at = datetime.now()
#             self.updated_at = datetime.now()
#         elif(kwargs):
#             for key,value in kwargs.items():
#                 if(key == "__class__"):
#                     continue
#                 elif(key == "created_at" or key == "updated_at"):
#                     self.__dict__[key] = datetime.strptime(value,DATE_TIME_FORMAT)
#                 elif(key == "id"):
#                     self.__dict__[key] = str(value)
#                 else:
#                     self.__dict__[key] = value
                

#     def __str__(self):
#         """
#             prints: [<class name>] (<self.id>) <self.__dict__>
#         """
#         return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)
    
#     def save(self):
#         """
#             updates the public instance attribute updated_at with the current datetime
#         """
#         self.updated_at = datetime.now()

#     def to_dict(self):
#         """
#              returns a dictionary containing all keys/values of __dict__ of the instance
#         """
#         newSelf = self
#         newSelf.created_at = datetime.isoformat(self.created_at)
#         newSelf.updated_at = datetime.isoformat(self.updated_at)
#         items = newSelf.__dict__.copy()
#         items["__class__"] = self.__class__.__name__
#         return items
    


# base = BaseModel()

# # print("[{}] ".format(base.to_dict()))
# string = base.to_dict()
# base2 = BaseModel(**string)
# # print(string + "this print")


import cmd


class MyCommandline(cmd.Cmd):
    prompt = '(hbnb) '
    def do_greet(self, me):
        """Says hello to the world"""
        print("Hello World")
    def do_EOF(self, line):
        print("")
        return True
    def default(self, line):
        print(f"Unknown Command {line}")
        # return super().default(line)

if __name__ == '__main__':
    MyCommandline().cmdloop()