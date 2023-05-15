
class EventedThing:

  def __init__(self):
    self.myObj ={}

  def work(self):
    return "hello"

  def on(self,event,cb):
    self.myObj[event]=cb


  def trigger (self,event, args):
    if(event in self.myObj.keys()):
      self.myObj[event](args)

eventedThing = EventedThing()

def hi(name):
  print('Nice to meet you, ' + name + '.');


eventedThing.on('meet',hi)
eventedThing.trigger('meet', 'Sarah')
print("==============================")
eventedThing.on('click',hi)
eventedThing.trigger('click', 'Rahim')