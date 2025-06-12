from application import Application
from startup import set_startup


if __name__ == "__main__":
    set_startup()
    app = Application()
    app.start()
