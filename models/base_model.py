from datetime import datetime
import uuid
import models
class BaseModel:
    def __init__(self, *args, **kwargs):
        x = uuid.uuid4()
        self.id = str(x)
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)

        if kwargs is not {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    self.key = datetime.fromisoformat(value)
                else:
                    self.key = value

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()  #you can use datetime.today()
        #storage.new(self)
        models.storage.save()

    def to_dict(self):
        my_dict = {"__class__": self.__class__.__name__}
        my_dict.update(self.__dict__)
        for key, value in my_dict.items():
            if key == "created_at":
                my_dict[key] = self.created_at.isoformat()
            if key == "updated_at":
                my_dict[key] = self.updated_at.isoformat()
        return my_dict

