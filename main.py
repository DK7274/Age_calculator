from guizero import *
from pydub import AudioSegment
import winsound
from datetime import datetime
import webbrowser
import ffmpeg
app = App("age calculator")
monthDictionary = {
    "january" : 1,
    "february":2,
    "march":3,
    "april":4,
    "may":5,
    "june":6,
    "july":7,
    "august":8,
    "september":9,
    "october":10,
    "november":11,
    "december":12
}
def close():
    filename = "applause.wav"
    winsound.PlaySound(filename,winsound.SND_FILENAME)
    webbrowser.open("https://www.youtube.com/watch?v=grd-K33tOSM")
    app.destroy()
def age_calculate():
    year = datetime.now().year - int(input_year.value)
    if len(input_month.value) >= 3:
        month = datetime.now().month - int(monthDictionary[input_month.value.lower()])
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
button = PushButton(app,text = "commit a major act of terrorism",command = close)
app.display()