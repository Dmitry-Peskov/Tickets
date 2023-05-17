from entities import WaitingList, Incident

# создаем список ожидания
queue = WaitingList()
# генерируем 10 инцидентов и кладём в список ожидания
for i in range(1, 11):
    incident = Incident(number=str(i),
                        creator='Дмитрий',
                        article='Нет сценария',
                        state='Активный',
                        executor='Денис',
                        description=f'Тестовый инцидент № {i}',
                        priority='Блокирующий')
    queue.add(incident)
# смотрим что есть в очереди
print(queue)
# извлекаем из очереди самый первый инцидент
inc_1 = queue.pop_left()
print(f'Забрали инцидент: {inc_1}\nВ списке остались инциденты:\n{queue}')
# тоже самое но с другого конца
inc_2 = queue.pop_right()
print(f'Забрали инцидент: {inc_2}\nВ списке остались инциденты:\n{queue}')
# можем бежать по очереди в цикле
for inc in queue:
    print(inc)
# можем обратиться к любому свойству конкретного инцидента, например к приоритету
print(inc_2.priority)
# у некоторых можем поменять значение
inc_2.article = 'Есть сценарий'
print(inc_2.article)
# я могу сравнить два инцидента друг с другом
print(inc_1 == inc_2)
print(inc_1 != inc_2)
# но не для каждого свойства можно присвоить значение в принципе или значение от балды
inc_2.priority = 'Бриллиантовый'
