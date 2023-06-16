class InvalidInputException(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, message="Both Repo Owner and Repo Name are required!"):
        self.message = message
        super().__init__(self.message)
