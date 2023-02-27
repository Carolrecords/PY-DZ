



id_client = 0
# phone_book = {123: ('Нехаев', "Михаил", "8900111", "друг"),
# 124: ("Петров", "Сергей", "8901222", "враг")}
phone_book = {}

def menu(data: dict, id_client: int):
 while True:
    print('Выберите действие: ')
    print('1 - создать новую запись')
    print('2 - распечатать содержимое справочника')
    print('3 - импортировать данные с текстового файла')
    get = input('Введите действие: ')
    if get == '':
       print('До свидания!')
       break
    elif get == '1':
        id_client += 1
        data = create(data, id_client, get_data())
    elif get == '2':
        print_phone_book(data)
    elif get == '3':
         name_fale = get_file_name()
    else:
         print('Некорректный ввод данных, введите ещё раз: ')




def create(data: dict, id: int, elem: tuple) -> dict: # добавляет запись в существующую телефонную книгу
    data[id] = elem
    return data

def print_phone_book(data: dict) -> None:
    for key, values in data.items():
      print(f'Идентификатор: {key}, {values}')

def get_data() -> tuple: # запрашивает данные у пользователя
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return (surname, name, phone, discription)

# 1-42 61 b 62 строки
def 

menu(phone_book, id_client)

