"""litequeue tests

* Docs      https://litements.exampl.io/queue/
* Github    https://github.com/litements/litequeue
"""

from litequeue import SQLQueue


def test_basic():
    q = SQLQueue(':memory:')

    assert q.put('a') == 1
    assert q.put('b') == 2

    """
    e.g,
    {
        'message': 'a',
        'message_id': '1e49f8676615a8c900094a638c5edfde',
        'status': 1,
        'in_time': 1650726882,
        'lock_time': 1650726925,
        'done_time': None
    }
    """
    task = q.pop()

    assert task['message'] == 'a'
    assert task['status'] == 1

    q.done(task['message_id'])

    # The status of task changes to 2 in the database
    # but it doesn't change the task itself.
    assert task['status'] == 1


def test_qsize():
    q = SQLQueue(':memory:')

    assert q.put('a') == 1
    assert q.put('b') == 2

    assert q.qsize() == 2

    task = q.pop()

    # still 2
    assert q.qsize() == 2

    # changes the count after done
    q.done(task['message_id'])
    assert q.qsize() == 1


