#!/usr/bin/python3

"""BaseModel that defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class or parrent classes"""

    def __init__(self, *args, **kwargs):
        """initialize edited

        args:no name keyword
        kwargs: named keyword

        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>
        """

        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(
         class_name, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute updated_at with the
           current datetime edit
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary containing all keys/values of __dict__
        """

        className = self.__class__.__name__
        copy_dict = self.__dict__.copy()

        # add class to dictionaty
        copy_dict['__class__'] = className

        # convert created_at and updated_at to isoformat
        copy_dict['created_at'] = self.created_at.isoformat()
        copy_dict['updated_at'] = self.updated_at.isoformat()

        return copy_dict
