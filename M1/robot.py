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
        self.straight = self.robot.get_rear_right_straight_ir()
        self.most = self.robot.get_rear_right_side_ir()
        self.most_dist = []
        self.str_dist = []

    def main(self, right, left):
        """Action.."""
        self.robot.set_grabber_height(100)
        self.robot.close_grabber(100)
        while True:
            self.robot.set_grabber_height(100)
            while self.filter_side() >= 0.05 and self.filter_straight() >= 0.05:
                print("1")
                self.robot.set_left_wheel_speed(-left - 8)
                self.robot.set_right_wheel_speed(-right + 1)
            self.robot.set_left_wheel_speed(-left + left)
            self.robot.set_right_wheel_speed(-right + right)
            while 0.03 < self.filter_side() < 0.05 and self.filter_straight() >= 0.045:
                print("2")
                self.robot.set_left_wheel_speed(-left)
                self.robot.set_right_wheel_speed(-right)
            self.robot.set_left_wheel_speed(-left + left)
            self.robot.set_right_wheel_speed(-right + right)
            while 0.02 < self.filter_side() <= 0.05 and self.filter_straight() < 0.05:
                print("3")
                self.robot.set_left_wheel_speed(left)
                self.robot.set_right_wheel_speed(-right)
                while self.filter_side() == 0.05 and self.filter_straight() == 0.05:
                    self.robot.set_left_wheel_speed(-left)
                    self.robot.set_right_wheel_speed(-right - 5)
            while self.filter_side() <= 0.05 and self.filter_straight() <= 0.03:
                self.robot.set_left_wheel_speed(left)
                self.robot.set_right_wheel_speed(-right)
                while self.filter_side() == 0.05 and self.filter_straight() == 0.05:
                    self.robot.set_left_wheel_speed(-left)
                    self.robot.set_right_wheel_speed(-right - 5)
            while self.filter_side() <= 0.03:
                self.robot.set_left_wheel_speed(left)
                self.robot.set_right_wheel_speed(-right)
                while self.filter_side() == 0.05 and self.filter_straight() == 0.05:
                    self.robot.set_left_wheel_speed(-left)
                    self.robot.set_right_wheel_speed(-right - 5)
            self.robot.set_left_wheel_speed(-left + left)
            self.robot.set_right_wheel_speed(-right + right)

    def filter_side(self):
        """Getting distance average."""
        for i in range(3):
            self.rospy(0.01)
            self.most_dist.append(self.robot.get_rear_right_side_ir())
        side_dif = abs(sum(self.most_dist)) / len(self.most_dist)
        self.most_dist.clear()
        return side_dif

    def filter_straight(self):
        """Getting distance average."""
        for i in range(3):
            self.rospy(0.01)
            self.str_dist.append(self.robot.get_rear_right_straight_ir())
        straight_dif = abs(sum(self.str_dist)) / len(self.str_dist)
        self.str_dist.clear()
        return straight_dif

    def wheels_speed(self, r_speed, l_speed):
        """Get wheels normal speed."""
        self.robot.set_right_wheel_speed(r_speed)
        self.robot.set_left_wheel_speed(l_speed)
        r = self.robot.get_right_wheel_encoder()
        lef = self.robot.get_left_wheel_encoder()
        self.rospy(0.05)
        self.robot.set_wheels_speed(0)
        self.rospy(0.05)
        lef1 = self.robot.get_left_wheel_encoder()
        r1 = self.robot.get_right_wheel_encoder()
        difr = r1 - r
        difl = lef1 - lef
        print(difr, difl)
        if difr > difl and max(difr, difl) - min(difr, difl) > 3:
            l_speed += 1
            if r_speed > 16 and l_speed > 16:
                while r_speed > 15 and l_speed > 15:
                    r_speed -= 1
                    l_speed -= 1
            return self.wheels_speed(r_speed, l_speed)
        if difl > difr and max(difr, difl) - min(difr, difl) > 3:
            r_speed += 1
            if r_speed > 16 and l_speed > 16:
                while r_speed > 15 and l_speed > 15:
                    r_speed -= 1
                    l_speed -= 1
            return self.wheels_speed(r_speed, l_speed)
        else:
            if r_speed > 16 and l_speed > 16:
                while r_speed > 15 and l_speed > 15:
                    r_speed -= 1
                    l_speed -= 1
            print(r_speed, l_speed)
            return self.main(r_speed, l_speed)


if __name__ == "__main__":
    robot = Robot()
    robot.wheels_speed(15, 15)
