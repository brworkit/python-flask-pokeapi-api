class NotFoundException(Exception):
    """Exception for account errors"""
    def __init__(self, message):
        super().__init__(message)
