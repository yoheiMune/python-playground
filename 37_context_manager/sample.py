"""
    Sample for Context Manager.

    References:
        - https://docs.python.jp/3/library/stdtypes.html#context-manager-types
        - https://docs.python.jp/3/reference/datamodel.html#with-statement-context-managers
        - https://docs.python.jp/3/library/contextlib.html

    Usage:
        $ python3 sample.py
"""
from datetime import datetime

"""
    Basic Usage.
"""
class Timer(object):
    def __enter__(self):
        self.timer = datetime.now()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.show()
    def show(self):
        diff = (datetime.now() - self.timer).microseconds / 1000
        print("time: {}ms".format(diff))
with Timer() as t:
    val = 0
    for i in range(1000000):
        if i % 100000 == 0:
            t.show()
        val += i

"""
    Treat Exceptions.
"""
import traceback
class OnigiriException(object):
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)   # <type 'exceptions.IOError'>
        print(exc_value)  # [Errno 2] No such file or directory: 'notfound.txt'
        print(traceback)  # <traceback object at 0x104362248>
        return True
with OnigiriException():
    open("notfound.txt")
print("After")

"""
    @contextlib.contextmanager
"""
from contextlib import contextmanager
@contextmanager
def tag(name):
    print("<{}>".format(name))
    yield "hello"
    print("</{}>".format(name))
with tag("h1") as msg:
    print(msg + "foo")
# <h1>
# hellofoo
# </h1>

"""
    contextlib.closing(thing)
"""
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen("http://www.yoheim.net/image/500.jpg")) as res:
    print("image: {} bytes".format(len(res.read())))


"""
    context.redirect_stdout(new_target)
    context.redirect_stderr(new_target)
"""
from contextlib import redirect_stdout
import io
f = io.StringIO()
with redirect_stdout(f):
    print("Hello Hello Hello")
s = f.getvalue()
print("io.StringIO:", s)  # io.StringIO: Hello Hello Hello


"""
    class contextlib.ContextDecorator
"""
from contextlib import ContextDecorator
class mycontext(ContextDecorator):
    def __enter__(self):
        print("Starting.")
        return self
    def __exit__(self, *exc):
        print("Finishing.")
        return False
@mycontext()
def f():
    print("f() is called.")
f()
# Starting.
# f() is called.
# Finishing.

with mycontext():
    print("in with block.")
# Starting.
# in with block.
# Finishing.

"""
    class contextlib.ExitStack
"""
from contextlib import ExitStack
from urllib.request import urlopen
fnames = [
    "http://www.yoheim.net/image/500.jpg",
    "http://www.yoheim.net/image/501.jpg",
    "http://www.yoheim.net/image/502.jpg"
]
with ExitStack() as stack:
    responses = [stack.enter_context(urlopen(fname)) for fname in fnames]
    # All request stream are opened.
# All requests are closed.
