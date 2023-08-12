#!/usr/bin/python3

"""This module creates an instance of the FileStorage class"""

import json
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
