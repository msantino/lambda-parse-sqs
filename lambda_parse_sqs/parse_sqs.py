from .errors import *
from .sqs_message_parser import Parser


def parse_messages(event: dict, provider: str = None) -> list:
    """ Parse SQS event payload and return a messages list

    Parameters:
    event (list): SQS Payload sent to lambda handler
    provider (str): Provider to parse messages

    Returns:
    list: parsed messages as list
    """
    if 'Records' not in event.keys():
        raise RecordsNotFoundException("Records index not found in events.")


    if len(event.get('Records')) == 0:
        raise RecordsNotFoundException("Record messages is empty.")

    messages_list = list()
    for record in event.get('Records'):
        messages_list.append(Parser(record, provider).message)

    return messages_list
