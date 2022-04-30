"""
https://docs.python.org/3/library/threading.html#lock-objects
"""
import click
import threading
import time

counter = 0
lock = threading.Lock()


def non_lock_count(thread_id):
    global counter

    counter
    print(f'{thread_id} Before: {counter}')

    counter += 1
    time.sleep(0.1)

    print(f'{thread_id} After: {counter}')


def lock_count(thread_id):
    global counter

    lock.acquire()
    print(f'{thread_id} Before: {counter}')

    counter += 1
    time.sleep(0.1)

    lock.release()
    print(f'{thread_id} After: {counter}')


def with_lock_count(thread_id):
    global counter

    # It's not possible to add a timeout using a with statement.
    # https://stackoverflow.com/questions/16740104/python-lock-with-statement-and-timeout
    with lock:
        print(f'{thread_id} Before: {counter}')

        counter += 1
        time.sleep(0.1)

        print(f'{thread_id} After: {counter}')


def lock_count_timeout(thread_id):
    global counter

    try:
        # Lock only for 0.05 seconds.
        lock.acquire(timeout=0.05)
        print(f'{thread_id} Before: {counter}')

        counter += 1
        time.sleep(0.1)

        lock.release()
        print(f'{thread_id} After: {counter}')
    except RuntimeError as e:
        # release unlocked lock
        print(f'{thread_id} {e}')


def locked_count(thread_id):
    global counter

    if lock.locked():
        print(f'{thread_id} Already locked')
    else:
        lock.acquire()
        print(f'{thread_id} Before: {counter}')

        counter += 1
        time.sleep(0.1)

        lock.release()
        print(f'{thread_id} After: {counter}')


def spawn(func):
    """Run increase_counter_and_print() with multiple threads."""
    for i in range(10):
        thread = threading.Thread(target=func, args=(i,))
        thread.start()


@click.command()
@click.option('--test-number', default=1, help='Number of test.')
def main(test_number):
    """Run thread lock tests."""
    if test_number == 1:
        spawn(non_lock_count)
    elif test_number == 2:
        spawn(lock_count)
    elif test_number == 3:
        spawn(with_lock_count)
    elif test_number == 4:
        spawn(lock_count_timeout)
    elif test_number == 5:
        spawn(locked_count)
    else:
        raise ValueError('Invalid test number.')


if __name__ == '__main__':
    main()

