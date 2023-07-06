import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
entered_states=[]
missing_states=[]
data=pandas.read_csv("50_states.csv")
states=data['state'].tolist()
temp=states
while(len(entered_states)<50):
    answer_state=screen.textinput(title=f"{len(entered_states)}/50 States Correct",prompt="What's another state's name?").title()
    if(answer_state=="Exit"):
        for state in temp:
            if state not in entered_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        entered_states.append(answer_state)
        states.remove(answer_state)
        row=data[data['state']==answer_state]
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(row.x),int(row.y))
        t.write(answer_state)
screen.mainloop()