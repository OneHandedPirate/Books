import os
import threading


print(f"Python-process with id: {os.getpid()} is running")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(
    f"{total_threads} thread{'s' if total_threads > 1 else ''} {'are' if total_threads > 1 else 'is'} currently running"
)
print(f"Current thread name: {thread_name}")
