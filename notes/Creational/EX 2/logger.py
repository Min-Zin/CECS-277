"""
A Singleton Logger Class:
    A logger can often be hel[ful in recording errors or tracking data
    during the program's execution. All of the logs are written to a file
    that can be accessed anywhere in the program. It could be impractical
    for each method and class to reconstruct a separate Logger object, so
    it may be better to just have the single Logger that any method or class
    can access and input data into. Creating it as a Singleton, we can ensure
    that the Logger is a single shared resource usable throughout the program.
"""

class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            self._file = open("log.txt", "w")
            self._file.write("--Log Begin--\n")
            Logger._initialized = True

    def write_msg(self, msg):
        self._file.write(msg + "\n")
        self._file.flush()

    def close_file(self):
        self._file.close()