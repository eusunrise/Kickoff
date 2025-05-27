from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import sqlite3
import os

PORTA = 8000

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/login":
            self.enviar_arquivo("login.html")
        elif self.path == "/cadastro":
            self.enviar_arquivo("cadastro.html")
        elif self.path == "/home":
            self.enviar_arquivo("home.html")
        elif self.path.startswith("/static/"):
            try:
                with open(self.path[1:], 'rb') as file:
                    self.send_response(200)
                    if self.path.endswith(".css"):
                        self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_error(404, "Arquivo estático não encontrado")
        else:
            self.send_error(404, "Página não encontrada")




    def do_POST(self):
        comprimento = int(self.headers['Content-Length'])
        dados = self.rfile.read(comprimento).decode('utf-8')
        dados = parse_qs(dados)

        if self.path == "/login":
            self.processar_login(dados)
        elif self.path == "/cadastro":
            self.processar_cadastro(dados)

    def enviar_arquivo(self, nome_arquivo):
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'rb') as f:
                conteudo = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(conteudo)
        else:
            self.send_error(404, "Arquivo nao encontrado")

    def processar_login(self, dados):
        username = dados.get("username", [""])[0]
        senha = dados.get("senha", [""])[0]

        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND senha=?", (username, senha))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            self.send_response(302)
            self.send_header("Location", "/home")
            self.end_headers()
        else:
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b"Login invalido.")

    def processar_cadastro(self, dados):
        username = dados.get("username", [""])[0]
        senha = dados.get("senha", [""])[0]

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (username, senha))
            conn.commit()
            conn.close()

            self.send_response(302)
            self.send_header("Location", "/login")
            self.end_headers()
        except sqlite3.IntegrityError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Usuario ja existe.")

if __name__ == "__main__":
    servidor = HTTPServer(('', PORTA), Servidor)
    print(f"Servidor rodando em http://localhost:{PORTA}")
    servidor.serve_forever()
