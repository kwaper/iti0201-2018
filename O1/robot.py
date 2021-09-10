"""Let`s find that object."""
from PiBot import PiBot
import rospy

# Create a robot instance
robot = PiBot()
middle_distance = []


def main(r_speed, l_speed):
    """Main function."""
    while True:
        robot.set_left_wheel_speed(-l_speed)
        robot.set_right_wheel_speed(r_speed)
        robot.set_grabber_height(100)
        get_distance_info()
        while get_distance_info() < 0.5:
            get_distance_info()
            print(get_distance_info())
            robot.set_right_wheel_speed(r_speed)
            robot.set_left_wheel_speed(l_speed)
            if get_distance_info() > 0.5:
                get_distance_info()
                robot.set_right_wheel_speed(-r_speed)
                robot.set_left_wheel_speed(l_speed)
            while get_distance_info() <= 0.16:
                robot.set_wheels_speed(0)
                print(get_distance_info())
                print("You have reached your destination!")
                return None


def get_distance_info():
    """Getting distance average."""
    for i in range(5):
        rospy.sleep(0.02)
        middle_distance.append(robot.get_front_middle_ir())
    middle_difference = abs(sum(middle_distance)) / len(middle_distance)
    middle_distance.clear()
    return middle_difference


def wheels_speed(r_speed, l_speed):
    """Get wheels normal speed."""
    robot.set_right_wheel_speed(r_speed)
    robot.set_left_wheel_speed(l_speed)
    r = robot.get_right_wheel_encoder()
    lef = robot.get_left_wheel_encoder()
    rospy.sleep(0.05)
    robot.set_wheels_speed(0)
    rospy.sleep(0.05)
    lef1 = robot.get_left_wheel_encoder()
    r1 = robot.get_right_wheel_encoder()
    difr = r1 - r
    difl = lef1 - lef
    print(difr, difl)
    if difr > difl and max(difr, difl) - min(difr, difl) > 3:
        l_speed += 1
        if r_speed > 14 and l_speed > 14:
            while r_speed > 13 and l_speed > 13:
                r_speed -= 1
                l_speed -= 1
        return wheels_speed(r_speed, l_speed)
    if difl > difr and max(difr, difl) - min(difr, difl) > 3:
        r_speed += 1
        if r_speed > 14 and l_speed > 14:
            while r_speed > 13 and l_speed > 13:
                r_speed -= 1
                l_speed -= 1
        return wheels_speed(r_speed, l_speed)
    else:
        if r_speed > 14 and l_speed > 14:
            while r_speed > 13 and l_speed > 13:
                r_speed -= 1
                l_speed -= 1
        print(r_speed, l_speed)
        return main(r_speed, l_speed)


if __name__ == '__main__':
    wheels_speed(10, 10)
