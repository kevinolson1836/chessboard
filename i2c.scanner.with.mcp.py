from smbus2 import SMBus
import time

TCA_ADDRESS = 0x70  # Default I2C address for TCA9548A

def select_channel(bus, channel):
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

def main():
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

if __name__ == "__main__":
    main()
