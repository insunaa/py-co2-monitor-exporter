import http.server
import prometheus_client
import signal
import sys
import threading
import time
from CO2Monitor import CO2Monitor  # Assuming you have a CO2Monitor class implementation

# Initialize CO2 Monitor.
monitor = CO2Monitor()

shutdown = False

# Start Prometheus metrics exposition.
def prometheus_expose():
    prometheus_client.start_http_server(9101)

def shutdown(signum, frame):
    print('Shutting down...')
    shutdown = True
    monitor.disconnect()
    sys.exit(0)

try:
    print("Connecting to the USB device...")
    monitor.connect()
    print("Connected successfully. Initiating data transfer...")
    # Initialize Prometheus metrics.
    co2_gauge = prometheus_client.Gauge('air_co2', 'Relative Concentration of CO2 (CntR) in ppm.')
    temp_gauge = prometheus_client.Gauge('air_temp', 'Ambient Temperature (Tamb) in ℃.')
    hum_gauge = prometheus_client.Gauge('air_hum', 'Relative Humidity')
    # Register update events.
    monitor.on_temp(lambda temperature: temp_gauge.set(temperature))
    monitor.on_co2(lambda co2: co2_gauge.set(co2))
    monitor.on_hum(lambda hum: hum_gauge.set(hum))
    monitor.on_error(lambda err: print(f'Device Error: {err}'))

    prometheus_thread = threading.Thread(target=prometheus_expose)
    prometheus_thread.start()

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)
    monitor.transfer()
    print("Data transfer completed.")
except Exception as e:
    print(f"Device Error: {e}")
    monitor.disconnect()
    sys.exit(1)

while shutdown == False:
    print('Looping')
    time.sleep(1)

prometheus_thread.join()

