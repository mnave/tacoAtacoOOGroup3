from UserList import UserList


class ServicesList(UserList):

    def __init__(self, list=None):
        if list is None:
            UserList.__init__(self)
        else:
            UserList.__init__(self, list)
