import json
import ipdb
import os

class AdmTemplate():
    type_obj = "adm_templates"

    def __init__(self, path, name):
        desfile = json.load(open(path))
        if name == "Mozzila Firefox":
            self._info = desfile
        else:
            self._info = {"policies" : desfile}
        self._name = name

    @property
    def info(self):
        return self._info
    
    @property
    def name(self):
        return self._name
    
    def get_info_dict(self):
        d = {
            "name" : self.name,
            "type" : "pol"
        }

        return {**d, **self.info}