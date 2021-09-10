"""Robot Labyrinth."""

import rospy
from PiBot import PiBot

robot = PiBot()


class Robot:
    """Object activities."""

    def __init__(self):
        """Description."""
        self.robot = PiBot()
        self.rospy = rospy.sleep
        self.start_timestamp = rospy.get_time()

    def main(self):
        """Action."""
        speed = self.test(15, 15)
        diagonal = self.robot.get_rear_right_diagonal_ir()
        straight = self.robot.get_rear_left_straight_ir()
        most = self.robot.get_rear_right_side_ir()
        self.find_wall(speed)
        while True:
            self.too_complex(speed)
            if most >= 0.05 and straight > 0.03:  # straight
                print("0")    # 0
                while straight >= 0.04 and most >= 0.04:
                    self.robot.set_right_wheel_speed(-speed[0] + 1)
                    self.robot.set_left_wheel_speed(-speed[1] - 8)
                    diagonal = self.robot.get_rear_right_diagonal_ir()
                    most = self.robot.get_rear_right_side_ir()
                    straight = self.robot.get_rear_right_straight_ir()
                self.robot.set_right_wheel_speed(speed[0] - speed[0])
                self.robot.set_left_wheel_speed(speed[1] - speed[1])
                self.robot.set_right_wheel_speed(-speed[0])
                self.robot.set_left_wheel_speed(speed[1])
                rospy.sleep(0.2)
                self.robot.set_right_wheel_speed(speed[0] - speed[0])
                self.robot.set_left_wheel_speed(speed[1] - speed[1])
            self.robot.set_right_wheel_speed(speed[0] - speed[0])
            self.robot.set_left_wheel_speed(speed[1] - speed[1])
            if straight < 0.031 and most < 0.05:
                self.robot.set_right_wheel_speed(speed[0] - speed[0])
                self.robot.set_left_wheel_speed(speed[1] - speed[1])
                for i in range(3):
                    straight = self.robot.get_rear_right_straight_ir()
                    self.rospy(0.05)
                print("view")  # view
                if straight < 0.031:
                    first_r = self.robot.get_right_wheel_encoder()
                    self.robot.set_right_wheel_speed(speed[0])
                    self.robot.set_left_wheel_speed(-speed[1])
                    self.rospy(0.5)
                    self.robot.set_right_wheel_speed(speed[0] - speed[0])
                    self.robot.set_left_wheel_speed(speed[1] - speed[1])
                    second_r = self.robot.get_right_wheel_encoder()
                    dif_r = abs(first_r) - abs(second_r)
                    self.robot.set_right_wheel_speed(speed[0])
                    self.robot.set_left_wheel_speed(speed[1])
                    self.rospy(0.5)
                    self.robot.set_right_wheel_speed(speed[0] - speed[0])
                    self.robot.set_left_wheel_speed(speed[1] - speed[1])
                    last_l = self.robot.get_left_wheel_encoder()  # or etogo
                    while self.robot.get_left_wheel_encoder() - last_l < dif_r * 2:
                        print("1")   # 1
                        self.robot.get_left_wheel_encoder()
                        self.robot.set_right_wheel_speed(-speed[0])
                        self.robot.set_left_wheel_speed(speed[1])
                    self.robot.set_right_wheel_speed(speed[0] - speed[0])
                    self.robot.set_left_wheel_speed(speed[1] - speed[1])
                    while diagonal > 0.03 and most > 0.03 and straight > 0.03:
                        print("2")  # 2
                        diagonal = self.robot.get_rear_right_diagonal_ir()
                        most = self.robot.get_rear_right_side_ir()
                        straight = self.robot.get_rear_right_straight_ir()
                        self.robot.set_right_wheel_speed(-speed[0])
                        self.robot.set_left_wheel_speed(-speed[1] - 1)
                    self.robot.set_right_wheel_speed(speed[0] - speed[0])
                    self.robot.set_left_wheel_speed(speed[1] - speed[1])
                    rospy.sleep(0.05)
                    diagonal = self.robot.get_rear_right_diagonal_ir()
                    most = self.robot.get_rear_right_side_ir()
                    straight = self.robot.get_rear_right_straight_ir()
                    while straight < 0.05:
                        print("3")      # 3
                        straight = self.robot.get_rear_right_straight_ir()
                        self.robot.set_right_wheel_speed(-speed[0])
                        self.robot.set_left_wheel_speed(speed[1])
                    self.robot.set_right_wheel_speed(speed[0] - speed[0])
                    self.robot.set_left_wheel_speed(speed[1] - speed[1])

            else:
                print("5")
                self.robot.set_right_wheel_speed(-speed[0])
                self.robot.set_left_wheel_speed(-speed[1])
                diagonal = self.robot.get_rear_right_diagonal_ir()
                most = self.robot.get_rear_right_side_ir()
                straight = self.robot.get_rear_right_straight_ir()
                self.robot.set_right_wheel_speed(speed[0] - speed[0])
                self.robot.set_left_wheel_speed(speed[1] - speed[1])

    def too_complex(self, speed):
        """Fixing."""
        most = self.robot.get_rear_right_side_ir()
        straight = self.robot.get_rear_right_straight_ir()
        while 0.03 <= most < 0.05 and straight > 0.03:
            print("1")
            self.robot.set_right_wheel_speed(-speed[0])  # drive along wall
            self.robot.set_left_wheel_speed(-speed[1])
            most = self.robot.get_rear_right_side_ir()
            straight = self.robot.get_rear_right_straight_ir()
        self.robot.set_right_wheel_speed(speed[0] - speed[0])  # speed = 0
        self.robot.set_left_wheel_speed(speed[1] - speed[1])

        while most < 0.03 and straight > 0.03:
            self.robot.set_right_wheel_speed(-speed[0])
            self.robot.set_left_wheel_speed(speed[1])
            most = self.robot.get_rear_right_side_ir()
            straight = self.robot.get_rear_right_straight_ir()
        self.robot.set_right_wheel_speed(speed[0] - speed[0])  # speed = 0
        self.robot.set_left_wheel_speed(speed[1] - speed[1])

    def test(self, l_speed, r_speed):
        """Fix wheels speed."""
        self.robot.set_right_wheel_speed(r_speed)
        self.robot.set_left_wheel_speed(l_speed)
        right1 = self.robot.get_right_wheel_encoder()
        left1 = self.robot.get_left_wheel_encoder()
        rospy.sleep(0.05)
        self.robot.set_wheels_speed(0)
        rospy.sleep(0.05)
        right2 = self.robot.get_right_wheel_encoder()
        left2 = self.robot.get_left_wheel_encoder()
        right_dif = right2 - right1
        left_dif = left2 - left1
        print(right_dif, left_dif)
        if left_dif > right_dif and max(right_dif, left_dif) - min(right_dif, left_dif) > 3:
            r_speed += 1
            self.robot.set_right_wheel_speed(r_speed - r_speed)
            self.robot.set_left_wheel_speed(l_speed - l_speed)
            return self.test(l_speed, r_speed)
        elif right_dif > left_dif and max(right_dif, left_dif) - min(right_dif, left_dif) > 3:
            l_speed += 1
            self.robot.set_right_wheel_speed(r_speed - r_speed)
            self.robot.set_left_wheel_speed(l_speed - l_speed)
            return self.test(l_speed, r_speed)
        else:
            if r_speed > 17 and l_speed > 17:
                while r_speed > 16 and l_speed > 16:
                    r_speed -= 1
                    l_speed -= 1
            elif r_speed < 15 and l_speed < 15:
                while r_speed < 15 and l_speed < 15:
                    r_speed += 1
                    l_speed += 1
            print(r_speed, l_speed)
            a = [r_speed, l_speed]
            return a

    def find_wall(self, speed):
        """Find the wall."""
        left = self.robot.get_rear_right_diagonal_ir()
        straight = self.robot.get_rear_left_straight_ir()
        most = self.robot.get_rear_right_side_ir()
        while left >= 0.05 and straight >= 0.05 and most >= 0.05:
            self.robot.set_right_wheel_speed(-speed[0])
            self.robot.set_left_wheel_speed(-speed[1] - 2)
            left = self.robot.get_rear_right_diagonal_ir()
            most = self.robot.get_rear_right_side_ir()
            straight = self.robot.get_rear_right_straight_ir()
        self.robot.set_right_wheel_speed(speed[0] - speed[0])
        self.robot.set_left_wheel_speed(speed[1] - speed[1])


if __name__ == "__main__":
    robot = Robot()
    robot.main()
