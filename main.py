from entities import Ticket, WaitingList, Incident

if __name__ == "__main__":
    queue = WaitingList()
    for i in range(1,10):
        ticket = Incident(str(i),'Дмитрий', 'Тикет','Вася','Вася','что такое')
        queue.add(ticket)

    print(queue)
    queue.pop_right()
    print(queue)
    queue.pop_left()
    print(queue)


