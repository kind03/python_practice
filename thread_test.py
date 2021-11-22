import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    status = ''
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        # flush()
        time.sleep(.1)
        if not signal.go:
            break
    # use blank space to cover the previous progress word -- "\ thinking!",
    # and then use backspace(\x08) the cursor back into the begin
    # actually in cmd \x08 can only move the cursor,
    # but in Pycharm Debug windows \x08 can actually delete characters.
    write(' ' * len(status) + '\x08' * len(status))
    # if use print, will automatically start a new line, and then print the content
    # write('\n')  = print('')
    print('Finished!')
    # write('\n')


def slow_function():
    time.sleep(3)
    return 4


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    # spinner.join()
    # print('\n')
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()

