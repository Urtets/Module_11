import sys
from pprint import pprint
class Introspection:

    def __init__(self, any_object):
        self.type = type(any_object)
        self.help = help(any_object)
        self.methods = dir(any_object)
        self.modules = sys.modules
        self.path = sys.path
        self.argvs = sys.argv


    def introspection_info(self):
        pprint(self.type)
        pprint(self.help)
        pprint(self.methods)
        pprint(self.modules)
        pprint(self.path)
        pprint(self.argvs)

checker = Introspection(sys)
checker.introspection_info()