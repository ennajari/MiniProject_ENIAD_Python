
import time
import threading
from playsound import playsound
def play_sound(file_path):
    playsound(file_path)
class IntervalTimer:
    def __init__(self, num_series, num_exercises, work_time, rest_time_exercise, rest_time_series):
        self.num_series = num_series
        self.num_exercises = num_exercises
        self.work_time = work_time
        self.rest_time_exercise = rest_time_exercise
        self.rest_time_series = rest_time_series
        self.is_paused = False
        self.is_stopped = False
    def start_timer(self):
        for series in range(self.num_series):
            if self.is_stopped:
                break
            print(f"Starting series {series + 1}/{self.num_series}")
            for exercise in range(self.num_exercises):
                if self.is_stopped:
                    break
                print(f"  Starting exercise {exercise + 1}/{self.num_exercises}")
                self.start_interval(self.work_time, "Work")
                if exercise < self.num_exercises - 1:
                    self.start_interval(self.rest_time_exercise, "Rest")
            if series < self.num_series - 1:
                self.start_interval(self.rest_time_series, "Series Rest")

    def start_interval(self, duration, phase):
        start_time = time.time()
        while time.time() - start_time < duration:
            if self.is_paused:
                start_time += 1
                time.sleep(1)
            elif self.is_stopped:
                break
            else:
                print(f"{phase} time remaining: {int(duration - (time.time() - start_time))} seconds", end='\r')
                time.sleep(1)
        if not self.is_stopped:
            threading.Thread(target=play_sound, args=("notification_sound.mp3",)).start()
        print()

    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("Timer paused.")
        else:
            print("Timer resumed.")

    def stop(self):
        self.is_stopped = True
        print("Timer stopped.")

def get_user_input():
    num_series = int(input("Enter number of series: "))
    num_exercises = int(input("Enter number of exercises per series: "))
    work_time = int(input("Enter work time for each exercise (seconds): "))
    rest_time_exercise = int(input("Enter rest time between exercises (seconds): "))
    rest_time_series = int(input("Enter rest time between series (seconds): "))
    return num_series, num_exercises, work_time, rest_time_exercise, rest_time_series

if __name__ == "__main__":
    num_series, num_exercises, work_time, rest_time_exercise, rest_time_series = get_user_input()
    timer = IntervalTimer(num_series, num_exercises, work_time, rest_time_exercise, rest_time_series)

    # Start the timer in a separate thread to handle pausing and stopping
    timer_thread = threading.Thread(target=timer.start_timer)
    timer_thread.start()

    while timer_thread.is_alive():
        command = input("Enter 'p' to pause/resume, 's' to stop: ").lower()
        if command == 'p':
            timer.pause()
        elif command == 's':
            timer.stop()
            timer_thread.join()
            break
