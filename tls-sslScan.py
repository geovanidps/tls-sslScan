#!/usr/bin/env python3
import ssl
import socket

def check_ssl_tls_version(host, port):
    # Create a new SSL context with the highest version of TLS
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)

    # Create a socket and connect to the server
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            # Get the version of the SSL/TLS protocol used by the connection
            version = ssock.version()

    # Check the version and print the result
    if version == 'SSLv3':
        print(f"The SSL version used is {version}. This is vulnerable.")
    elif version == 'TLSv1' or version == 'TLSv1.1' or version == 'TLSv1.2':
        print(f"The TLS version used is {version}. This is vulnerable.")
    elif version == 'TLSv1.3':
        print(f"The TLS version used is {version}. This is not vulnerable.")
    else:
        print("Could not identify the SSL/TLS version :/")

def main():
    # Get the server address from the user
    server = input("Enter the server address (e.g., example.com): ")
    port = 443  # Use port 443 for SSL/TLS

    # Call the function to check the SSL/TLS version
    check_ssl_tls_version(server, port)

if __name__ == "__main__":
    main()
