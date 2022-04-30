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

    print(f'{thread_id} After: {counter}')
    lock.release()


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
    else:
        raise ValueError('Invalid test number.')


if __name__ == '__main__':
    main()

