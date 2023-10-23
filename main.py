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

states_list = locations.state.to_list()
states_dict = {'States': []}

correct_states = 0

while game_is_on:

    answer_state = (screen.textinput(title="Guess the State", prompt="What's another state's name?")).title()

    current_answer = locations[locations.state == f"{answer_state}"]

    if answer_state == 'Exit':
        states_dict['States'] = states_list
        missed_states = pandas.DataFrame(states_dict)
        missed_states.to_csv('states_to_learn.csv')
        break

    if locations['state'].eq(answer_state).any():
        locator.goto(int(current_answer.x), int(current_answer.y))
        locator.write(f"{answer_state}")
        correct_states += 1
        screen.title(f"{correct_states}/50 States Correct")
        states_list.pop(answer_state)

        if correct_states == 50:
            locator.goto(0, 0)
            locator.write(f"Congratulations! {correct_states}/50 Answered Correctly!")
            game_is_on = False

    else:
        locator.goto(0, 0)
        locator.write(f"Game Over. {correct_states}/50 Answered Correctly")
        states_dict['States'] = states_list
        missed_states = pandas.DataFrame(states_dict)
        missed_states.to_csv('states_to_learn.csv')
        game_is_on = False
