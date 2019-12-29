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