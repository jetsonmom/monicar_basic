from adafruit_pca9685 import PCA9685
from adafruit_motorkit import MotorKit
from board import SCL, SDA
import busio
import time

# I2C 버스 설정
i2c_bus = busio.I2C(SCL, SDA)

# PCA9685 초기화 (서보 제어용)
pca = PCA9685(i2c_bus, address=0x40)
pca.frequency = 60
servo_channel = pca.channels[0]

# MotorKit 초기화 (DC 모터 제어용)
kit = MotorKit(i2c_bus=i2c_bus, address=0x60)
motor = kit.motor1

# 서보를 중앙으로 이동
servo_channel.duty_cycle = 0x7FFF
time.sleep(1)

# 서보를 특정 각도로 이동
servo_channel.duty_cycle = 0x9000
time.sleep(1)

# 모터 앞으로 이동
motor.throttle = 1.0
time.sleep(3)

# 모터 뒤로 이동
motor.throttle = -1.0
time.sleep(3)

# 모터와 서보 정지
motor.throttle = 0
servo_channel.duty_cycle = 0x7FFF
