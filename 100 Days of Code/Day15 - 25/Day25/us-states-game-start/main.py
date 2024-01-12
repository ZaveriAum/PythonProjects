import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("Us State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()
guessed_state = []

while len(guessed_state) != 50:
    answer_state = screen.textinput(f"score : {len(guessed_state)}/50", "What's the name of the state").title()
    for name in state_name:
        if name == answer_state:
            guessed_state.append(answer_state)
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            state_info = data[data.state == answer_state]
            new_turtle.goto(int(state_info.x), int(state_info.y))
            new_turtle.write(answer_state)
    if answer_state == "Off":
        break

remaining_state = [name for name in state_name if name not in guessed_state]

# for name in state_name:
#     for g_st in guessed_state:
#         if g_st != name:
#             remaining_state.append(name)


final_score = 50 - len(remaining_state)

end_info = {
    "remaining State": remaining_state,
    "end_statement": f"You got {final_score} correct."
}
new_data = pandas.DataFrame(end_info)
new_data.to_csv("state_to_learn.csv")
screen.exitonclick()
