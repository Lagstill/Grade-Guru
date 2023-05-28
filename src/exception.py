import sys

def error_msg_detail(msg, detail:sys):
    _,_,exec_traceback = detail
    error_msg = "Error occured at line " + str(exec_traceback.tb_lineno) + " in " + exec_traceback.tb_frame.f_code.co_filename + ":\n" + str(msg)
    return error_msg

class CustomException(Exception):
    def __init__(self, msg, detail:sys):
        super().__init__(msg)
        self.msg = error_msg_detail(msg, detail)
    
    def __str__(self):
        return self.msg
    