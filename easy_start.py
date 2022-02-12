import os
from migrate import run_migrate
from start import start

if __name__ == "__main__":
    run_migrate()
    start()