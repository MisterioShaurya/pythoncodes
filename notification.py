import datetime
from plyer import notification
notification.notify(
    title = "To-Do List".format(datetime.date.today()),
    message = "1.Learn more about python \n 2.Make new projects \n 3.Design webpage",
    app_icon = "D:/icons/Slogografientnobgico.ico",
    timeout = 10
)