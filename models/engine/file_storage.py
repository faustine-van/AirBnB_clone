#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


class FileStorage:
    """
    save to json file  an load from json file

    - Private class ttributes:
        o __file_path: string - path to the JSON file (ex: file.json)
        o __objects: dictionary - empty but will store all objects

    - Public instance methods:
        o all(self): returns the dictionary __objects
        o new(self,obj): sets in __objects the obj with key <obj class name>.id
        o save(self): serializes __objects to the JSON file (path: __file_path)
        o reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns airthe dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{str(obj.id)}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        json_str = {}
        for key, obj in self.__objects.items():
            json_str[key] = obj.to_dict()
            with open(FileStorage.__file_path, 'w') as file:
                # convert object into json string
                json.dump(json_str, file)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                read_file = file.read()
                loaded_data = json.loads(read_file)
                for value in loaded_data.values():
                    class_name = value["__class__"]
                    self.new(eval(class_name)(**value))
        except Exception:
            pass
