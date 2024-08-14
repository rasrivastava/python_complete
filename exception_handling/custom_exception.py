class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(e)

