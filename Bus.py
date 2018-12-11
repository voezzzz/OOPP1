
class ProblemReq:
    def __init__(self, problem,description,location,datereported,username):
        self.__problem = problem
        self.__description = description
        self.__location = location
        self.__datereported = datereported
        self.__username = username
        self.__status = 'pending'

    def get_problem(self):
        return self.__problem

    def get_other(self):
        return self.__other

    def get_description(self):
        return self.__description

    def get_location(self):
        return self.__location

    def get_datereported(self):
        return self.__datereported

    def get_username(self):
        return self.__username

    def get_status(self):
        return self.__status

    def set_problems(self, problem):
        self.__problem = problem

    def set_other(self, other):
        self.__other = other

    def set_description(self, description):
        self.__description = description

    def set_location(self, location):
        self.__location = location

    def set_datereported(self, datereported):
        self.__datereported = datereported

    def set_username(self, username):
        self.__username = username

    def set_status(self, status):
        self.__status = status





