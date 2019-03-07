import struct
import time

_GLOBAL_HEADER = struct.pack('@IHHiIII', 2712847316, 2, 4, 0, 0, 65535, 1)


class Writer:
    def __init__(self, out):
        self._out = out

    def __enter__(self):
        self._file = open(self._out, 'wb') if self._out else None

        if self._file:
            self._file.write(_GLOBAL_HEADER)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()

    def write(self, package):
        if self._file is None:
            return

        sec, usec = map(int, str(time.time()).split('.'))

        self._file.write(struct.pack("@IIII", sec, usec, len(package), len(package)))
        self._file.write(package)
