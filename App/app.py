import requests
import time
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import (
    OTLPMetricExporter,
)
from opentelemetry.metrics import (
    get_meter_provider,
    set_meter_provider,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter

exporter = OTLPMetricExporter(endpoint='localhost:4317', headers=None, insecure=True)
console_exporter = ConsoleMetricExporter()
reader = PeriodicExportingMetricReader(exporter)
console_reader = PeriodicExportingMetricReader(console_exporter)
provider = MeterProvider(metric_readers=[reader, console_reader])
set_meter_provider(provider)
meter = get_meter_provider().get_meter("otel-demo")
counter = meter.create_counter("otel-demo-counter")
tracer = trace.get_tracer(__name__)

for i in range(5):
    with tracer.start_as_current_span(name="span-name") as span:
        span.set_attribute("span-attribute", "attribute-value")
        span.set_attribute("is_api_call", "true")
        requests.get('http://api.github.com')
        print("{}...".format(i))
        time.sleep(1)

counter.add(1, attributes={
    "attribute-key": "my-counter-attribute",
    "another-attribute-key": "another-attribute-value"
})
