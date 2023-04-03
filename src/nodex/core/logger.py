import sys
import os

class Logger:
    @staticmethod
    def log(message):
        frame = sys._getframe()
        lineno = frame.f_back.f_lineno
        filename = frame.f_back.f_code.co_filename.split(os.sep)[-1]

        if type(message) == list:
            message = " " + ''.join(str([str(item) for item in message])) + " "

        message = str(message)
        message = f"[{filename}:{lineno}] " + message
        print(message)
