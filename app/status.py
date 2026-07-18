import sys


class Status:

    @staticmethod
    def update(message: str):
        sys.stdout.write("\r" + " " * 80)
        sys.stdout.flush()

        sys.stdout.write(f"\r🤖 {message}")
        sys.stdout.flush()

    @staticmethod
    def done():
        sys.stdout.write("\r" + " " * 80)
        sys.stdout.write("\r")
        sys.stdout.flush()