import time
from Adafruit_PCA9685 import PCA9685

class SimpleDrive:
    def __init__(self, i2c_address=0x40, throttle_channel=0, speed_center=2048, speed_limit=4096):
        self.pwm = PCA9685(address=i2c_address)
        self.pwm.set_pwm_freq(60)
        self.throttle_channel = throttle_channel
        self.speed_center = speed_center
        self.speed_limit = speed_limit

    def run(self, speed):
        pulse = self.speed_center + speed
        self.pwm.set_pwm(self.throttle_channel, 0, pulse)
        print(f"Throttle Pulse: {pulse}")

    def move_forward(self):
        self.run(self.speed_limit)
        print("Moving Forward")

    def move_backward(self):
        self.run(-self.speed_limit)
        print("Moving Backward")

    def stop(self):
        self.run(0)
        print("Stopping")

# 사용 예제
if __name__ == "__main__":
    drive = SimpleDrive(i2c_address=0x40, throttle_channel=0, speed_center=2048, speed_limit=1024)

    # 앞으로 이동
    drive.move_forward()
    time.sleep(3)

    # 정지
    drive.stop()
    time.sleep(1)

    # 뒤로 이동
    drive.move_backward()
    time.sleep(3)

    # 정지
    drive.stop()
