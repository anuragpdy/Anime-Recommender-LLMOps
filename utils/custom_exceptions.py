import sys

class CustomException(Exception):
    """
    Custom exception class to provide detailed error messages including
    the file name and line number.
    """
    def __init__(self, message: str, error_detail: Exception = None):
        # The detailed message is constructed using system exception info
        # to find the file and line where the error occurred.
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        
        self.error_message = (
            f"{message} | Error: {str(error_detail)} "
            f"| File: {file_name} | Line: {line_number}"
        )
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message