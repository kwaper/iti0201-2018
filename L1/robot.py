"""Simulatsioon."""
from PiBot import PiBot
import rospy

def follow_line():
    """Follow line."""
    robot = PiBot()
    robot.set_wheels_speed(15)
    colour = 500
    while True:
        left_sensor = robot.get_third_line_sensor_from_left()
        right_sensor = robot.get_third_line_sensor_from_right()
        print("left sensor: " + str(left_sensor))
        print("right sensor :" + str(right_sensor))
        if right_sensor > colour and left_sensor < colour:
            robot.set_right_wheel_speed(-15)
            robot.set_left_wheel_speed(-20)
            rospy.sleep(0.05)
        elif right_sensor < colour and left_sensor > colour:
            robot.set_right_wheel_speed(-20)
            robot.set_left_wheel_speed(-15)
            rospy.sleep(0.05)
        elif right_sensor < colour and left_sensor < colour:
            robot.set_wheels_speed(-20)
            rospy.sleep(0.05)
        elif right_sensor > colour and left_sensor > colour:
            robot.set_right_wheel_speed(15)
            robot.set_left_wheel_speed(-15)


if __name__ == '__main__':
    follow_line()
