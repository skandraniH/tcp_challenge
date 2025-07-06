import socket
import math
import re

def solve_challenge():
    host = "challenge01.root-me.org"
    port = 52002
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024).decode().strip()
        print("Received:", data)
        
        # Improved number extraction
        # Matches numbers only in the specific phrases we need
        num1 = float(re.search(r"square root of (\d+)", data).group(1))
        num2 = float(re.search(r"multiply by (\d+)", data).group(1))
        print(f"Numbers extracted: {num1}, {num2}")
        
        # Perform calculation
        result = math.sqrt(num1) * num2
        answer = round(result, 2)
        formatted_answer = "{:.2f}".format(answer)
        print("Sending:", formatted_answer)
        
        s.sendall(formatted_answer.encode() + b'\n')
        response = s.recv(1024).decode()
        print("Server response:", response)

solve_challenge()