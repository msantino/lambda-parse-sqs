[![Actions Status](https://github.com/msantino/lambda-parse-sqs/workflows/CI/badge.svg)](https://github.com/msantino/lambda-parse-sqs/actions)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![PyPI version](https://badge.fury.io/py/lambda-parse-sqs.svg)](https://badge.fury.io/py/lambda-parse-sqs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/msantino/lambda-parse-sqs.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/msantino/lambda-parse-sqs/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/msantino/lambda-parse-sqs.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/msantino/lambda-parse-sqs/context:python)
[![Twitter Follow](https://img.shields.io/twitter/follow/msantino.svg?style=social&label=Follow)](https://twitter.com/msantino)




# Lambda Parse SQS Messages

When creating a Lambda subscription to consume SQS events, it's possible to receive multiple messages at once function invocation. So, its necessary to parse message body and iterate over multiple events. 

```bash
pip install lambda-parse-sqs
```

```python
from lambda_parse_sqs import parse_messages

def lambda_handler(event, context):

    messages = parse_messages(event)
    for message in messages:
        # Do wethever you want
```