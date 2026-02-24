#It waits until the task finishes before moving to the next line.
import time

def normal_function():
    print("Starting the normal function.")
    time.sleep(2)  # wait for 2 seconds to simulate a time-consuming task
    print("This is a normal function.")
    print("It executes sequentially.")
normal_function()
print("This line will execute after the normal function finishes.")