import os
from pathlib import Path


def run_migrate():
    migrate = Path(__file__).parent.joinpath("db", "migrations.py")
    os.environ["FLASK_APP"] = str(migrate)

    os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")


if __name__ == "__main__":
    run_migrate()
