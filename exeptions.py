class InvalidTicketState(ValueError):
    def __init__(self, value):
        super().__init__(f"Не корректное значение '{value}' для свойства state")

class InvalidTicketPriority(ValueError):
    def __init__(self, value):
        super().__init__(f"Не корректное значение '{value}' для свойства priority")