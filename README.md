# Orange Pi 3 LTS Lab

A hands-on embedded Linux lab for the Orange Pi 3 LTS (Allwinner H6), focused on learning from userspace GPIO experimentation to practical platform work and system integration.

## Overview

This repository contains practical examples for:

- **I2C sensor integration** — See `Aht10integration/README.md`
- **SPI display control** — See `lcddisplay_spi/README.md`
- Systemd service setup and embedded Linux debugging
- Device tree overlays and U-Boot configuration

## Quick Start

### 1. Install dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install smbus2 spidev
```

### 2. AHT10 I2C Temperature Logger

For complete setup, wiring, and troubleshooting, see `Aht10integration/README.md`.

```bash
python3 Aht10integration/aht10_logger.py 0
```

### 3. SPI LCD Display Control

For complete setup, wiring, device tree configuration, and troubleshooting, see `lcddisplay_spi/README.md`.

```bash
sudo python3 lcddisplay_spi/lcd_display.py
```

## Repository Structure

```
orange_pi3_lts_Lab/
├── Aht10integration/
│   ├── README.md          (I2C sensor setup & service management)
│   ├── aht10_logger.py
│   ├── aht10.service
│   └── images/
├── lcddisplay_spi/
│   ├── README.md          (SPI device & display setup)
│   ├── lcd_display.py
│   └── images/
└── README.md              (this file)
```

## Hardware & Software

**Board:** Orange Pi 3 LTS (Allwinner H6)  
**Runtime:** Python 3 on Linux  
**Key Libraries:** smbus2 (I2C), spidev (SPI), gpiod (GPIO)

**Sensors & Peripherals:**
- AHT10 temperature/humidity sensor (I2C)
- SPI LCD display module (SPI bus 1)

## Documentation

- **Main README** (this file) — project overview and quick start
- **`Aht10integration/README.md`** — I2C sensor setup, calibration, and systemd service
- **`lcddisplay_spi/README.md`** — SPI device configuration, wiring, and display control

## Demonstration

- [SPI LCD Display Demonstration](https://drive.google.com/drive/folders/1jV2pZ4CKhYPPJa0x4ME6Q3aJ-s64QMXE)

## License

Educational and personal learning use. See LICENSE if added later.

## Contact

For questions or collaboration, use the repository's issue tracker or reach out via GitHub.
