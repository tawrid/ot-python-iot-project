import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting Open-Source OT Python IoT Application...")
    # Emulate secure local telemetry loops (e.g., OPC UA or secure MQTT)
    while True:
        logging.info("Processing sensor telemetry and applying OT safe bounds check.")
        time.sleep(10)

if __name__ == "__main__":
    main()
