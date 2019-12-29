import json
import unittest
from parameterized import parameterized
from lambda_parse_sqs import Parser
from lambda_parse_sqs.errors import RecordsNotFoundException, ProviderSelectionException
from tests.fixture import load_json_as_dict

# payloads to test
SQS_PAYLOAD_GENERIC = load_json_as_dict("sqs_payload_generic")
SQS_PAYLOAD_SNS = load_json_as_dict("sqs_payload_sns")
SQS_PAYLOAD_SNS_RAW = load_json_as_dict("sqs_payload_sns_raw")

# When parsed, messages list should look like this
EXPECTED_PAYLOAD = {
    "Foo": "Bar"
}

# Expected providers list
PROVIDER_COMPARE_LIST = [
    ('_parser_generic', None),
    ('_parser_generic', 'GENERIC'),
    ('_parser_sns', 'SNS'),
    ('_parser_sns_raw', 'SNS_RAW'),
]
class TestParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser_generic = Parser(SQS_PAYLOAD_GENERIC)
        cls.parser_sns = Parser(SQS_PAYLOAD_SNS, provider='SNS')
        cls.parser_sns_raw = Parser(SQS_PAYLOAD_SNS_RAW, provider='SNS_RAW')
        
    ## Payload parsing validation
    def test_generic_parser_payload(self):
        self.assertEqual(EXPECTED_PAYLOAD, self.parser_generic.message)

    def test_sns_payload(self):
        self.assertEqual(EXPECTED_PAYLOAD, self.parser_sns.message)

    def test_sns_raw_payload(self):
        self.assertEqual(EXPECTED_PAYLOAD, self.parser_sns_raw.message)

    ## Provider validation
    @parameterized.expand(PROVIDER_COMPARE_LIST)
    def test_identify_provider(self, expected_provider, passed_provider):
        self.assertEqual(expected_provider, self.parser_generic._identify_provider(passed_provider))
    
    def test_invalid_provider_should_raise_exception(self):
        self.assertRaises(ProviderSelectionException, self.parser_generic._identify_provider, 'NOT_VALID_PROVIDER')

    ## Extract records
    