import time

def countdown_timer():
    try:
        total_seconds = int(input("Enter time in seconds for countdown: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    print("\nStarting countdown...")
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(timer_format, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up! Countdown finished.")

if __name__ == "__main__":
    countdown_timer()
