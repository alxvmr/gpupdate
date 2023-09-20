class RegistryKey():
    type_obj = "regkey"
    
    def __init__(self, keyname, valuename=None, type=None, data=None):
        self._keyname = keyname
        self._valuename = valuename
        self._type = type
        self._data = data

    @property
    def keyname(self):
        return self._keyname
    
    def get_info_dict_without_keyname(self):
        return {
            "valuename" : self._valuename,
            "type_key" : self._type,
            "data" : self._data,
            "type" : "regkey"
        }

    def get_info_dict_full(self):
        d = {"keyname" : self._keyname}
        d_add = self.get_info_dict_without_keyname()
        return {**d, **d_add}