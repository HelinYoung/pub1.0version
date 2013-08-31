from http.server import HTTPServer,CGIHTTPRequestHandler  
port = 8080  
httpd = HTTPServer(('',port),CGIHTTPRequestHandler) #创建一个服务器  
print("Strating simpleHttpd on port: "+str(httpd.server_port))  
httpd.serve_forever()