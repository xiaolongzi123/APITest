import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
class IsInstance:

    def get_instance(self, value, check):
        flag = None
        if isinstance(value, str):
            # if check == value:
            if check in value:
                flag = True
            else:
                flag = False
        elif isinstance(value, float):
            if value - float(check) == 0:
                flag = True
            else:
                flag = False
        elif isinstance(value, int):
            if value - int(check) == 0:
                flag = True
            else:
                flag = False
        return flag
