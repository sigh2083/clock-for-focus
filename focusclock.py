import time
import os

def timer(minutes):
    for i in range(minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end="\r")
        time.sleep(1)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    work_time = 25
    break_time = 5

    while True:
        print("开始工作！专注", work_time, "分钟。")
        timer(work_time)
        print("工作时间结束！休息", break_time, "分钟。")
        timer(break_time)
        clear_console()

if __name__ == "__main__":
    main()
