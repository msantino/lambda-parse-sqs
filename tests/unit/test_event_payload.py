import json
import unittest
from lambda_parse_sqs import parse_messages
from lambda_parse_sqs.errors import RecordsNotFoundException
from tests.fixture import load_json_as_dict

# payloads to test
INVALID_EVENT_PAYLOAD = load_json_as_dict("invalid_event_payload")
VALID_EMPTY_EVENT_PAYLOAD = load_json_as_dict("valid_empty_event_payload")
VALID_NOT_EMPTY_EVENT_PAYLOAD = load_json_as_dict("valid_not_empty_event_payload")


class TestEventPayload(unittest.TestCase):
    
    def test_should_raise_error_when_invalid_payload(self):
        self.assertRaises(RecordsNotFoundException, parse_messages, INVALID_EVENT_PAYLOAD)
    
    def test_should_raise_error_when_valid_empty_payload(self):
        self.assertRaises(RecordsNotFoundException, parse_messages, VALID_EMPTY_EVENT_PAYLOAD)
    
    def test_not_empty_payload_size(self):
        self.assertEqual(len(VALID_NOT_EMPTY_EVENT_PAYLOAD['Records']), len(parse_messages(VALID_NOT_EMPTY_EVENT_PAYLOAD)))