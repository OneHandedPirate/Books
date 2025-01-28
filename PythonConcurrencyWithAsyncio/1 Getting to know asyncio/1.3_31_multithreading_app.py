import threading


def hello_from_thread():
    print(f"Hello from {threading.current_thread()} thread!")


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(
    f"{total_threads} thread{'s' if total_threads > 1 else ''} {'are' if total_threads > 1 else 'is'} currently running"
)
print(f"Current thread name: {thread_name}")
hello_thread.join()
