# Orange Pi 3 LTS Lab

A hands-on embedded Linux lab for the Orange Pi 3 LTS (Allwinner H6), focused on learning from userspace GPIO experimentation to practical platform work and system integration.

This repository is a growing collection of notes, scripts, and service examples used while exploring embedded Linux on a real single-board computer.

## Overview

The goal of this project is to build practical experience with:

- Linux userspace hardware control
- I2C sensor integration
- SPI display and device communication
- Systemd service setup
- Embedded Linux debugging and logging
- Board bring-up fundamentals
- Yocto BSP learning and customization
- Device tree overlays and U-Boot configuration

## Current project content

At the moment, the repository contains working examples for:

### 1. AHT10 I2C Temperature and Humidity Logger

The `Aht10integration/` directory contains a complete example of I2C sensor integration with logging and systemd service setup.

**Features:**
- Reads temperature and humidity from an AHT10 sensor over I2C
- Logs measurements to `/var/log/aht10.csv` in CSV format
- Runs as a background systemd service
- Demonstrates sensor calibration, data decoding, and service management

**See:** `Aht10integration/README.md` for detailed setup and documentation.

### 2. SPI LCD Display Control

The `lcddisplay_spi/` directory contains a practical example of controlling an SPI-based LCD display with color support.

**Features:**
- Enables SPI device tree overlay via U-Boot
- Configures SPI bus parameters in `orangepienv.txt`
- Python-based color control and display manipulation
- Demonstrates userspace SPI device access
- LED backlight wired to 3.3V for continuous illumination

**Setup Steps:**
1. Check tree overlays in boot DTB
2. Enable `spidev1` overlay in `orangepienv.txt`
3. Add SPI bus parameters: `param_spidev_spi_bus=1, param_spi_cs=0`
4. Use Python with `spidev` module to control display colors

**See:** `lcddisplay_spi/README.md` for detailed setup guide and troubleshooting.

**Demonstration:** [Watch LCD Display in Action](https://drive.google.com/drive/folders/1jV2pZ4CKhYPPJa0x4ME6Q3aJ-s64QMXE)

## Repository structure

```text
orange_pi3_lts_Lab/
├── Aht10integration/
│   ├── README.md
│   ├── images/
│   ├── aht10_logger.py
│   ├── aht10.service
│   └── notes/
├── lcddisplay_spi/
│   ├── README.md
│   ├── images/
│   ├── lcd_display.py
│   └── notes/
├── .gitignore
├── README.md
└── LICENSE (if added later)
```

## Hardware and software used

**Board & SoC:**
- Board: Orange Pi 3 LTS
- SoC: Allwinner H6
- U-Boot: OrangePi variant

**Sensors & Peripherals:**
- AHT10 temperature and humidity sensor (I2C)
- SPI LCD display module (SPI bus 1)

**Software & Interfaces:**
- Runtime: Python 3 on Linux
- I2C communication via `smbus2`
- SPI communication via `spidev`
- Service management: systemd

## Setup

### 1. Install Python dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install smbus2 spidev
```

### 2. I2C Sensor Setup (AHT10)

For the AHT10 I2C sensor integration, follow the guide in `Aht10integration/README.md`:

```bash
python3 Aht10integration/aht10_logger.py 0
```

Then install the systemd service for automatic logging on boot.

### 3. SPI Display Setup (LCD Display)

For the SPI LCD display integration, follow the detailed steps in `lcddisplay_spi/README.md`:

**Quick Start:**
1. Edit `/boot/orangepienv.txt` and add:
   ```
   overlays=spidev1
   param_spidev_spi_bus=1
   param_spi_cs=0
   ```
2. Reboot and verify `/dev/spidev1.0` exists
3. Wire the display (VCC to 3.3V, LED to 3.3V, SPI pins to bus 1)
4. Run the Python script:
   ```bash
   sudo python3 lcddisplay_spi/lcd_display.py
   ```

### 4. Install systemd services

```bash
# For AHT10 sensor
sudo cp Aht10integration/aht10.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now aht10.service
```

Update the service file paths to match your repository location if needed.

## Example output

### AHT10 CSV Log Output

```csv
2026-09-29 12:00:00,24.31,52.7
2026-09-29 12:00:05,24.28,52.8
2026-09-29 12:00:10,24.30,52.6
```

### SPI Display Console Output

```text
Initializing SPI display...
SPI device opened: /dev/spidev1.0
Display initialized successfully
Setting color to red...
Setting color to green...
Setting color to blue...
Display control complete
```

## Learning path

This repository is intentionally structured around a practical progression:

1. **Userspace hardware access** — understanding GPIO, I2C, and SPI from Linux userspace
2. **I2C and peripheral communication** — sensor integration and data reading
3. **SPI device control** — display communication and color management
4. **Device tree and U-Boot configuration** — enabling hardware features
5. **Linux service integration** — running hardware applications as background services
6. **Embedded system debugging and logging** — understanding systemd, journald, and CSV logging
7. **Kernel and BSP work** — foundation for deeper Orange Pi 3 LTS customization

## Notes

This project is a living lab. The repository will continue to expand as new experiments, drivers, patches, and BSP-related work are added.

The focus is on learning by doing: documenting findings, testing hardware access directly, and building a deeper understanding of how embedded Linux works on real hardware.

Each project includes:
- **Step-by-step setup guides** for hardware and software
- **Complete wiring diagrams** and connection details
- **Working Python examples** demonstrating device communication
- **Troubleshooting sections** for common issues
- **Visual demonstrations** (photos and videos where applicable)

## Demonstration Links

- [SPI LCD Display Demonstration](https://drive.google.com/drive/folders/1jV2pZ4CKhYPPJa0x4ME6Q3aJ-s64QMXE) — setup, wiring, color control, and live interaction

## Reference and documentation

For detailed setup and troubleshooting:

- **Main README** (`README.md`) — this file, with project overview and quick start
- **AHT10 Integration** (`Aht10integration/README.md`) — I2C sensor setup and service management
- **SPI LCD Display** (`lcddisplay_spi/README.md`) — SPI device configuration and color control

## License

This project is currently intended for educational and personal learning use unless a separate license is added later.

## Contact

For questions, improvements, or collaboration ideas, use the repository's issue tracker or reach out through GitHub.
