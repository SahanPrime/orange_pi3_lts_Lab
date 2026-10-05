# SPI LCD Test Suite for Orange Pi 3 LTS

This directory contains Python examples for driving a TFT LCD display over the Orange Pi 3 LTS SPI bus using Linux userspace GPIO control.

The code in this folder is intended for experimentation and validation of low-level display initialization, SPI communication, and basic screen rendering on the Allwinner H6-based Orange Pi 3 LTS board.

## Overview

The examples here demonstrate how to:

- configure GPIO control lines for LCD reset and data/command selection
- initialize an SPI device in userspace using `spidev`
- send commands and data bytes to a TFT controller
- perform display reset and initialization sequences
- render basic screen fills and color patterns

These examples are written for learning and hardware bring-up purposes and are useful when developing embedded Linux interfaces for TFT panels on single-board computers.

## Hardware connection

The scripts assume a display panel connected using the Orange Pi SPI bus and a simple GPIO control interface:

- RESET line: GPIO `PL2` (Linux GPIO line 2)
- DC / D/C line: GPIO `PL3` (Linux GPIO line 3)
- SPI bus: `spidev1.0`
- SPI mode: `0b00` (Mode 0)
- SPI frequency: 16 MHz

The configuration in the scripts is:

```python
GPIO_CHIP = 'gpiochip0'
RESET_LINE = 2
DC_LINE = 3
spi.open(1, 0)
spi.max_speed_hz = 16000000
spi.mode = 0b00
```

## Wiring notes

Use the board's SPI signals and the panel's control pins consistently with your hardware setup. Typical connection logic is:

- LCD reset -> Orange Pi GPIO PL2
- LCD D/C (A0/RS) -> Orange Pi GPIO PL3
- LCD SPI MOSI -> Orange Pi SPI MOSI
- LCD SPI SCLK -> Orange Pi SPI SCLK
- LCD CS -> Orange Pi SPI CS
- LCD VCC -> 3.3V (verify panel spec)
- LCD GND -> GND

Note: Actual wiring depends on your display module and adapter board. Verify pin names, voltage, and SPI wiring before powering the panel.

## Files in this folder

### `screenred.py`

A minimal display test script that:

- initializes the control pins
- opens the SPI bus
- resets the panel
- sends a common TFT controller initialization sequence
- fills the screen with a solid red color

This is useful as a first hardware validation test to confirm that the display powers on, initializes correctly, and responds to SPI traffic.

### `multicolourtest.py`

A more feature-complete display test script that:

- configures the same GPIO and SPI setup
- initializes the panel with a standard ILI9341/ST7789-style sequence
- supports full-screen color fills and multiple patterns
- provides a framework for testing render output and pixel layout correctness

This script is better suited for verifying color rendering, memory access configuration, and panel orientation.

## Prerequisites

Install the required Python libraries on the Orange Pi:

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo pip3 install spidev gpiod
```

The scripts use both:

- `spidev` for SPI access
- `gpiod` for Linux GPIO control

## Running the examples

### 1. Validate the display is reachable

Run the red-screen test:

```bash
python3 screenred.py
```

### 2. Run a color/fill test

```bash
python3 multicolourtest.py
```

If the display is correctly wired and initialized, you should see screen output or a stable panel response during the initialization sequence.

## Expected behavior

During execution, the scripts will:

- request GPIO lines for reset and data/command control
- toggle the panel reset pin
- write command and data bytes over SPI
- initialize the TFT controller
- render a displayed screen test pattern

If the screen stays blank, the code may not be talking to the right SPI bus, the reset pin may be wired incorrectly, or the display controller may require a different initialization profile.

## Troubleshooting

Common issues:

- blank display: verify SPI wiring and chip-select configuration
- no response: confirm `gpiochip0` is the correct chip on your board
- incorrect colors or orientation: adjust memory access configuration and scan direction
- initialization hangs: check reset timing and panel power state

Useful checks:

```bash
ls /dev/spidev*
```

```bash
cat /sys/kernel/debug/gpio | head
```

```bash
sudo gpioinfo
```

## Notes

This project is a hands-on embedded Linux exercise focused on userspace hardware control. The scripts are intentionally simple and transparent to make it easier to understand the SPI and GPIO behavior behind TFT display initialization.

They are not intended to be a complete display driver library, but they provide a practical starting point for custom display control, debug output, and experimentation on the Orange Pi 3 LTS.

## Related repository context

This folder is part of the larger project:

- `SahanPrime/orange_pi3_lts_Lab`

The overall repository focuses on learning embedded Linux on the Orange Pi 3 LTS, from userspace GPIO control to practical system integration and Yocto-related experimentation.
