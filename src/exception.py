import sys
from src.logger import logging

#main function
def error_message_detail(error,error_detail:sys):
    #exec_info return (type,value,raceback) so from that only traceback
    #traceback contains filename,line number,function calls
    _,_,exec_tb=error_detail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exec_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)#This initializes Python's original Exception class.
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message  
