# Use the nomenclature rule: [CONSTANT TYPE]_[VARIABLE NAME]
# Each const should be separated from other with two empty lines


LIST_OF_WORKING_TIME = ['10:00', '11:00', '12:00', '13:00',
                        '14:00', '15:00', '16:00', '17:00',
                        '18:00', '19:00', '20:00', '21:00']


LIST_OF_DURATIONS = ['30 минут', '1 час',
                     '1,5 часа', '2 часа',
                     '2,5 часа', '3 часа']


REGEX_TIME = r'(?:[^\d:]|^)\b(?=\d+:\d)((?:(?:2[0-3]|[0-1]?[0-9]):(?=\d\d))?(?:[0-5]?[0-9]:)?[0-5][0-9])\b'


TOKEN_TELEGRAM_BOT = '643902066:AAGVpWolpa4vLW7OR-CHYurHilJqLR5ASsM'


LIST_OF_ADMINS = [116486112]


URL_QR_CODE = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={} заказал {} в {} на {}'
