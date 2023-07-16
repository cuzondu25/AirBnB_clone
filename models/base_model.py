#!/usr/bin/bash
"""my base module"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """my Base class"""

    def __init__(self, *args, **kwargs):
        """initialaisation of the attributes
        Attributs:
            id: unique id of each new instance
            created_at: timean instance is created
            updated_at : time an instance is updated
            models.storage.new(self):   update the storage file
        """

        x = uuid.uuid4()
        self.id = str(x)
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
            models.storage.new(self)
        else:
            models.storage.new(self)

        
    def __str__(self):
        """returns: returns the string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves an instance to assstorage"""
        self.updated_at = datetime.now()  #you can use datetime.today()
        #storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns the dictionary representation of the object"""
        my_dict = {"__class__": self.__class__.__name__}
        my_dict.update(self.__dict__)
        for key, value in my_dict.items():
            if key == "created_at":
                my_dict[key] = self.created_at.isoformat()
            if key == "updated_at":
                my_dict[key] = self.updated_at.isoformat()
        return my_dict

