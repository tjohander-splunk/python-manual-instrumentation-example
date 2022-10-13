#!/bin/zsh
splunk-py-trace-bootstrap
OTEL_RESOURCE_ATTRIBUTES=deployment.environment=py-metrics-test \
OTEL_SERVICE_NAME=py-metrics-test \
splunk-py-trace python3 ./App/app.py