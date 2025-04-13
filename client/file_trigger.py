import time
import psutil
import subprocess
from shared.config import TARGET_FILENAME

def is_excel_file_open(target_name):
    for proc in psutil.process_iter(['name', 'cmdline']):
        if proc.info['name'] and 'EXCEL.EXE' in proc.info['name']:
            if proc.info['cmdline']:
                for arg in proc.info['cmdline']:
                    if target_name.lower() in arg.lower():
                        return True
    return False

def main():
    print(f"[CLIENT] '{TARGET_FILENAME}' 열림 감지 대기 중...")
    while True:
        if is_excel_file_open(TARGET_FILENAME):
            print("[CLIENT] 트리거 감지됨! 원격 스트리밍 시작.")
            subprocess.Popen(["python", "client/screen_sender.py"])
            subprocess.Popen(["python", "client/input_receiver.py"])
            break
        time.sleep(2)

if __name__ == "__main__":
    main()
