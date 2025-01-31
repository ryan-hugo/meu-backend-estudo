from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Manipula requisições GET
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("Hello, World! Esta é a página inicial.".encode('utf-8'))
            
        elif self.path == "/about":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("Esta é a página Sobre.".encode('utf-8'))
            
        else:
            self.send_error(404, "Página não encontrada.")
            
            
    # POST  
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_message = f"Você enviou {post_data.decode('utf-8')}"
        self.wfile.write(response_message.encode('utf-8'))
        
        
        
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8201):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    def signal_handler(sig, frame):
        print("\nServidor sendo interrompido...")
        httpd.server_close()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    print(f"Servidor rodando na porta {port} . . .")
    httpd.serve_forever()
        
if __name__ == '__main__':
    run()