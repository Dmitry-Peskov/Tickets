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

    def __repr__(self):
        return f'{self.__class__.__name__} № {self.__number}'

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        return self.number != other.number


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
            raise err.InvalidTicketPriority(value)

    # TODO описать оставшиеся параметры класса


class WaitingList:

    def __init__(self):
        self.__collection = []

    def __repr__(self):
        return str(self.__collection)

    def __iter__(self):
        return iter(self.__collection[:])

    def add(self, ticket):
        if issubclass(ticket.__class__, Ticket):
            self.__collection.append(ticket)
        else:
            raise err.AddInWaitingListInvalidType(ticket)

    def pop_left(self) -> Incident:
        if len(self.__collection) != 0:
            inc = self.__collection.pop(0)
            return inc

    def pop_right(self) -> Incident:
        if len(self.__collection) != 0:
            inc = self.__collection.pop(-1)
            return inc

    def clear(self):
        self.__collection.clear()
