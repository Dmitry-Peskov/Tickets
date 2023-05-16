from entities import Ticket, WaitingList, Incident

if __name__ == "__main__":
    queue = WaitingList()
    t = Ticket('1', '1', '1')
    queue.add(t)
    i = Incident('1', '1', '1','1', '1', '1')
    queue.add(i)
    print(queue)
