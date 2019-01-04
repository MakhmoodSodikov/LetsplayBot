import message_frames as msg
import markups as mrk
import telegram
import constants as const


# Class for implementing new client's current order details
class NewOrder:
    room_type = str()
    date = None
    time = None
    duration = None
    is_done = False
    is_paid = False

    def __init__(self):
        self.room_type = str()
        self.date = None
        self.time = None
        self.is_done = False
        self.is_paid = False


# Class for implementing new client's profile
class NewClient:
    id = int()
    name = str()
    username = str()
    last_order = NewOrder()
    feedback = str()
    orders = []

    def push_last_order(self):
        self.orders.append(self.last_order)
        if self.last_order.is_done:
            self.last_order = NewOrder()

    def __init__(self, id=None, name=None, username=None):
        self.id = id
        self.name = name
        self.username = username


# Class which implements new dialog details
class NewDialog:
    client = NewClient()
    id = int()

    def __init__(self, id, client=None):
        self.client = client
        self.id = id


# Class for dialogs database
class Dialogs:
    def __init__(self):
        self.dialogs_db = []
        self.curr_id = 0
        self.id_list = []

    def _find_user(self, update):
        query = update.callback_query
        user_id = query.from_user.id

        for dialog_num in range(len(self.dialogs_db)):
            # print(1, user_id)
            if self.dialogs_db[dialog_num].id == user_id:
                return dialog_num

    def _push_new_dialog(self, new_dialog):
        self.id_list.append(new_dialog.id)
        self.dialogs_db.append(new_dialog)

    def start(self, bot, update):
        print(1)
        user_id = update.message.from_user.id
        chat_id = update.message.chat_id

        if user_id not in self.id_list:
            client = NewClient(self.curr_id,
                               name=update.message.from_user.first_name,
                               username=update.message.from_user.username)
            curr_dialog = NewDialog(id=user_id,
                                    client=client)

            self._push_new_dialog(curr_dialog)

            bot.send_message(chat_id=chat_id,
                             text=msg.send_start_text.format(update.message.from_user.first_name),
                             reply_markup=mrk.start_markup(),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            self.curr_id += 1

            print(update.message.from_user.first_name, update.message.from_user.id, self.curr_id)
        else:
            bot.send_message(chat_id=chat_id,
                             text=msg.send_start_text.format(update.message.from_user.first_name),
                             reply_markup=mrk.start_markup(),
                             parse_mode=telegram.ParseMode.MARKDOWN)

    # def new_order(self, bot, update):
    #     print(0)
    #     query = update.callback_query
    #     user_id = query.from_user.id
    #
    #     for dialog_num in range(len(self.dialogs_db)):
    #         print(1, user_id)
    #         if self.dialogs_db[dialog_num].id == user_id:
    #             print(2)
    #             if update.callback_query:
    #                 print(3)
    #                 self.handle_query(bot, update, dialog_num)

    # def handle_query(self, bot, update, dialog_num):
    #     print(4)
    #     rooms = ['lux_room', 'easy_room', 'vip_room']
    #     query_data = update.callback_query.data
    #
    #     if query_data == 'take_an_order':
    #         self.send_take_order(bot, update)
    #     if query_data in rooms:
    #         self.dialogs_db[dialog_num].last_order.room_type = query_data
    #         self.send_ask_time(bot, update)
    #     # here should be other IF-conditions

    def reset_room(self, bot, update):
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.ask_reset_room_text,
                         reply_markup=mrk.room_types_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def reset_time(self, bot, update):
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.ask_reset_time_text,
                         reply_markup=mrk.time_chart_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def reset_duration(self, bot, update):
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.ask_reset_duration_text,
                         reply_markup=mrk.duration_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def send_ask_room(self, bot, update):
        dialog = self._find_user(update)
        self.dialogs_db[dialog].client.push_last_order()

        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.ask_room_type_text,
                         reply_markup=mrk.room_types_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def send_ask_time(self, bot, update, room_type):
        dialog = self._find_user(update)
        self.dialogs_db[dialog].client.last_order.room_type = room_type
        room_types_dict = {'lux_room': 'LUX-комнату',
                           'vip_room': 'VIP-комнату',
                           'easy_room': 'Общий Зал'}
        print(room_type)
        msg_text = msg.ask_time_text.format(room_types_dict[room_type])

        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg_text,
                         reply_markup=mrk.time_chart_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def send_ask_duration(self, bot, update, time):
        print(time)
        dialog = self._find_user(update)
        self.dialogs_db[dialog].client.last_order.time = time

        print(self.dialogs_db[dialog].client.last_order.room_type,
              self.dialogs_db[dialog].client.last_order.time,
              self.dialogs_db[dialog].client.id,
              self.dialogs_db[dialog].client.username)

        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.ask_duration_text,
                         reply_markup=mrk.duration_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def send_verify(self, bot, update, duration):
        dialog = self._find_user(update)
        self.dialogs_db[dialog].client.last_order.duration = duration
        room_dict = {'lux_room': 'LUX-комнату',
                     'vip_room': 'VIP-комнату',
                     'easy_room': 'комнату из Общего Зала'}
        dur_dict = {'hlf_hour': '30 минут',
                    'one_hour': '1 час',
                    'one_hlf_hour': '1,5 часа',
                    'two_hours': '2 часа',
                    'two_hlf_hours': '2,5 часа',
                    'three_hours': '3 часа'}

        room = self.dialogs_db[dialog].client.last_order.room_type
        time = self.dialogs_db[dialog].client.last_order.time
        duration = self.dialogs_db[dialog].client.last_order.duration
        print(msg.ask_verify_text.format(room_dict[room], time, dur_dict[duration]))
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.ask_verify_text.format(room_dict[room], time, dur_dict[duration]),
                         reply_markup=mrk.verify_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def verify_order(self, bot, update):
        dialog = self._find_user(update)
        chat_id = self.dialogs_db[dialog].id
        client = self.dialogs_db[dialog].client
        room_dict = {'lux_room': 'LUX-комнату',
                     'vip_room': 'VIP-комнату',
                     'easy_room': 'Комнату из Общего Зала'}
        dur_dict = {'hlf_hour': '30 минут',
                    'one_hour': '1 час',
                    'one_hlf_hour': '1,5 часа',
                    'two_hours': '2 часа',
                    'two_hlf_hours': '2,5 часа',
                    'three_hours': '3 часа'}

        bot.send_photo(chat_id=chat_id, photo=const.URL_QR_CODE.format(client.name,
                                                                       room_dict[client.last_order.room_type],
                                                                       client.last_order.time,
                                                                       dur_dict[client.last_order.duration]))
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.verify_text.format(client.name),
                         reply_markup=mrk.again_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def feedback(self, bot, update):
        bot.send_message(chat_id=update.callback_query.from_user.id,
                         text=msg.left_feedback_text,
                         reply_markup=mrk.exit_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    def feedback_handle(self, bot, update):
        query = update.message
        user_id = query.from_user.id
        dialog_num = 0
        for dialog in range(len(self.dialogs_db)):
            if self.dialogs_db[dialog].id == user_id:
                dialog_num = dialog
        client = self.dialogs_db[dialog_num].client
        client.feedback = update.message.text
        print(update.message.text)
        bot.send_message(chat_id=self.dialogs_db[dialog_num].id,
                         text=msg.thanks_for_feedback_text,
                         reply_markup=mrk.exit_markup(),
                         parse_mode=telegram.ParseMode.MARKDOWN)

    # TODO
    # DICTS SHOULD BE MOVED TO CONSTS
    # MANAGE DEPENDENCIES
    # ADD FUNCTION TO CHOOSE DAY
