#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models
# from models.engine.file_storage import FileStorage

class BaseModel:

    """ Base class for all our classes """

    def __init__(self, *args, **kwargs):

        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            tosave = self.to_dict()
            models.storage.new(tosave)
        elif kwargs:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                elif(key == "created_at" or key == "updated_at"):
                    self.__dict__[key] = datetime.strptime(value,DATE_TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
            prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
             returns a dictionary containing all keys/values of __dict__ of the instance
        """
        newself = self
        newself.created_at = datetime.isoformat(self.created_at)
        newself.updated_at = datetime.isoformat(self.updated_at)
        items = newself.__dict__.copy()
        items["__class__"] = self.__class__.__name__
        return items
