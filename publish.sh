#!/bin/sh

rm -rf build dist lambda_parse_sqs.egg-info

python setup.py sdist bdist_wheel

python -m twine upload dist/*