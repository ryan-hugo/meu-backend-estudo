from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Manipula requisições GET
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Hello, World! Esta e a página inicial.")
        elif self.path == "/about":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Esta é a página Sobre.")
        else:
            self.send_error(404, "Página não encontrada.")
            
            
    # POST  
    def do_POST(self):
        content_lenght = int(self.headers['Content-Lenght'])
        post_data = self.rfile.read(content_lenght)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Você enviou: {post_data.decode('utf-8')}".enconde())
        
        
        
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando na porta {port}. . .")
    httpd.serve_forever()
        
        
if __name__ == '__main__':
    run()