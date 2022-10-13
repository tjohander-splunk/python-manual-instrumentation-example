# python-manual-instrumentation-example

To try this out:
1. Create an `.env` file in the project root.  Add in three env vars:
```
SPLUNK_ACCESS_TOKEN=<some-valid-token>
SPLUNK_REALM=<your-o11y-realm>
SPLUNK_MEMORY_TOTAL_MIB=1024
```
2. Make sure Docker is running on your local machine and fire up the Collector: `docker-compose up -d`
3. Launch the app with the bootstrap script: `./send-telemetry-to-collector.sh`