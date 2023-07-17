#!/usr/bin/python3
"""my storage file"""
import json
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """my file storage class
    Attributes
        file_path:  path to storage file
        objects:    objects to be saved
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns object dictionary to be saved"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to the dictionary of objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
