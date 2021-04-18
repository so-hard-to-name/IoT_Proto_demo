# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
     
    def do_GET(self):

        f = open("temperature.txt", "r")
        temp_data = f.readlines()
        current = temp_data[-1]
        history = temp_data[-5:]
        print(history)


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))        
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>Latest Temperature</h1>", "utf-8"))
        self.wfile.write(bytes("<p>%s</p>" % current, "utf-8"))
        self.wfile.write(bytes("<h1>History</h1><p>only the last 5 histories</p>", "utf-8"))
        for h in history:
            self.wfile.write(bytes("<p>%s</p>" % h, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")