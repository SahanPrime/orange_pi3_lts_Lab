import spidev
import gpiod
import time

# --- PIN CONFIGURATION ---
GPIO_CHIP = 'gpiochip0' 
RESET_LINE = 2        # PL2
DC_LINE = 3           # PL3

print("1. Initializing Control Lines (PL2 & PL3)...")
chip = gpiod.Chip(GPIO_CHIP)

reset_pin = chip.get_line(RESET_LINE)
reset_pin.request(consumer="TFT_RST", type=gpiod.LINE_REQ_DIR_OUT)

dc_pin = chip.get_line(DC_LINE)
dc_pin.request(consumer="TFT_DC", type=gpiod.LINE_REQ_DIR_OUT)

# --- SPI INITIALIZATION ---
print("2. Opening SPI Bus at a stable 16MHz...")
spi = spidev.SpiDev()
spi.open(1, 0)               # spidev1.0
spi.max_speed_hz = 16000000  # 16 MHz is highly stable for test wires
spi.mode = 0b00              # SPI Mode 0

def write_cmd(cmd):
    dc_pin.set_value(0)      # Command Mode
    spi.writebytes([cmd])

def write_data(data):
    dc_pin.set_value(1)      # Data Mode
    if isinstance(data, int):
        spi.writebytes([data])
    else:
        spi.writebytes(data)

try:
    print("3. Executing Hardware Reset...")
    reset_pin.set_value(1)
    time.sleep(0.01)
    reset_pin.set_value(0)   # Active low reset
    time.sleep(0.05)
    reset_pin.set_value(1)   # Release reset
    time.sleep(0.12)         # Crucial delay for driver stability

    print("4. Blasting Full Initialization Matrix...")
    # Software Reset
    write_cmd(0x01)
    time.sleep(0.01)
    
    # Power Control B
    write_cmd(0xCF)
    write_data([0x00, 0xC1, 0X30])
    # Power On Sequence Control
    write_cmd(0xED)
    write_data([0x64, 0x03, 0X12, 0X81])
    # Driver Timing Control A
    write_cmd(0xE8)
    write_data([0x85, 0x00, 0x78])
    # Power Control A
    write_cmd(0xCB)
    write_data([0x39, 0x2C, 0x00, 0x34, 0x02])
    # Pump Ratio Control
    write_cmd(0xF7)
    write_data([0x20])
    # Driver Timing Control B
    write_cmd(0xEA)
    write_data([0x00, 0x00])
    
    # Power Control 1 & 2
    write_cmd(0xC0)
    write_data([0x23])
    write_cmd(0xC1)
    write_data([0x10])
    
    # VCOM Control 1 & 2
    write_cmd(0xC5)
    write_data([0x3e, 0x28])
    write_cmd(0xC7)
    write_data([0x86])
    
    # Memory Access Control (Sets up color pixel layout orientation)
    write_cmd(0x36)
    write_data([0x48]) # Standard RGB pixel order mapping
    
    # Pixel Format Set (16-bit color / RGB565)
    write_cmd(0x3A)
    write_data([0x55])
    
    # Frame Rate Control
    write_cmd(0xB1)
    write_data([0x00, 0x18])
    
    # Exit Sleep Mode
    write_cmd(0x11)
    time.sleep(0.12)
    
    # Global Display ON
    write_cmd(0x29)
    time.sleep(0.02)

    print("5. Formatting Screen Geometry bounds...")
    # Set Column Address (0 to 239)
    write_cmd(0x2A)
    write_data([0x00, 0x00, 0x00, 0xEF])
    # Set Page/Row Address (0 to 319)
    write_cmd(0x2B)
    write_data([0x00, 0x00, 0x01, 0x3F])

    print("6. Painting Canvas RED...")
    write_cmd(0x2C)          # Memory Write
    
    # Pure Red in RGB565 format: 0xF800
    red_pixel = [0xF8, 0x00]
    pixel_packet = red_pixel * 2048
    
    # Loop enough times to fill a 240x320 panel (~76,800 pixels)
    for _ in range(80):
        write_data(pixel_packet)
        
    print("\n[SUCCESS] The screen grid has initialized. Stripes should be gone and replaced by RED!")

except KeyboardInterrupt:
    print("\nTest stopped.")
finally:
    spi.close()
    reset_pin.release()
    dc_pin.release()

