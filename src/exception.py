import sys
from logger import logging

def error_message_detail(error, error_detail:sys):
    _, _, exe_tb = error_detail.exc_info()
    error_message = "Error occured in Python script named [{0}] line number [{1}] error message [{2}]".format(
        exe_tb.tb_frame.f_code.co_filename, exe_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self) -> str:
        return self.error_message

