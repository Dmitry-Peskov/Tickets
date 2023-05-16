class InvalidTicketState(ValueError):
    def __init__(self, value):
        super().__init__(f"Не корректное значение '{value}' для свойства state")


class InvalidTicketPriority(ValueError):
    def __init__(self, value):
        super().__init__(f"Не корректное значение '{value}' для свойства priority")


class AddInWaitingListInvalidType(TypeError):
    def __init__(self, value):
        super().__init__(f"В список ожидания не возможно поместить объект типа: {type(value)}")
