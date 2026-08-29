import time

def countdown_timer(seconds):
    print(f"\nTimer started for {seconds} seconds...\n")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(timer_format)
        time.sleep(1)
        seconds -= 1
    
    print("00:00")
    print("Time's up! ⏰")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter time in seconds: "))
        if user_input <= 0:
            print("Please enter a positive number of seconds.")
        else:
            countdown_timer(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
