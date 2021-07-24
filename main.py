from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
sc = Screen()
sc.setup(width=500, height=400)
sc.setworldcoordinates(0, 0, 500, 400)
bet = sc.textinput("Make a bet", "Choose color: red, orange, yellow, green, blue, purple.").lower()
end = False


class RaceTurtle():
    def __init__(self):
        self.distance = 0
        self.obj = Turtle()
        self.obj.penup()
        self.obj.shape("turtle")

    def set_color(self, color):
        self.obj.color(color)

    def set_position(self, pos_x, pos_y):
        self.obj.goto(self.distance + pos_x, pos_y)
        self.distance += pos_x

    def get_distance(self):
        return self.distance

    def get_color(self):
        return self.obj.color()


def make_turtle(i):
    turtle_obj = RaceTurtle()
    turtles.append(turtle_obj)
    turtles[i].set_color(colors[i])
    turtles[i].set_position(0, 50 * i + 50)


def check_bet(winner):
    if winner != bet:
        print("You lose the bet")
    else:
        print("You win!!!")


def race():
    for i in range(6):
        make_turtle(i)
    global end
    while not end:
        for turtle_num in range(0, len(turtles)):
            rand = random.randint(10, 20)
            turtles[turtle_num].set_position(rand, 50 * turtle_num + 50)
            if turtles[turtle_num].get_distance() >= 500:
                end = True
                win = turtles[turtle_num].get_color()[0]
                print(f"Winner is {win} turtle!\n")
                check_bet(win)
                break


race()

sc.exitonclick()
