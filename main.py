# servo_animation_code.py -- show simple servo animation list
import time, random, board
from pwmio import PWMOut
from adafruit_motor import servo

animation = (
    
    (0, 1.3),
    (90, 1),
    (180, 1.3),
    (0, 1)
    
)

# your servo will likely have different min_pulse & max_pulse settings
servoA = servo.Servo(PWMOut(board.SERVO_1, frequency=50), min_pulse=500, max_pulse=2250)
servoB = servo.Servo(PWMOut(board.SERVO_2, frequency=50), min_pulse=500, max_pulse=2250)

servoA.angle = 0
time.sleep(0)
servoA.angle = 180
servoB.angle = 90 
time.sleep(0)
servoA.angle = 90
servoB.angle = 0

ani_pos = 0
ease_speed = 0.1
num_ease_slices = 50
while True:
    new_angle, secs = animation[ ani_pos ]
    print("new position:", new_angle, secs)
    for i in range(num_ease_slices):
        servoA.angle += (new_angle - servoA.angle) * ease_speed
        print((new_angle - servoA.angle) * ease_speed)
        time.sleep( secs / num_ease_slices )
    print("got there")
    time.sleep(0)
    ani_pos = (ani_pos + 1) % len(animation)
    break
while True:
    new_angle, secs = animation[ ani_pos ]
    print("new position:", new_angle, secs)
    for i in range(num_ease_slices):
        servoA.angle += (new_angle - servoA.angle) * ease_speed
        print((new_angle - servoA.angle) * ease_speed)
        time.sleep( secs / num_ease_slices )
    print("got there")
    time.sleep(0)
    ani_pos = (ani_pos + 1) % len(animation)
    break
while True:
    new_angle, secs = animation[ ani_pos ]
    print("new position:", new_angle, secs)
    for i in range(num_ease_slices):
        servoA.angle += (new_angle - servoA.angle) * ease_speed
        print((new_angle - servoA.angle) * ease_speed)
        time.sleep( secs / num_ease_slices )
    print("got there")
    time.sleep(0)
    ani_pos = (ani_pos + 1) % len(animation)
    break