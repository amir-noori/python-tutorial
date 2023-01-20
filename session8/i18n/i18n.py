from .fa import message_list as FA
from .en import message_list as EN
from enum import Enum

class Lang(Enum):
    FA = 1
    EN = 2

class I18N:

    def __init__(self, lang):
        self.lang = lang
        if self.lang == Lang.FA:
            self.messages = FA
        elif self.lang == Lang.EN:
            self.messages = EN

    def message(self, key, *args):
        if args:
            return self.messages[key].format(*args)
        return self.messages[key]       

# i18n = I18N(Lang.EN)

# def print_info_i18n(message_key):
#     print(i18n.message(message_key, "test", "test2"))

# print_info_i18n("team_name")