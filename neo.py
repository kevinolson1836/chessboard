import board
import neopixel
import time

# Configuration
LED_COUNT = 8        # Number of NeoPixels
LED_PIN = board.D18  # GPIO pin (usually D18 for PWM control)
BRIGHTNESS = 0.5     # 0.0 to 1.0

# Create NeoPixel object
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=BRIGHTNESS, auto_write=False)

# Set all LEDs to green
green_color = (0, 255, 0)  # RGB
for i in range(LED_COUNT):
    pixels[i] = green_color

pixels.show()  # Send data to the LEDs

print("All 8 NeoPixels set to green.")

# Optional: keep them on for a while
time.sleep(1000000)

# Turn off after delay
pixels.fill((0, 0, 0))
pixels.show()
