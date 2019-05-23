from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory
import base64

class MyClientProtocol(WebSocketClientProtocol):

   def onConnect(self, response):
      print("Server connected: {0}".format(response.peer))

   def onOpen(self):
      print("WebSocket connection open.")
      
      # opening the image file and encoding in base64
      with open("image.jpg", "client") as image_file:
         encoded_string = base64.b64encode(image_file.read())

      print("Encoded size of the sent image: {0} bytes".format(len(encoded_string)))

      # sending the encoded image
      self.sendMessage(encoded_string) #encoded_string pass data to encoded
      #from self.sendMessage(encoded_string.encode('utf8'))


   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {0} bytes".format(len(payload)))
      else:
         # printing the size of the encoded image which is received
         print("Encoded size of the received image: {0} bytes".format(len(payload)))

   def onClose(self, wasClean, code, reason):
      print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':

   import sys

   from twisted.python import log
   from twisted.internet import reactor
   log.startLogging(sys.stdout)

   from autobahn.twisted.websocket import WebSocketClientFactory
   factory = WebSocketClientFactory()
   factory.protocol = MyClientProtocol

   reactor.connectTCP("127.0.0.1", 9000, factory)
   reactor.run()

