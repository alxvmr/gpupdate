from datetime import datetime
import ipdb


class Report():
    type_obj = "report"

    def __init__(self, d):
        self._domain = d
        self._warnings = []
        self._errors = []
        self._gpos = []
        self._gpos_applied = []
        self._gpos_not_applied = []
        self._admtempls = []
        self._regkeys = []
        self._timestamp = str(datetime.now())
    
    @property
    def domain(self):
        return self._domain
    
    @property
    def gpos(self):
        return self._gpos
    
    @property
    def warnings(self):
        return self._warnings

    @property
    def errors(self):
        return self._errors
    
    @property
    def timestamp(self):
        return self._timestamp
    
    @property
    def admtempls(self):
        return self._admtempls
    
    @property
    def regkeys(self):
        return self._regkeys
    
    @domain.setter
    def domain(self, d):
        self._domain = d
    
    @gpos.setter
    def gpos(self, gpo):
        for g in self._gpos:
            if g.name == gpo.name:
                return
        self._gpos.append(gpo)

    @warnings.setter
    def warnings(self, w):
        self._warnings.append(w)

    @errors.setter
    def errors(self, e):
        self._errors.append(e)

    @admtempls.setter
    def policies(self, p):
        for p_exist in self._admtempls:
            if p_exist.get_info_dict() == p.get_info_dict():
                return
            
        self._admtempls.append(p)

    @regkeys.setter
    def regkeys(self, rk):
        for rk_exist in self._regkeys:
            if rk_exist.get_info_dict_full() == rk.get_info_dict_full():
                return
        self._regkeys.append(rk)

    @property
    def is_machine(self):
        return self._is_machine

    def get_gpos_dict(self):
        return [gp.get_info_dict() for gp in self.gpos]
    
    def get_warnings_dict(self):
        return [w.get_info_dict() for w in self.warnings]
    
    def get_errors_dict(self):
        return [e.get_info_dict() for e in self.errors]
    
    def get_admtempls_dict(self):
        return [p.get_info_dict() for p in self.admtempls]
    
    def get_regkeys_dict(self):
        d = {}
        for rk in self.regkeys:
            cur = d.get(rk.keyname, [])
            cur.append(rk.get_info_dict_without_keyname())
            d[rk.keyname] = cur
        return d
    
    def get_info_dict(self):
        return {
            "timestamp": self.timestamp,
            "is_machine": str(self.is_machine),
            "domain": self.domain,
            "summary": {
                "errors":self.get_errors_dict(),
                "warnings":self.get_warnings_dict(),
                "type":"summary"
            },
            "details":{
                "gpos": self.get_gpos_dict(),
                "admtempls" : self.get_admtempls_dict(),
                "regkeys" : self.get_regkeys_dict()
            }
        }


class ReportComputer(Report):
    type_obj = "report_computer"
    _is_machine = True

    def __init__(self, name, domain=None):
        self._name = name
        super().__init__(domain)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        self._name = n

    def set_gpo(self, gpo):
        self.gpos = gpo

    def set_warning(self, w):
        self.warnings = w

    def set_error(self, e):
        self.errors = e

    def get_info_dict(self):
        d = {
            "computer_name":self.name,
            "type":self.type_obj
        }
        d_s = super().get_info_dict()
        return {**d, **d_s}


class ReportUser(Report):
    type_obj = "report_user"
    _is_machine = False

    def __init__(self, user_name=None, computer_name=None, domain=None):
        self._user_name = user_name
        self._computer_name = computer_name
        super().__init__(domain)
        #self.machine = ReportComputer()

    @property
    def user_name(self):
        return self._user_name
    
    @property
    def computer_name(self):
        return self._computer_name
    
    @user_name.setter
    def user_name(self, name):
        self._user_name = name

    @computer_name.setter
    def computer_name(self, name):
        self._computer_name = name

    def set_gpo(self, gpo):
        self.gpos = gpo

    def set_warning(self, w):
        self.warnings = w

    def set_error(self, e):
        self.errors = e

    def get_info_dict(self):
        d = {
            "computer_name":self.computer_name,
            "user_name":self.user_name,
            "type":self.type_obj
        }
        d_s = super().get_info_dict()
        return {**d, **d_s}