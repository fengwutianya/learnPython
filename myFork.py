import os

print("process %s start." % os.getpid())
pid = os.fork()
if pid == 0:
    print("I am a child process (%s) and my parent process is (%s)." % (os.getpid(), os.getppid()))
else:
    print("I am the parent process (%s)" % (os.getpid()))