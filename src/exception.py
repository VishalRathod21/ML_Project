import sys 
import logging
def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and its details and returns a formatted string with the error message.
    """
    _,_,exc_tb = error_detail.exc_info()  # Get the error details\
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename where the error occurred
    error_message = "Error occurred in script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)  # Format the error message
    )  # Correctly close the format method
    return error_message  # Return the formatted error message
    

class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It takes an error and its details and raises a formatted error message.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Call the parent constructor with the error message
        self.error_message = error_message_detail(error_message, error_detail)  # Get the formatted error message
        logging.info(self.error_message)
    def __str__(self):
        return self.error_message  # Return the formatted error message when the exception is printed
    


     