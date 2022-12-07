from account import Account

class user(Account):

    def __init__(self, name, document) -> None:
        super().__init__(name, document)