import psutil
import time
import logging

logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

def monitor_system():
    while True:
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        
        log_message = f"CPU Usage: {cpu_percent}%, Memory Usage: {memory_percent}%"
        logging.info(log_message)
        
        if cpu_percent > 80 or memory_percent > 80:
            alert_message = f"ALERT: High resource usage detected! {log_message}"
            logging.warning(alert_message)
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    monitor_system()