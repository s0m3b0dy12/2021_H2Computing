import random
import socket

EOL = b'\r\n'

COLOURS = [
    'red', 'orange', 'blue', 'purple',
    '#C0C000', # dark yellow
    '#00C000' # dark green
]

MESSAGES = ['Hello, World!', 'Computing is Fun', 'Alamak!']

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 8000))
listen_socket.listen()


def handle_request(new_socket):
    # Keep loading request until end of first line (\r\n).
    request = b''
    while EOL not in request:
        received = new_socket.recv(1024)
        if received == b'':
            new_socket.close()
            return
        request += received
# Extract first line and split it into three.
# Requested path is always the second part.
    index = request.index(EOL)
    first_line = request[:index].decode()
    path = first_line.split()[1]
# Start response with standard HTTP status line.
    response = b'HTTP/1.1 200 OK' + EOL
# Generate CSS document for response if path is '/css'.
# Otherwise, generate HTML document for response.
    if path == '/css':
        # Generate CSS document.
        border_colour = random.choice(COLOURS)
        text_colour = random.choice(COLOURS)
        body = 'p {{ border: 5px solid {0}; color: {1};'
        body += 'font‐size: 72px; padding: 20px; }}'
        body = body.format(border_colour, text_colour)
        body = body.encode()
        
# Append HTTP header fields to response.
        response += b'Content-Type: text/css' + EOL
        response += b'Content-Length: '
        response += str(len(body)).encode() + EOL
    else:
        msg = random.choice(MESSAGES)
        body = '<!DOCTYPE html>\n<html>'
        body += '<head><title>{0}</title>'
        body += '<link rel="stylesheet" href="/css"></head>'
        body += '<body><p>{0}</p></body></html>'
        body = body.format(msg).encode()

        # Append HTTP header fields to response.
        response += b'Content-Type: text/html' + EOL
        response += b'Content-Length: '
        response += str(len(body)).encode() + EOL

    # Append empty line to response.
    response += EOL
    # Append document as message body.
    response += body
    # Send the response and close the socket.
    new_socket.sendall(response)
    new_socket.close()


while True:
    new_socket, addr = listen_socket.accept()
    handle_request(new_socket)
