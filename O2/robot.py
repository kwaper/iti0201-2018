"""Let`s find that object."""
from PiBot import PiBot

# Create a robot instance
robot = PiBot()

# Drive towards object
robot.set_grabber_height(100)

robot.set_right_wheel_speed(-15)
robot.set_left_wheel_speed(15)

while True:
    distance_from_object = robot.get_front_middle_ir()
    while distance_from_object < 0.5:
        distance_from_object = robot.get_front_middle_ir()
        print(robot.get_front_middle_ir())
        robot.set_wheels_speed(15)
        right_obj = robot.get_front_right_ir()
        while (0.17 >= distance_from_object or distance_from_object == 1) and right_obj == 1:
            distance_from_object = robot.get_front_middle_ir()
            right_obj = robot.get_front_right_ir()
            left_obj = robot.get_front_left_ir()
            robot.set_right_wheel_speed(15)
            robot.set_left_wheel_speed(-15)
            print(f"mid {robot.get_front_middle_ir()} right {robot.get_front_right_ir()}")
            while 0.3 < right_obj < 0.9 and distance_from_object == 1:
                print(f"2mid {robot.get_front_middle_ir()} 2right {robot.get_front_right_ir()}")
                right_obj = robot.get_front_right_ir()
                left_obj = robot.get_front_left_ir()
                robot.set_wheels_speed(15)
                while left_obj == right_obj:
                    robot.set_wheels_speed(0)
