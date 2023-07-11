import json
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        self.key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[self.key] = obj.__str__()
        self.obj = obj
    def dis(self):
        print(FileStorage.__objects)

    def save(self):
        obj_dict = {self.key: self.obj.to_dict()}
        with open(FileStorage.__file_path, 'a', encoding='utf-8') as f:
            json.dump(obj_dict, f)
        
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as e:
                json_dict = json.load(e)
        except Exception:
            pass

