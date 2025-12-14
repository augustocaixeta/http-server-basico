import socket
from urllib.parse import unquote

HOST = "localhost"
PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor rodando em http://{HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"\nConexão recebida de: {client_address}")

    request_bytes = client_socket.recv(1024)
    request = request_bytes.decode()
    lines = request.splitlines()

    if not lines:
        client_socket.close()
        continue

    first = lines[0]
    method, path, _ = first.split()

    status = "200 OK"
    body = ""

    if path == "/":
        body = "Servidor HTTP básico."
    elif path.startswith("/uppercase"):
        if "text=" in path:
            text = path.split("text=")[1]
            text = unquote(text)
            body = text.upper()
        else:
            body = "Use /uppercase?text=seu_texto"
    else:
        status = "404 Not found"
        body = "Página não encontrada"

    response = (
        f"HTTP/1.1 {status}\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
        f"{body}"
    )

    client_socket.sendall(response.encode())
    client_socket.close()