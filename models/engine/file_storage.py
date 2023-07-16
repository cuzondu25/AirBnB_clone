#!/usr/bin/python3
"""my storage file"""
import json
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
        self.key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[self.key] = obj.__str__()
        self.obj = obj
    def dis(self):
        print(FileStorage.__objects)

    def save(self):
        """saves objects"""
        #obj_dict = {self.key: self.obj.to_dict()}
        try:
            with open(FileStorage.__file_path) as e:
                obj_dict = json.load(e)
        except FileNotFoundError:
            obj_dict = {}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            obj_dict[self.key] = self.obj.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """reloads json objects from file"""
        try:
            with open(FileStorage.__file_path, 'r') as e:
                json_dict = json.load(e)
                for keys, value in json_dict.items():
                    for key in value.key():
                        if key == "__class__":
                            del value[key]
                    self.new(eval(BaseModel(**value)))
        except Exception:
            pass
