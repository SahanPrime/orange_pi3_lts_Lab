import spidev
import gpiod
import time

# --- PIN CONFIGURATION ---
GPIO_CHIP = 'gpiochip0' 
RESET_LINE = 2        # PL2
DC_LINE = 3           # PL3

print("1. Hooking into Control Pins (PL2 & PL3)...")
chip = gpiod.Chip(GPIO_CHIP)
reset_pin = chip.get_line(RESET_LINE)
reset_pin.request(consumer="TFT_RST", type=gpiod.LINE_REQ_DIR_OUT)
dc_pin = chip.get_line(DC_LINE)
dc_pin.request(consumer="TFT_DC", type=gpiod.LINE_REQ_DIR_OUT)

# --- SPI INITIALIZATION ---
print("2. Launching SPI Engine at 16MHz...")
spi = spidev.SpiDev()
spi.open(1, 0)
spi.max_speed_hz = 16000000  
spi.mode = 0b00              

def write_cmd(cmd):
    dc_pin.set_value(0)      
    spi.writebytes([cmd])

def write_data(data):
    dc_pin.set_value(1)      
    if isinstance(data, int):
        spi.writebytes([data])
    else:
        spi.writebytes(data)

def init_display():
    """Initializes the TFT panel grid structures."""
    reset_pin.set_value(1)
    time.sleep(0.01)
    reset_pin.set_value(0)
    time.sleep(0.05)
    reset_pin.set_value(1)
    time.sleep(0.12)

    write_cmd(0x01) # Software Reset
    time.sleep(0.01)
    
    # Generic ILI9341/ST7789 Initialization Profile
    write_cmd(0xCF); write_data([0x00, 0xC1, 0X30])
    write_cmd(0xED); write_data([0x64, 0x03, 0X12, 0X81])
    write_cmd(0xE8); write_data([0x85, 0x00, 0x78])
    write_cmd(0xCB); write_data([0x39, 0x2C, 0x00, 0x34, 0x02])
    write_cmd(0xF7); write_data([0x20])
    write_cmd(0xEA); write_data([0x00, 0x00])
    write_cmd(0xC0); write_data([0x23])
    write_cmd(0xC1); write_data([0x10])
    write_cmd(0xC5); write_data([0x3e, 0x28])
    write_cmd(0xC7); write_data([0x86])
    write_cmd(0x36); write_data([0x48]) # Memory Access
    write_cmd(0x3A); write_data([0x55]) # 16-bit color format (RGB565)
    write_cmd(0xB1); write_data([0x00, 0x18])
    
    write_cmd(0x11) # Exit Sleep Mode
    time.sleep(0.12)
    write_cmd(0x29) # Display On
    time.sleep(0.02)

    # Configure bounds (Standard 240x320 matrix)
    write_cmd(0x2A); write_data([0x00, 0x00, 0x00, 0xEF])
    write_cmd(0x2B); write_data([0x00, 0x00, 0x01, 0x3F])

def flood_screen(color_bytes):
    """Fills the panel memory canvas with a designated pixel sequence."""
    write_cmd(0x2C) # Memory write command
    packet = color_bytes * 2048
    for _ in range(80): # Enough iterations to cover standard canvas size
        write_data(packet)

# Define 16-bit RGB565 color patterns
TEST_COLORS = {
    "RED":   [0xF8, 0x00],
    "GREEN": [0x07, 0xE0],
    "BLUE":  [0x00, 0x1F],
    "WHITE": [0xFF, 0xFF],
    "BLACK": [0x00, 0x00]
}

try:
    print("3. Calibrating screen matrices...")
    init_display()
    
    print("\nStarting Dynamic Screen Test Loop. Press Ctrl+C to terminate.\n")
    while True:
        for color_name, color_bytes in TEST_COLORS.items():
            print(f" -> Displaying: {color_name}")
            flood_screen(color_bytes)
            time.sleep(1.5)

except KeyboardInterrupt:
    print("\nTest cycle interrupted. Clearing panel layout...")
    flood_screen(TEST_COLORS["BLACK"])
finally:
    spi.close()
    reset_pin.release()
    dc_pin.release()
