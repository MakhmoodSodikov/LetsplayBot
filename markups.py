# Use the nomenclature rule: [variable name]_markup
# Each variable should be separated from other with two empty lines


from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from constants import LIST_OF_WORKING_TIME as TABLE, LIST_OF_DURATIONS as DUREX


RESET_LAST_ORDER = InlineKeyboardButton('Сбросить заказ и начать все заново', callback_data='take_an_order')
NEW_ORDER = InlineKeyboardButton('Новый заказ', callback_data='take_an_order')
CHOOSE_ANOTHER_ROOM = InlineKeyboardButton('Выбрать другую комнату', callback_data='reset_room')
CHOOSE_ANOTHER_TIME = InlineKeyboardButton('Выбрать другое время', callback_data='reset_time')
CHOOSE_ANOTHER_DURATION = InlineKeyboardButton('Выбрать другую длительность', callback_data='reset_duration')
VERIFY = InlineKeyboardButton('Подтвердить!', callback_data='verify_order')
LEFT_FEEDBACK = InlineKeyboardButton('Оставить отзыв', callback_data='feedback')

RETURN_MENU = [CHOOSE_ANOTHER_ROOM, CHOOSE_ANOTHER_TIME, RESET_LAST_ORDER]
VERIFY_MENU = [VERIFY, CHOOSE_ANOTHER_DURATION, CHOOSE_ANOTHER_ROOM, CHOOSE_ANOTHER_TIME, RESET_LAST_ORDER]
LAST_MENU = [NEW_ORDER, LEFT_FEEDBACK]


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        for i in footer_buttons:
            menu.append([i])
    return menu


def start_markup():
    button_list = [
        InlineKeyboardButton("Заказать место", callback_data='take_an_order')
    ]
    return InlineKeyboardMarkup(build_menu(button_list, 1))


def room_types_markup():
    button_list = [
        InlineKeyboardButton("VIP-комната", callback_data='vip_room'),
        InlineKeyboardButton("LUX-комната", callback_data='lux_room'),
        InlineKeyboardButton("Общий зал", callback_data='easy_room')
    ]
    return InlineKeyboardMarkup(build_menu(button_list,
                                           n_cols=2,
                                           footer_buttons=[RESET_LAST_ORDER]))


def time_chart_markup():
    default_time_mark = []
    for i in range(len(TABLE)):
        default_time_mark.append(InlineKeyboardButton(TABLE[i],
                                                      callback_data=TABLE[i]))
        # print(default_time_mark[i])
    return InlineKeyboardMarkup(build_menu(default_time_mark,
                                           n_cols=4,
                                           footer_buttons=[CHOOSE_ANOTHER_ROOM, RESET_LAST_ORDER]))


def duration_markup():
    dur_dict = {'30 минут': 'hlf_hour',
                '1 час': 'one_hour',
                '1,5 часа': 'one_hlf_hour',
                '2 часа': 'two_hours',
                '2,5 часа': 'two_hlf_hours',
                '3 часа': 'three_hours'}

    durations_menu = []
    for i in range(len(DUREX)):
        durations_menu.append(InlineKeyboardButton(DUREX[i],
                                                   callback_data=dur_dict[DUREX[i]]))
    return InlineKeyboardMarkup(build_menu(durations_menu,
                                           n_cols=2,
                                           footer_buttons=RETURN_MENU))


def verify_markup():
    return InlineKeyboardMarkup(build_menu(VERIFY_MENU, n_cols=1))


def again_markup():
    return InlineKeyboardMarkup(build_menu(LAST_MENU, n_cols=1))


def exit_markup():
    return InlineKeyboardMarkup(build_menu([NEW_ORDER], n_cols=1))
