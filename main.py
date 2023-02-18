import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# ----------------------------------------------
# Get the coordinate on mouse click
# def get_mouse_click_coor(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# --------------------------------------------------
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
print(states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    convert_answer = answer_state.title()

    if convert_answer == "Exit":
        # missing_states = []
        missing_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if convert_answer in states:
        guessed_states.append(convert_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == convert_answer]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(states_data.state.item())



# screen.exitonclick()