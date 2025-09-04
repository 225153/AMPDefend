#!/usr/bin/env python3
import os
import datetime
import c104

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGFILE = os.path.join(BASE_DIR, "ampdefend.log")

def log_event(msg: str):
    print(msg)
    with open(LOGFILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {msg}\n")

def main():
    log_event("Starting IEC104 Honeypot via c104 library on port 2404")
    server = c104.Server(ip="0.0.0.0", port=2404)
    station = server.add_station(common_address=1)
    station.add_point(io_address=100, type=c104.Type.M_ME_NC_1, report_ms=5000)
    server.start()

    # Keep running indefinitely
    try:
        while True:
            # Potentially, monitor logs or heartbeat here
            pass
    except KeyboardInterrupt:
       log_event("IEC104 Honeypot stopped")

if __name__ == "__main__":
    main()

