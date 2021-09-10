"""Terminator."""
import rospy
from PiBot import PiBot

robot = PiBot()
count = int()
robot.get_leftmost_line_sensor()
robot.get_rightmost_line_sensor()


def counting(count):
    """Counting."""
    if count == 3:
        print("Turning Right")
        robot.set_right_wheel_speed(-30)
        robot.set_left_wheel_speed(0)
        rospy.sleep(0.7)
        return count
    elif count == 2:
        print("Going Straight")
        robot.set_wheels_speed(-20)
        rospy.sleep(0.7)
    elif count == 1:
        print("Turning Left")
        robot.set_right_wheel_speed(0)
        robot.set_left_wheel_speed(-30)
        rospy.sleep(0.7)


while True:
    color_from_left = robot.get_leftmost_line_sensor()
    color_from_right = robot.get_rightmost_line_sensor()
    if count == 3:
        count -= 3
    if color_from_right == color_from_left:
        robot.set_wheels_speed(-13)
    elif color_from_left > color_from_right:
        robot.set_left_wheel_speed(-15)
        robot.set_right_wheel_speed(15)
        if color_from_right > 300:
            robot.set_right_wheel_speed(-15)
    elif color_from_left < color_from_right:
        robot.set_left_wheel_speed(15)
        robot.set_right_wheel_speed(-15)
        if color_from_left > 300:
            robot.set_left_wheel_speed(-15)
    if color_from_right < 300 and color_from_left < 300:
        count += 1
        print(count)
        counting(count)
