# AHT10 Integration on Orange Pi 3 LTS

This folder contains the complete working example for reading temperature and humidity from an AHT10 sensor over I2C on the Orange Pi 3 LTS. It includes the Python data logger, the systemd service configuration, and the notes needed to run the setup reliably on Linux.

The example logs measurements to `/var/log/aht10.csv` and also prints sensor readings to the console for quick debugging and journald/systemd visibility.

## Files in this directory

- `aht10_logger.py` — reads temperature and humidity from the AHT10 sensor and writes CSV log output
- `aht10.service` — systemd unit to run the logger automatically at boot
- `images/` — optional folder for wiring and terminal screenshots related to this project

## Overview

The AHT10 sensor is connected to the Orange Pi 3 LTS through the I2C bus. The logger performs the required startup sequence, waits for the sensor to become ready, reads calibrated temperature and humidity values, and writes them in CSV format.

This project is a practical example of:

- I2C communication on Linux
- userspace hardware access
- sensor polling and decoding
- systemd service integration
- embedded Linux logging and debugging

## Hardware setup

### Wiring

Use the AHT10 module with the standard I2C interface:

- VCC -> 3.3V
- GND -> GND
- SDA -> I2C SDA line
- SCL -> I2C SCL line

On the Orange Pi 3 LTS, use the correct I2C bus for your board revision and the relevant GPIO pins. In the examples used in this repository, the sensor was connected to the board's I2C bus and verified through the `i2cdetect` / Python logger workflow.

## Software setup

### 1. Install required packages

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install smbus2
```

### 2. Verify the I2C bus

```bash
sudo i2cdetect -y 0
```

If the AHT10 is detected successfully, you should see its I2C address in the scan output.

### 3. Run the logger manually

```bash
python3 Aht10integration/aht10_logger.py 0
```

This uses I2C bus `0` by default. If your device is connected to a different bus, pass the bus number as the first argument.

Example output:

```text
2026-09-30 13:22:42,27.21,86.6
2026-09-30 13:22:47,27.24,87.7
2026-09-30 13:22:52,27.26,86.6
```

## Service installation

To install the logger as a background service:

```bash
sudo cp Aht10integration/aht10.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now aht10.service
```

Check the status:

```bash
sudo systemctl status aht10.service
```

The service file expects the script to exist at:

```text
/home/orangepi/Documents/orange_pi3_lts_Lab/Aht10integration/aht10_logger.py
```

If your repo is stored in a different location, update the `ExecStart` line in `aht10.service` before enabling it.

## Log output

The logger writes values in CSV format to `/var/log/aht10.csv`.

Example file content:

```csv
2026-09-30 13:22:42,27.21,86.6
2026-09-30 13:22:47,27.24,87.7
2026-09-30 13:22:52,27.26,86.6
```

The first value is the timestamp, followed by temperature and humidity.

## Systemd and troubleshooting

### Check service logs

```bash
journalctl -u aht10.service -f
```

### Common issues

- Sensor not detected on I2C bus: verify the bus number and hardware wiring
- Permission errors: ensure the script path and service file match your repo location
- No CSV output: confirm the script is running and the logger has permission to write to `/var/log/`
- Wrong sensor readings: check power supply, cable connections, and whether the board is using the expected I2C bus

## Reference and project location

The complete project documentation is linked from the main repository README:

- `README.md` in the repository root
- `Aht10integration/README.md` for the detailed sensor setup and service notes

This keeps the top-level project overview clean while keeping the hardware-specific instructions close to the actual code and service files.

## Screenshots

This section is intended for images related to the sensor setup, wiring, terminal output, and systemd verification.

Recommended screenshot files to keep in this folder:

- `images/aht10_wiring.jpg`
- `images/aht10_terminal_output.png`
- `images/aht10_systemctl_status.png`
- `images/aht10_i2c_detect.png`

Add the images in the `images/` directory and then reference them here if needed.

## Summary

This AHT10 integration is a good example of a practical embedded Linux workflow:

1. connect a sensor to the board
2. read it via I2C from userspace
3. process and log values in Python
4. run the logger as a service with systemd
5. validate the system with real measurements

This directory is intentionally kept focused and easy to follow so it can serve as a clean reference for future board-level sensor experiments.
