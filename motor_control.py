
from machine import Pin, PWM, Timer #importing PIN and PWM

dutyCycleNormal = 15000
dutyCycleTurning = 20000
digitalMode = 1
joystickMode = 2


class Motor:

    def __init__(self) -> None:
        # #OUT1  and OUT2
        # self.In1=Pin(6,Pin.OUT)  #IN1`
        # self.In2=Pin(7,Pin.OUT)  #IN2
        # #OUT3  and OUT4
        # self.In3=Pin(4,Pin.OUT)  #IN3
        # self.In4=Pin(3,Pin.OUT)  #IN4

        self.wobbleState = 0
        self.motorTimer = Timer(-1)
        self.motorTimer.deinit()

        self.rightWheelFwd=PWM(Pin(6))
        self.rightWheelRev=PWM(Pin(7))
        self.leftWheelFwd=PWM(Pin(4))
        self.leftWheelRev=PWM(Pin(3))
        # EN_B=PWM(Pin(2))
        # Defining frequency for enable pins
        self.rightWheelFwd.freq(1500)
        self.rightWheelRev.freq(1500)
        self.leftWheelFwd.freq(1500)
        self.leftWheelRev.freq(1500)

        # Setting maximum duty cycle for maximum speed (0 to 65025)
        # EN_A.duty_u16(65025)
        # EN_B.duty_u16(65025)
        pass

    def control(self, valueArray):
        if len(valueArray) != 8:
            self.stop()
            return
        

        if valueArray[5] != 0:
            if valueArray[5] == 4: # ^ key
                self.initiateWobble()
            elif valueArray[5] == 16: # x key
                self.initiateShake()
            elif valueArray[5] == 8: # 0 key
                self.spinRight()
            elif valueArray[5] == 32: # square key
                self.spinLeft()
        else:
            mode = valueArray[2]

            if mode == digitalMode:
                value = valueArray[6]
                if value == 0:
                    self.stop()
                elif value == 1:
                    self.forward()
                elif value == 2:
                    self.reverse()
                elif value == 4:
                    self.left()
                elif value == 8:
                    self.right()
                else:
                    self.stop()
            elif mode == joystickMode:
                value = valueArray[6]
                if value == 0:
                    self.stop()
                elif value >= 25 and value <= 75:
                    self.forward()
                elif value >= 125 and value <= 175:
                    self.reverse()
                elif value > 75 and value < 125:
                    self.left()
                elif value > 175 or value < 25:
                    self.right()
                else:
                    self.stop()
            else: 
                self.stop()
                return    


# if value >25 and value <175:
#   self.right()
# elif value >75 and <125:
#       self.left ()

    def forward(self):
        self.rightWheelFwd.duty_u16(dutyCycleNormal)
        self.rightWheelRev.duty_u16(0)
        self.leftWheelFwd.duty_u16(dutyCycleNormal)
        self.leftWheelRev.duty_u16(0)
        print("Running Forward..")
        # self.In1.high()
        # self.In2.low()
        # self.In3.high()
        # self.In4.low()
        pass
    
    def reverse(self):
        self.rightWheelFwd.duty_u16(0)
        self.rightWheelRev.duty_u16(dutyCycleNormal)
        self.leftWheelFwd.duty_u16(0)
        self.leftWheelRev.duty_u16(dutyCycleNormal)
        print("Running Reverse..")
        # self.In1.low()
        # self.In2.high()
        # self.In3.low()
        # self.In4.high()
        pass

    def left(self):
        self.rightWheelFwd.duty_u16(dutyCycleNormal)
        self.rightWheelRev.duty_u16(0)
        self.leftWheelFwd.duty_u16(dutyCycleTurning)
        self.leftWheelRev.duty_u16(0)
        print("Left..")
        
    def right(self):
        self.rightWheelFwd.duty_u16(dutyCycleTurning)
        self.rightWheelRev.duty_u16(0)
        self.leftWheelFwd.duty_u16(dutyCycleNormal)
        self.leftWheelRev.duty_u16(0)
        print("right..")

    def spinRight(self):
        self.rightWheelFwd.duty_u16(dutyCycleNormal)
        self.rightWheelRev.duty_u16(0)
        self.leftWheelFwd.duty_u16(0)
        self.leftWheelRev.duty_u16(dutyCycleNormal)
        print("Spinning right..")

    def spinLeft(self):
        self.rightWheelFwd.duty_u16(0)
        self.rightWheelRev.duty_u16(dutyCycleNormal)
        self.leftWheelFwd.duty_u16(dutyCycleNormal)
        self.leftWheelRev.duty_u16(0)
        print("Spinning Left..")

    def wobble(self, timer_instance):
        print("Swapping Wobble Mode..", self.wobbleState)
        if self.wobbleState == 0:
            self.forward()
            self.wobbleState = 1
        else:
            self.reverse()
            self.wobbleState = 0
    
    def shake(self, timer_instance):
        print("Swapping shake Mode..", self.wobbleState)
        if self.wobbleState == 0:
            self.spinRight()
            self.wobbleState = 1
        else:
            self.spinLeft()
            self.wobbleState = 0

    def initiateShake(self):
        self.motorTimer.init(freq=2, mode=Timer.PERIODIC, callback=self.shake)

    def initiateWobble(self):
        self.motorTimer.init(freq=2, mode=Timer.PERIODIC, callback=self.wobble)

    def stop(self):
        self.rightWheelFwd.duty_u16(0)
        self.rightWheelRev.duty_u16(0)
        self.leftWheelFwd.duty_u16(0)
        self.leftWheelRev.duty_u16(0)
        self.motorTimer.deinit()

        print("Stopped..")
        pass