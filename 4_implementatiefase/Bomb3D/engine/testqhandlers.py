# -*- coding: utf-8 -*-
# 08/09 OGO 2.3.2
# Coded by: Anson

# First run QConverter to get data
# Then run QReaderEventWriter to start the right events
# Last send the gamestate to the output

import Queue
import event

class QReaderEventWriter(object):

  def __init__(self, inqueue, gamestate):
  
    # input conversion
    self.inqueue = inqueue
    self.gamestate = gamestate
  
  def getPlayer(self, playerID):
    for player in self.gamestate.players:
      if player.UUID == playerID:
        return player
  
  def handle(self, input):
    while True:
      input.run()
      events = self.gamestate.events
      
      while not self.inqueue.empty():
        # gets items from the queue
        item = self.inqueue.get(1)
        item = '1 ' + item # local testing
        ident, messageType, messageData = item.split(" ", 2)
        
        if messageType == "token":
          events.token.emit(self.gamestate.engine);
        
        # The player has moved the mouse
        if messageType == "m":
          cordX, cordY = messageData.split("x", 1)
          events.eMouseEvent.emit(self.gamestate, int(cordX), int(cordY), self.getPlayer(ident))
        
        # The player has sent a chat message
        elif messageType == "c":
          events.eChtMessage.emit(self.gamestate, messageData, self.getPlayer(ident))
        
        # The player has pressed a key / clicked a mouse button
        elif messageType == "b":
          messageData = messageData.strip()
          if messageData == "AcceForwOn":
            events.eAcceForwOn.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "AcceForwOff":
            events.eAcceForwOff.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "AcceBackOn":
            events.eAcceBackOn.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "AcceBackOff":
            events.eAcceBackOff.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "StepLeftOn":
            events.eStepLeftOn.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "StepLeftOff":
            events.eStepLeftOff.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "StepRghtOn":
            events.eStepRghtOn.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "StepRghtOff":
            events.eStepRghtOff.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "DropBombOn":
            events.eDropBombOn.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "DropBombOff":
            events.eDropBombOff.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "Powerup1On":
            events.ePowerup1On.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "Powerup1Off":
            events.ePowerup1Off.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "Powerup2On":
            events.ePowerup2On.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "Powerup2Off":
            events.ePowerup2Off.emit(self.gamestate, self.getPlayer(ident))
           
          elif messageData == "Powerup3On":
            events.ePowerup3On.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "Powerup3Off":
            events.ePowerup3Off.emit(self.gamestate, self.getPlayer(ident))
          
          elif messageData == "MinimapTOn":
            events.eMinimapTOn.emit(self.gamestate, self.getPlayer(ident))
          elif messageData == "MinimapTOff":
            events.eMinimapTOff.emit(self.gamestate, self.getPlayer(ident))
            
          else:
            print "Unhandled key: '" + messageData + "'"    
            
        elif messageType == "q": 
          if messageData == "escape":
            events.eNeatQuit.emit(self.gamestate, self.getPlayer(ident))

