from contextlib import contextmanager


class Lock:
    def __init__(self, lock_name):
        self.name = lock_name

    def acquire(self):
        print('%s lock acquired' % self.name)

    def release(self):
        print('%s lock released' % self.name)


@contextmanager
def locked(lock: Lock):
    lock.acquire()
    try:
        yield lock
    finally:
        lock.release()


class closing(object):
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, *exc_info):
        try:
            close_it = self.obj.close
        except AttributeError:
            pass
        else:
            close_it()


if __name__ == '__main__':
    lock1 = Lock('abc')
    with locked(lock1) as f:
        print('lock name = %s' % f.name)
