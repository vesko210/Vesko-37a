import random

class MissingParameterError(Exception):
    pass

class InvalidParameterError(Exception):
    def __init__(self, invalid_parameter):
        message = (f"Invalid class parameter: {invalid_parameter}")
        super().__init__(message)

class InvalidAgeError(InvalidParameterError):
    def __init__(self, invalid_parameter, ):
        super().__init__(invalid_parameter)

class InvalidSoundError(InvalidParameterError):
    pass


class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
