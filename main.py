import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

locator = turtle.Turtle()
locator.penup()
locator.hideturtle()
turtle.shape(image)

game_is_on = True

locations = pandas.read_csv("50_states.csv")

correct_states = 0

while game_is_on:

    answer_state = (screen.textinput(title="Guess the State", prompt="What's another state's name?")).title()

    current_answer = locations[locations.state == f"{answer_state}"]

    if locations['state'].eq(answer_state).any():
        locator.goto(int(current_answer.x), int(current_answer.y))
        locator.write(f"{answer_state}")
        correct_states += 1
        screen.title(f"{correct_states}/50 States Correct")

        if correct_states == 50:
            locator.goto(0, 0)
            locator.write(f"Congratulations! {correct_states}/50 Answered Correctly!")
            game_is_on = False

    else:
        locator.goto(0, 0)
        locator.write(f"Game Over. {correct_states}/50 Answered Correctly")
        game_is_on = False

screen.exitonclick()
