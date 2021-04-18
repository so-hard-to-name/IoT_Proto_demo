import socketserver
from datetime import datetime

HOST = "localhost"
PORT = 8081

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

        f = open("temperature.txt", "a")

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")        
        f.write(current_time + "   Temperature: " + data.decode("utf-8") + "\n")
        f.close()

        # print("{} wrote:".format(self.client_address[0]))
        # print(data)
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":    
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()