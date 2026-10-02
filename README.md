# Orange Pi 3 LTS Lab

A hands-on embedded Linux lab for the Orange Pi 3 LTS (Allwinner H6), focused on learning from userspace GPIO experimentation to practical platform work and system integration.

This repository is a growing collection of notes, scripts, and service examples used while exploring embedded Linux on a real single-board computer.

## Overview

The goal of this project is to build practical experience with:

- Linux userspace hardware control
- I2C sensor integration
- Systemd service setup
- Embedded Linux debugging and logging
- Board bring-up fundamentals
- Yocto BSP learning and customization

## Current project content

At the moment, the repository contains a working example for reading temperature and humidity from an AHT10 sensor over I2C on the Orange Pi 3 LTS.

### AHT10 I2C logger

The `Aht10integration/` directory contains:

- `aht10_logger.py` — Python script that reads temperature and humidity from an AHT10 sensor and logs values to `/var/log/aht10.csv`
- `aht10.service` — systemd unit that runs the logger automatically at boot
- `README.md` — detailed documentation for the AHT10 integration, wiring, service setup, and troubleshooting

This example demonstrates:

- I2C bus access with `smbus2`
- sensor calibration and trigger sequence
- polling the busy flag and decoding raw sensor data
- logging measurements in CSV format
- running as a background service on Linux

For the full setup guide, wiring notes, example output, and service documentation, see:

- `Aht10integration/README.md`

## Repository structure

```text
orange_pi3_lts_Lab/
├── Aht10integration/
│   ├── README.md
│   ├── aht10_logger.py
│   ├── aht10.service
│   └── images/
├── .gitignore
├── README.md
└── LICENSE (if added later)
```

## Hardware and software used

- Board: Orange Pi 3 LTS
- SoC: Allwinner H6
- Sensor: AHT10 temperature and humidity sensor
- Interface: I2C
- Runtime: Python 3 on Linux

## Setup

### 1. Install Python dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install smbus2
```

### 2. Run the logger manually

```bash
python3 Aht10integration/aht10_logger.py 0
```

This uses I2C bus `0` by default. If your device is on a different bus, pass the bus number as the first argument.

### 3. Install the systemd service

```bash
sudo cp Aht10integration/aht10.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now aht10.service
```

The service file expects the script to live at:

```text
/home/orangepi/Documents/orange_pi3_lts_Lab/Aht10integration/aht10_logger.py
```

If your checkout is in a different location, update the `ExecStart` path in `aht10.service` before enabling it.

## Example log output

The script writes data in CSV format like this:

```csv
2026-09-29 12:00:00,24.31,52.7
2026-09-29 12:00:05,24.28,52.8
```

The values are stored in `/var/log/aht10.csv` and also printed to stdout for journald/systemd capture.

## Learning path

This repository is intentionally structured around a practical progression:

1. Userspace hardware access
2. I2C and peripheral communication
3. Linux service integration
4. Embedded system debugging and logging
5. Kernel and BSP work for the Orange Pi 3 LTS

## Notes

This project is a living lab. The repository will continue to expand as new experiments, drivers, patches, and BSP-related work are added.

The focus is on learning by doing: documenting findings, testing hardware access directly, and building a deeper understanding of how embedded Linux works on real hardware.

## License

This project is currently intended for educational and personal learning use unless a separate license is added later.

## Contact

For questions, improvements, or collaboration ideas, use the repository's issue tracker or reach out through GitHub.
