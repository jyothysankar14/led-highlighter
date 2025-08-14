# LED Highlighter

**Individually Addressable LED Highlighter** — a DIY wearable/project that uses addressable LEDs to highlight text or objects in your environment.

---

##  Features
- High-resolution control using **Individually Addressable LEDs** (e.g. WS2812, SK6812)
- Intuitive **highlight functionality**, activated by buttons or motion
- Customizable **color patterns**, brightness levels, and effects
- Compact and portable—ideal for DIY markers, guide pointers, or ambient highlighting

---

##  Hardware Requirements
| Component                       | Suggested Options           |
|----------------------------------|------------------------------|
| Microcontroller                  | Arduino (Uno/Nano), ESP32    |
| Addressable LEDs                 | WS2812B or SK6812 (NeoPixels)|
| Power Supply                     | USB 5 V or appropriate LiPo  |
| Activation Method                | Push button, Hall sensor, etc. |
| (Optional) Diffuser/Enclosure    | Acrylic, 3D-printed housing  |

---

##  Software & Libraries
- **FastLED** or **Adafruit NeoPixel** — for LED control  
- (Optional) **Analog/button/IMU libraries** — depending on input method  
- If using ESP32: **PlatformIO** recommended for firmware development

---

##  Getting Started

1. Clone the Repository:
```bash
git clone https://github.com/jyothysankar14/led-highlighter.git
cd led-highlighter

2. Set Up the Hardware:

Wire LEDs to the microcontroller’s digital output and power rails

Add a button or sensor to trigger highlighting

3. Upload Firmware:

Open the .ino or PlatformIO project

Configure LED pin, LED count, trigger pin, and patterns

Upload to your board

4. Customize Behavior:

Edit color configurations, brightness, or animation patterns

Pair with sensors or external modules for advanced triggers.

Folder Structure

led-highlighter/
├── hardware/           # Fritzing files, schematics, PCB layouts
├── firmware/           # Arduino code or PlatformIO project files
├── assets/             # Diagrams, photos
├── docs/               # Design notes or usage guides
└── README.md           # This documentation

License

This project is licensed under the MIT License. Feel free to adapt and share it freely!

Acknowledgements

Adafruit NeoPixel for easy LED programming

DIY lighting communities and tutorials for inspiration

Your creativity—turn this into something awesome!
