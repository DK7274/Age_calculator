from guizero import *
from datetime import datetime
app = App("age calculator")
monthDictionary = {
    "January" : 1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}
def reset():
    app.destroy()
    app.display()
def age_calculate():
    year = datetime.now().year - int(input_year.value)
    if len(input_month.value) >= 3:
        month = datetime.now().month - int(monthDictionary[input_month.value])
    else:
        month = datetime.now().month - int(input_month.value)
    day = datetime.now().day - int(input_day.value)
    if month <=0:
        month = month + 12
        year = year -1
    if day <=0:
        month -= 1
        day += 30
    if month >= 12:
        year += 1
        month -= 12
    age = Text(app,text=input_name.value + ", your age is: "+ str(day) + " days, " + str(month) + " months and " +str(year) + " years old.")
app.bg = "#a1a38c"
message = Text(app, text="Age calculator")
message = Text(app,text="Input Name")
input_name = TextBox(app)
message = Text(app,text="Input Year Born")
input_year =TextBox(app)
message = Text(app,text="Input Month Born")
input_month = TextBox(app)
message = Text(app,text="Input Day Born")
input_day = TextBox(app)
button = PushButton(app,text = "calculate age",command= age_calculate)
button = PushButton(app,text = "reset",command = reset)
app.display()