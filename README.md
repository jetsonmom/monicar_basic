### 1. `smbus2` 설치
터미널에서 다음 명령어를 사용하여 `smbus2` 패키지를 설치하세요:
```bash
pip3 install smbus2
```

이 명령어는 Python의 패키지 관리자인 `pip`를 사용하여 `smbus2` 모듈을 설치합니다.

### 2. 설치 확인
설치가 완료되면, 다시 Python 스크립트를 실행하여 오류가 해결되었는지 확인합니다:
```bash
python3 test_servo.py
```

###오류 메시지에서 `ServoKit`이라는 이름이 정의되지 않았다는 것을 확인할 수 있습니다. 이 오류는 `ServoKit` 클래스가 사용되었지만 해당 클래스가 포함된 라이브러리가 불러와지지 않았거나 설치되지 않았기 때문에 발생합니다. 일반적으로 `ServoKit` 클래스는 `adafruit_servokit` 라이브러리에서 제공됩니다.

### 해결 방법:

1. **`adafruit_servokit` 라이브러리 설치**:
   이 라이브러리가 설치되어 있는지 확인하고, 설치되어 있지 않다면 다음 명령어로 설치합니다:
   ```bash
   pip3 install adafruit-circuitpython-servokit
   ```

2. **코드에서 라이브러리 임포트**:
   `ServoKit` 클래스를 사용하기 전에, Python 코드에서 해당 라이브러리를 불러와야 합니다. 다음과 같은 코드가 포함되어 있는지 확인하세요:
   ```python
   from adafruit_servokit import ServoKit
   ```

3. **스크립트 재실행**:
   필요한 라이브러리를 설치하고 코드에서 제대로 임포트한 후, 스크립트를 다시 실행하여 오류가 해결되었는지 확인합니다:
   ```bash
   python3 test_servo.py
   ```
4. **오린에서 basic_servo.py 실행시에  코드 수정해야함.**
busnum=1을 busnum=7로 바꿔줘야함
