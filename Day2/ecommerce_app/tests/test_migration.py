import os
from alembic import command
from alembic.config import Config

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ALEMBIC_INI = os.path.join(PROJECT_ROOT, "alembic.ini")


def get_alembic_config():
    config = Config(ALEMBIC_INI)
    config.set_main_option("script_location", os.path.join(PROJECT_ROOT, "alembic"))
    return config


def test_alembic_upgrade():
    config = get_alembic_config()
    command.upgrade(config, "head")


def test_alembic_downgrade():
    config = get_alembic_config()
    command.downgrade(config, "base")