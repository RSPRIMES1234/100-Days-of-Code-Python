#Hurdle 4
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     while front_is_clear() and wall_on_right():
#         move()
#         break
#     while not front_is_clear() and wall_on_right():
#         turn_left()
#         break
#     while front_is_clear() and not wall_on_right():
#         turn_right()
#         move()
#         break
#     while not front_is_clear() and not wall_on_right():
#         turn_right()
#         move()
#         break

#Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    while front_is_clear() and wall_on_right():
        move()
        break
    while not front_is_clear() and wall_on_right():
        turn_left()
        break
    while front_is_clear() and not wall_on_right():
        turn_right()
        move()
        break
    while not front_is_clear() and not wall_on_right() and not at_goal():
        turn_right()
        move()
        break
