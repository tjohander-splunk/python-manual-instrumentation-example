#!/bin/zsh
export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=py-metrics-test
export OTEL_SERVICE_NAME=py-metrics-test
splunk-py-trace-bootstrap
splunk-py-trace python3 ./App/app.py