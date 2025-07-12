from smbus2 import SMBus
import time

bus = SMBus(1)       # I2C-1 bus on Pi

TCA_ADDRESS = 0x70  # Default I2C address for TCA9548A (i2c splitter)

I2C_ADDRESS = [
    
    [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08],
    [0x09,0x10,0x11,0x12,0x13,0x14,0x15,0x16],
    [0x17,0x18,0x19,0x20,0x21,0x22,0x23,0x24],
    [0x25,0x26,0x27,0x28,0x29,0x30,0x31,0x32],
    [0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x40],
    [0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48],
    [0x49,0x50,0x51,0x52,0x53,0x54,0x55,0x56],
    [0x57,0x58,0x59,0x60,0x61,0x62,0x63,0x64],
    
    ]  # Replace with your ATtiny814 I2C address


occupied_color = [1,1,0]


unoccupied_color = [0,1,1]


height = 8
width = 8

channel = 0

def main(bus):
    # print(hex(I2C_ADDRESS[2][0]))
    
    # init boot
    startup()

    # scan for hall effect changes
    # scan_for_hall_effect_chnages()
    # select_channel(2)
    # byte = bus.read_byte(0x17)
    # print(f"Received: {byte:#04x}")  # hex output

    on_off_loop()


#  *************     utils     ***************

def send_led_data(location=[0,0], color=[0,0,0]):
    # input should be [red,green,blue]
    # Send RGB values as 3 bytes
    
    # rgb_data = [r,g,b]
    x = location[0]
    y = location[1]
    
    global bus
    
    try:
        select_channel(x)
        bus.write_i2c_block_data(I2C_ADDRESS[x][y], 0x00, color)  # 0x00 could be your LED register or ignored
        print(f"Sent RGB: {color}")
    except Exception as e:
        print(f"Error occurred: {e} while tryong to send {color} to board number: {hex(I2C_ADDRESS[x][y])} on chanel: {channel}")




def select_channel(channel):
    with SMBus(1) as bus:
        if 0 <= channel <= 7:
            bus.write_byte(TCA_ADDRESS, 1 << channel)
            # print(f"Channel {channel} selected.")
        else:
            raise ValueError("Channel must be between 0 and 7")



def scan_bus(bus):
    devices = []
    for addr in range(0x03, 0x77):
        try:
            bus.write_quick(addr)
            devices.append(hex(addr))
        except:
            pass
    return devices


def scan_and_print_i2c_devices():
    with SMBus(1) as bus:  # SMBus(1) is typical for Raspberry Pi
        for ch in range(8):
            print(f"\n--- Scanning TCA9548A Channel {ch} ---")
            select_channel(bus, ch)
            time.sleep(0.1)  # Give some time for the channel to switch
            devices = scan_bus(bus)
            if devices:
                for device in devices:
                    if (device != '0x70'):
                        print(f"Devices found on channel {ch}: {device}")
            else:
                # print(f"No devices found on channel {ch}")
                pass
            print()
            print()
            print()



def startup():
    # set rows 1,2 and 7,8 to occupied color
    # set 3,4,5,6 to unoccupied color
    index = 0
    for x in range(height):
        for y in range(width):
            
            # top 2 rows
            if (index < 15):
                send_led_data(location=[x,y], color=occupied_color)
            
            # middle section 
            if (index > 15 and index < 39):
                send_led_data(location=[x,y], color=unoccupied_color)
            
            # bottom 2 rows
            if (index > 39):
                send_led_data(location=[x,y], color=occupied_color)
            
            index = index + 1
    
    # pass


def scan_for_hall_effect_chnages():
    while True:
        with SMBus(1) as bus:  # "1" is the I2C bus number (Raspberry Pi uses 1)
            for x in range(height):
                select_channel(x)
                for y in range(width):
                    try:
                        # byte = bus.read_byte(I2C_ADDRESS[x][y])
                        byte = bus.read_byte(I2C_ADDRESS[x][y])
                        print(f"Received: {byte:#04x}")  # hex output
                    except Exception as e:
                        # print(f"Error occurred: {e}")
                        pass


def on_off_loop():
    while True:
        for x in range(height):
            for y in range(width):
                send_led_data(location=[x,y], color=[100,100,100])
        print("on")
        time.sleep(3)
        for x in range(height):
            for y in range(width):
                send_led_data(location=[x,y], color=[0,0,0])
        print("off")
        time.sleep(3)


if __name__ == "__main__":
    main(bus)
