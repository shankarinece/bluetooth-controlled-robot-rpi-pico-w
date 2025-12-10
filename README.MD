# Bluetooth Controlled Robot Car with RPI Pico W
This project uses RPI Pico W boards's in-built BLE module to receive control signals from app/computer. This avoids the need of HC-05/06 modules to add a BT interface. <br />
If you are trying this, ensure to procure a W version like RPI Pico W or RPI Pico 2 W<br /><br />

This is done for my school robotics project at [Lake Montfort School, Bangalore](https://lakemontfortschool.ac.in/). 

# Motor Driver
This board uses a BO motor driver, that gets the PWM signals from RPI MCU and drives the motor. In this project, L298 Driver board, something similar to [this](https://robu.in/product/l298n-2a-based-motor-driver-module-good-quality/?gad_source=1&gad_campaignid=20381096599&gclid=Cj0KCQiAi9rJBhCYARIsALyPDtveBfTElFwoYwNDLqpHOKq6RpIx1Dey8nMyDAu_IZM-VtaTvZsOMngaArgTEALw_wcB) is used. It provides upto 2 Amps of current to each motor. <br />

# Power Management
The Moror driver is powered by a ~12v Li-Ion battery (3x 3.7v 18650 cells connected in series with a BMS). <br />
Since the motor driver board has a 5v (7805 type) regulator on board, the RPI Pico board is supplied with the power from this regulator. 
The motor used works from 3v to 6v. Since the Motor driver is supplied with 12v, we use PWM Dutycycle (30% max) from the RPI to limit the supply to the motor to avoid burnout


# Phone App
[Dabble app](https://play.google.com/store/apps/details?id=io.dabbleapp&hl=en_CA&gl=US) that runs on Andriod phone is used to connect to the RPI BT module. In the Dabble app select Gamepad mode --> Joystick mode to send the joystick data to the BT in RPI. <br />
In this mode, the joystick sends data from 0 to 199 when the joystick is moved, with 0 being the far right and 50 being the top and 100 being the far left and 150 being the bottom most. This data is processed in line #104 in main.py and the motor's PWM is controlled.

# Firmware
Micropython is used to code the RPI MCU. [This example](https://github.com/micropython/micropython/blob/master/examples/bluetooth/ble_simple_peripheral.py) from BT interface is tweaked to process data from the Dabble app.

# Development
* Used VS Code with official [RPI Pico extension](https://marketplace.visualstudio.com/items?itemName=raspberry-pi.raspberry-pi-pico) to perform development. This connects to pico when the board is connected over USB
* 
# Schematics
![Pseudo schematics](/circuit.png)