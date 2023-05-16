import exeptions as err
import attributes as attr


class Ticket:

    def __init__(self, number: str, creator: str, article: str, state: str = 'Активный'):
        self.__number = number
        self.__creator = creator
        self.__article = article
        self.__state = state

    @property
    def number(self):
        return self.__number

    @property
    def creator(self):
        return self.__creator

    @property
    def article(self):
        return self.__article

    @article.setter
    def article(self, article: str):
        self.__article = article

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        if state in attr.STATES:
            self.__state = state
        else:
            raise err.InvalidTicketState(value=state)


class Incident(Ticket):

    def __init__(self, number, creator, article, state, executor: str, description: str, priority: str = 'Высокий'):
        super().__init__(number, creator, article, state)
        self.__priority = priority
        self.__executor = executor
        self.__description = description

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        if value in attr.PRIORITY:
            self.__priority = value
        else:
            raise err.InvalidTicketPriority
