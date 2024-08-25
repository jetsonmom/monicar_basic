#!/usr/bin/env python

import time

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

class PCA9685:
    """
    PWM motor controller using PCA9685 boards.
    This is used for most RC Cars
    """

    def __init__(self, channel, address, frequency=60, busnum=None, center=0):
        self.default_freq = 60
        self.pwm_scale = frequency / self.default_freq

        import Adafruit_PCA9685

        if busnum is not None:
            from Adafruit_GPIO import I2C
            def get_bus():
                return busnum
            I2C.get_default_bus = get_bus
        
        self.pwm = Adafruit_PCA9685.PCA9685(address=address)
        self.pwm.set_pwm_freq(frequency)
        self.channel = channel

        self.pulse = center
        self.prev_pulse = center
        self.running = True

    def set_pwm(self, pulse):
        try:
            self.pwm.set_pwm(self.channel, 0, int(pulse * self.pwm_scale))
        except:
            self.pwm.set_pwm(self.channel, 0, int(pulse * self.pwm_scale))

    def run(self, pulse):
        pulse = clamp(pulse, 0, 4095)  # PWM 값이 0에서 4095 사이에 있어야 함
        self.set_pwm(pulse)
        self.prev_pulse = pulse

    def set_pwm_clear(self):
        self.pwm.set_all_pwm(0, 0)

    def set_pulse(self, pulse):
        self.pulse = pulse

class VehicleController:
    def __init__(self):
        # ROS 파라미터를 Python 변수로 변환
        self.STEER_CENTER = 380
        self.STEER_LIMIT = 100
        self.STEER_DIR = -1  # 조향 방향
        self.SPEED_CENTER = 2048  # 모터의 중립 위치를 2048로 설정
        self.SPEED_LIMIT = 4096  # 모터의 최대 PWM 범위
        #self.has_steer = 1  # 스티어링이 있는지 여부
        #self.isDCSteer = 0  # DC 모터로 스티어링을 제어하는지 여부
        self.i2cSteer = 96
        self.i2cThrottle = 64
        self.k_steer = 1  # 조향 게인
        self.k_throttle = 0.2  # 스로틀 게인

        busnum = 1  # Jetson Nano에서는 일반적으로 I2C 버스 1을 사용합니다.

        self.steer_controller = PCA9685(channel=0, address=self.i2cSteer, busnum=busnum)
        self.throttle_controller = PCA9685(channel=0, address=self.i2cThrottle, busnum=busnum)

    def perform_sequence(self):
        # 모터를 중립 위치로 설정
        self.throttle_controller.run(self.SPEED_CENTER)
        print("74")
        time.sleep(1)

        # 앞으로 이동
        forward_pulse = self.SPEED_CENTER + int(self.k_throttle * self.SPEED_LIMIT)
        self.throttle_controller.run(forward_pulse)
          print("80")
        time.sleep(3)

        # 뒤로 이동
        backward_pulse = self.SPEED_CENTER - int(self.k_throttle * self.SPEED_LIMIT)
        self.throttle_controller.run(backward_pulse)
        time.sleep(3)

        # 좌회전
        left_pulse = self.STEER_CENTER + int(self.STEER_DIR * self.k_steer * self.STEER_LIMIT)
        self.steer_controller.run(left_pulse)
        time.sleep(3)

        # 우회전
        right_pulse = self.STEER_CENTER - int(self.STEER_DIR * self.k_steer * self.STEER_LIMIT)
        self.steer_controller.run(right_pulse)
        time.sleep(3)

        # 차량 정지
        self.throttle_controller.run(self.SPEED_CENTER)
        self.steer_controller.run(self.STEER_CENTER)

if __name__ == "__main__":
    controller = VehicleController()
    controller.perform_sequence()
