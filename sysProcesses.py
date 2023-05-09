
import re
"""Program to synthesize input as a string 
    to solve arithmetic functions and 
    return a list of values which can be used for output display"""

from operations import Operators
class Processor(Operators):

    def cleanInput(self,QString):
        """
            To clean up input and setup evaluate process
        """
        replaceableChar = ["{","}","]","[","^"]
        Replace = {
            "{":"(",
            "}":")",
            "[":"(",
            "]":")",
            "^":"**"
        }
        for char in QString:
            if char in replaceableChar:
                QString = QString.replace(char,Replace[char])
        return QString.strip()

    def evaluate(self,QString):
        QString = QString.strip()

        if not re.match('^[\d+\-*/()% ]+$',QString):
            raise ValueError()
        return eval(QString)
