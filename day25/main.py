import turtle
import pandas

FONT = ('Courier', 8, 'bold')

screen = turtle.Screen()
screen.title('US think they are the center of the world')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
game_is_on = True
states_list = pandas.read_csv('50_states.csv')
correct = []
text = turtle.Turtle()
text.penup()
text.ht()
text.color("black")
text.speed("fastest")

while game_is_on:
  answer_state = screen.textinput(
      title=f"#{len(correct)}/50 states guessed",
      prompt="Guess another state's name"
  ).lower()

  if answer_state == 'exit':
      break

  state = states_list[states_list['state']
      .map(lambda x: x.lower()) == answer_state]

  game_is_on = len(correct) < 50

  if not game_is_on:
      break

  if len(state) == 0:
      continue

  if state.index[0] in correct:
      continue

  correct.append(state.index[0])
  text.goto(int(state.x), int(state.y))
  text.write(str(state.state[state.index[0]]), align='center', font=FONT)

turtle.mainloop()
