from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler
import constants as const
import models


if __name__ == '__main__':
    updater = Updater(token=const.TOKEN_TELEGRAM_BOT)
    dispatcher = updater.dispatcher

    dialogs = models.Dialogs()
    # ------------------------------------------------------

    start_command_handler = CommandHandler('start',
                                           lambda bot, update: dialogs.start(bot, update))
    new_order_handler = CallbackQueryHandler(pattern='take_an_order',
                                             callback=lambda bot, update: dialogs.send_ask_room(bot, update))
    room_type_handler_st = CallbackQueryHandler(pattern='lux_room',
                                                callback=lambda bot, update: dialogs.send_ask_time(bot,
                                                                                                   update,
                                                                                                   'lux_room'))
    room_type_handler_ea = CallbackQueryHandler(pattern='easy_room',
                                                callback=lambda bot, update: dialogs.send_ask_time(bot,
                                                                                                   update,
                                                                                                   'easy_room'))
    room_type_handler_vi = CallbackQueryHandler(pattern='vip_room',
                                                callback=lambda bot, update: dialogs.send_ask_time(bot,
                                                                                                   update,
                                                                                                   'vip_room'))
    reset_time_handler = CallbackQueryHandler(pattern='reset_time',
                                              callback=lambda bot, update: dialogs.reset_time(bot,
                                                                                              update))
    reset_room_handler = CallbackQueryHandler(pattern='reset_room',
                                              callback=lambda bot, update: dialogs.reset_room(bot,
                                                                                              update))
    time_handler_0 = CallbackQueryHandler(pattern='10:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '10:00'))
    time_handler_1 = CallbackQueryHandler(pattern='11:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '11:00'))
    time_handler_2 = CallbackQueryHandler(pattern='12:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '12:00'))
    time_handler_3 = CallbackQueryHandler(pattern='13:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '13:00'))
    time_handler_4 = CallbackQueryHandler(pattern='14:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '14:00'))
    time_handler_5 = CallbackQueryHandler(pattern='15:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '15:00'))
    time_handler_6 = CallbackQueryHandler(pattern='16:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '16:00'))
    time_handler_7 = CallbackQueryHandler(pattern='17:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '17:00'))
    time_handler_8 = CallbackQueryHandler(pattern='18:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '18:00'))
    time_handler_9 = CallbackQueryHandler(pattern='19:00',
                                          callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                 update,
                                                                                                 '19:00'))
    time_handler_10 = CallbackQueryHandler(pattern='20:00',
                                           callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                  update,
                                                                                                  '20:00'))
    time_handler_11 = CallbackQueryHandler(pattern='21:00',
                                           callback=lambda bot, update: dialogs.send_ask_duration(bot,
                                                                                                  update,
                                                                                                  '21:00'))
    duration_handler_0 = CallbackQueryHandler(pattern='hlf_hour',
                                              callback=lambda bot, update: dialogs.send_verify(bot,
                                                                                               update,
                                                                                               'hlf_hour'))

    duration_handler_1 = CallbackQueryHandler(pattern='one_hour',
                                              callback=lambda bot, update: dialogs.send_verify(bot,
                                                                                               update,
                                                                                               'one_hour'))

    duration_handler_2 = CallbackQueryHandler(pattern='one_hlf_hour',
                                              callback=lambda bot, update: dialogs.send_verify(bot,
                                                                                               update,
                                                                                               'one_hlf_hour'))

    duration_handler_3 = CallbackQueryHandler(pattern='two_hours',
                                              callback=lambda bot, update: dialogs.send_verify(bot,
                                                                                               update,
                                                                                               'two_hours'))

    duration_handler_4 = CallbackQueryHandler(pattern='two_hlf_hours',
                                              callback=lambda bot, update: dialogs.send_verify(bot,
                                                                                               update,
                                                                                               'two_hlf_hours'))

    duration_handler_5 = CallbackQueryHandler(pattern='three_hours',
                                              callback=lambda bot, update: dialogs.send_verify(bot,
                                                                                               update,
                                                                                               'three_hours'))
    duration_reset_handler = CallbackQueryHandler(pattern='reset_duration',
                                                  callback=lambda bot, update: dialogs.reset_duration(bot,
                                                                                                      update))
    verify_order_handler = CallbackQueryHandler(pattern='verify_order',
                                                callback=lambda bot, update: dialogs.verify_order(bot,
                                                                                                  update))
    left_feedback_handler = CallbackQueryHandler(pattern='feedback',
                                                 callback=lambda bot, update: dialogs.feedback(bot,
                                                                                               update))
    feedback_handler = MessageHandler(filters=Filters.text,
                                      callback=lambda bot, update: dialogs.feedback_handle(bot,
                                                                                           update))
    # DON'T FORGET TO ADD TO DISPATCHER, MOTHERFUCKER!
    # | | | |
    # v v v v
    # ------------------------------------------------------
    dispatcher.add_handler(duration_handler_0)
    dispatcher.add_handler(duration_handler_1)
    dispatcher.add_handler(duration_handler_2)
    dispatcher.add_handler(duration_handler_3)
    dispatcher.add_handler(duration_handler_4)
    dispatcher.add_handler(duration_handler_5)
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(new_order_handler)
    dispatcher.add_handler(room_type_handler_st)
    dispatcher.add_handler(room_type_handler_ea)
    dispatcher.add_handler(room_type_handler_vi)
    dispatcher.add_handler(time_handler_0)
    dispatcher.add_handler(time_handler_1)
    dispatcher.add_handler(time_handler_2)
    dispatcher.add_handler(time_handler_3)
    dispatcher.add_handler(time_handler_4)
    dispatcher.add_handler(time_handler_5)
    dispatcher.add_handler(time_handler_6)
    dispatcher.add_handler(time_handler_7)
    dispatcher.add_handler(time_handler_8)
    dispatcher.add_handler(time_handler_9)
    dispatcher.add_handler(time_handler_10)
    dispatcher.add_handler(time_handler_11)
    dispatcher.add_handler(reset_room_handler)
    dispatcher.add_handler(reset_time_handler)
    dispatcher.add_handler(duration_reset_handler)
    dispatcher.add_handler(verify_order_handler)
    dispatcher.add_handler(left_feedback_handler)
    dispatcher.add_handler(feedback_handler)
    # ------------------------------------------------------

    updater.start_polling(clean=True)
    # ------------------------------------------------------

    updater.idle()
