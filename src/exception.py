import sys

def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_msg = str(error)
    error_message = f"Error occured in python script name: {file_name}, line number: {line_no}, error message: {error_msg}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


