import sys
import logging


def error_message_detail(error, error_detail:sys):
    # The line _ , _, exc_tb = error_detail.exc_info() is used to extract the traceback object from an exception in Python.
    # error_detail.exc_info() returns a tuple containing:
    # The exception type
    # The exception value (the actual error message)
    # The traceback object (exc_tb), which contains information about where the exception occurred.
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in Python Script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
        )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

            