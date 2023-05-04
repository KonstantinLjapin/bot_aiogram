import logging


def bot_log(message_id):
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(message_id)


if __name__ == '__main__':
    logging.warning('This is a warning message!')
