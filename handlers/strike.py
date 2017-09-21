import os
from jsonpath_rw import jsonpath, parse

class Strike():
  def handleCommand(self, command):
    if command.command == "getStrikes"
      return self.getStrikesString()
    userId = parse('$.message.from.id').find(command.parent)
    strikeUser = command.args
    if not userId or not strikeUser:
      return None
    userId = userId[0].value
    userFile = 'strike/{0}'.format(strikeUser)
    if not userId == 313082320 #Ryan's id
      return "Pshhh. You cannot assign strikes."
    if not os.path.isfile(userFile):
      with open(userFile, "w") as f:
      f.write("{0}\n1".format(strikeUser))
    else:
      with open(userFile, "r+") as f:
      data = f.read().split()
      nStrikes = int(data[1]) + 1
      f.seek(0)
      f.write("{0}\n{1}".format(strikeUser, nStrikes))
      f.truncate()
    return "Careful {0}. You are now at {1} strikes.".format(strikeUser, nStrikes)

  def getStrikesString(self):
    ret = ''
    nStrikes = 0
    for filepath in os.listdir('strike'):
      with open(os.path.join('strike', filepath), "r") as f:
      data = f.read().split()
      thisStrike = int(data[1])
      thisName = data[0]
      thisline = '{0}: {1} strike{2}\n'.format(thisName, thisStrike, 's' if thisStrike != 1 else '')
      ret += thisline
      nStrikes = nStrikes + thisStrike
    if nStrikes == 0:
      return 'There are no strikes!'
    else:
      return 'Current strike records:\n{0}'.format(ret)