import time
from Adafruit_PCA9685 import PCA9685

class SimpleSteering:
    def __init__(self, i2c_address=0x40, channel=0, center=380, frequency=60, busnum=1):
        self.pwm = PCA9685(address=i2c_address)
        self.pwm.set_pwm_freq(frequency)
        self.channel = channel
        self.center = center

        self.pwm.set_pwm(self.channel, 0, self.center)
        print("Steering Controller Awaked!!")

    def steer(self, pulse):
        self.pwm.set_pwm(self.channel, 0, pulse)
        print(f"Steering Pulse: {pulse}")

# 사용 예제
if __name__ == "__main__":
    steering = SimpleSteering(i2c_address=0x40, channel=0, center=380, frequency=60)
    
    # 예제: 왼쪽으로 조향
    steering.steer(300)
    time.sleep(3)

    # 예제: 오른쪽으로 조향
    steering.steer(460)
    time.sleep(3)

    # 예제: 중앙으로 복귀
    steering.steer(380)
