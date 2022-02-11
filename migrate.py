import os
from pathlib import Path


if __name__ == "__main__":
    migrate = Path(__file__).parent.joinpath("db", "migrations.py")
    os.environ["FLASK_APP"] = str(migrate)

    os.system("flask db init")
    os.system("flask db migrate")
    os.system("flask db upgrade")
