import random
import datetime
MyQueue=[]
def ManageTaskSchedule():
  MyQueue.append("{} :: {}".format(str(datetime.datetime.now()),random.randint(10,99)))
  if len(MyQueue) > 15:
    MyQueue.pop(0)
