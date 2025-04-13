import socket
import ssl
import struct
import pickle
import pyautogui
import numpy as np
import cv2
from shared.config import SERVER_IP, SCREEN_PORT, CA_CERT_PATH

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=CA_CERT_PATH)
context.check_hostname = False

with socket.create_connection((SERVER_IP, SCREEN_PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_IP) as ssock:
        print("[CLIENT] 화면 전송 시작")
        while True:
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            data = pickle.dumps(frame)
            size = struct.pack(">L", len(data))
            ssock.sendall(size + data)
