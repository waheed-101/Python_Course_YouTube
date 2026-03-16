# Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.



import time

wait_time = 1
maximum_retries = 5
attempts = 0

while attempts < maximum_retries:
    print(f"Attempts: {attempts + 1} - Wait Time: {wait_time} sec")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
