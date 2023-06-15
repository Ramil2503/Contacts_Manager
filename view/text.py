main_menu = '''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать новый контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход
    '''

menu_choice = 'Выберите пункт меню: '
input_error = 'Некорректный ввод. Введите от 1 до 8'
book_error = 'Телефонная книга пуста или файл не открыт'

open_successful = 'Телефонная книга успешно открыта'

input_new_contact = 'Введите данные нового контакта'
new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите коммент: ']
search_word = 'Введите искомый элемент: '
# input_change_contact = 'Введите данные нового контакта'
input_index = 'Введите индекс изменяемого контакта: '
input_change_contact = 'Введите данные изменяемого контакта или Enter? чтоб оставить без изменений: '

file_saved = 'Файл успешно сохранен!'

delete_contact = 'Введите ID контакта которого хотите удалить: '
delete_error = 'ID контакта которого вы хотите удалить не сущевствует.'
contact_deleted = 'Контакт успешно удалён!'

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранен'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'
