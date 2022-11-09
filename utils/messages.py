from db.user import get_all_user_information

START_MESSAGE = "Привет"
NOT_ADMIN = "Вы не состоите в базе админов!"
ADMIN_MENU = "Добро пожаловать в Админку!\nВыберите действие:"
EDIT_POSIBILITIES = "Выберите аккаунт:"
UPDATED = "Изменения учтены!"
ERROR = "Ошибка!"

SEND_DOCUMENT = "Отправьте фото или документ:"
WRITE_DESCRIPTION = "Напишите описание:"
SHOW_ID_TEXT = "Показать ID"


def SHOW_ID(id: int):
    return f"Ваш ID: {id}\nПерешлите его админу"


def get_all_posibilities():
    information = get_all_user_information()
    message = ""
    for i in information:
        can_pay = '+' if i[3] else '-'
        can_approve = '+' if i[2] else '-'
        can_create = '+' if i[1] else '-'
        message += f"Пользователь: {i[4]} ({i[0]})\nМожет платить: {can_pay}\nМожет согласовывать: " \
                   f"{can_approve}\nМожет создавать: {can_create}\n\n"
    return message
