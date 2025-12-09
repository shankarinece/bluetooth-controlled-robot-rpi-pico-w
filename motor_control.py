
from machine import Pin,PWM,UART #importing PIN and PWM

dutyCycleNormal = 15000
dutyCycleTurning = 20000
class Motor:

    def __init__(self) -> None:
        # #OUT1  and OUT2
        # self.In1=Pin(6,Pin.OUT)  #IN1`
        # self.In2=Pin(7,Pin.OUT)  #IN2
        # #OUT3  and OUT4
        # self.In3=Pin(4,Pin.OUT)  #IN3
        # self.In4=Pin(3,Pin.OUT)  #IN4



        self.in1Pwm=PWM(Pin(6))
        self.in2Pwm=PWM(Pin(7))
        self.in3Pwm=PWM(Pin(4))
        self.in4Pwm=PWM(Pin(3))
        # EN_B=PWM(Pin(2))
        # Defining frequency for enable pins
        self.in1Pwm.freq(1500)
        self.in2Pwm.freq(1500)
        self.in3Pwm.freq(1500)
        self.in4Pwm.freq(1500)

        # Setting maximum duty cycle for maximum speed (0 to 65025)
        # EN_A.duty_u16(65025)
        # EN_B.duty_u16(65025)
        pass

    def control(self, value):
        if value >= 25 and value <= 75:
            self.forward()
        elif value >= 125 and value <= 175:
            self.reverse()
        elif value > 75 and value < 125:
            self.left()
        elif value > 175 or value < 25:
            self.right()
            pass
        else:
            self.stop()

# if value >25 and value <175:
#   self.right()
# elif value >75 and <125:
#       self.left ()

    def forward(self):
        self.in1Pwm.duty_u16(dutyCycleNormal)
        self.in2Pwm.duty_u16(0)
        self.in3Pwm.duty_u16(dutyCycleNormal)
        self.in4Pwm.duty_u16(0)
        print("Running Forward..")
        # self.In1.high()
        # self.In2.low()
        # self.In3.high()
        # self.In4.low()
        pass
    
    def reverse(self):
        self.in1Pwm.duty_u16(0)
        self.in2Pwm.duty_u16(dutyCycleNormal)
        self.in3Pwm.duty_u16(0)
        self.in4Pwm.duty_u16(dutyCycleNormal)
        print("Running Reverse..")
        # self.In1.low()
        # self.In2.high()
        # self.In3.low()
        # self.In4.high()
        pass

    def left(self):
        self.in1Pwm.duty_u16(dutyCycleNormal)
        self.in2Pwm.duty_u16(0)
        self.in3Pwm.duty_u16(dutyCycleTurning)
        self.in4Pwm.duty_u16(0)
        print("Left..")
        
    def right(self):
        self.in1Pwm.duty_u16(dutyCycleTurning)
        self.in2Pwm.duty_u16(0)
        self.in3Pwm.duty_u16(dutyCycleNormal)
        self.in4Pwm.duty_u16(0)
        print("right..")

    def stop(self):
        self.in1Pwm.duty_u16(0)
        self.in2Pwm.duty_u16(0)
        self.in3Pwm.duty_u16(0)
        self.in4Pwm.duty_u16(0)
        print("Stopped..")
        pass