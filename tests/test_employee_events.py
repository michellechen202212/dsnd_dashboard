import pytest
from pathlib import Path
from sqlite3 import connect

# Fixture: Path to the database
@pytest.fixture
def db_path():
    project_root = Path(__file__).resolve().parent.parent
    return project_root / 'python-package' / 'employee_events' / 'employee_events.db'

# Test: Database file exists
def test_db_exists(db_path):
    assert db_path.is_file(), f"Database not found at {db_path}"

# Fixture: Database connection
@pytest.fixture
def db_conn(db_path):
    return connect(db_path)

# Fixture: List of table names
@pytest.fixture
def table_names(db_conn):
    name_tuples = db_conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    return [x[0] for x in name_tuples]

# Test: Employee table exists
def test_employee_table_exists(table_names):
    assert 'employee' in table_names, "'employee' table is missing"

# Test: Team table exists
def test_team_table_exists(table_names):
    assert 'team' in table_names, "'team' table is missing"

# Test: Employee Events table exists
def test_employee_events_table_exists(table_names):
    assert 'employee_events' in table_names, "'employee_events' table is missing"

