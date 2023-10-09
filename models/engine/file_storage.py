#!/usr/bin/python3
"""FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage props"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set __objects"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize objects to JSON and it save to file"""
        objs_dict = FileStorage.__objects
        data = {obj: objs_dict[obj].to_dict() for obj in objs_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Deserialize file objects, if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
                for obj in data.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
