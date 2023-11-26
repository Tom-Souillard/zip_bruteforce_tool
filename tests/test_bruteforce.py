import pytest
from zip_bruteforce_tool.bruteforce import run_fcrackzip, run_john
from zip_bruteforce_tool.utils import create_zip_file, extract_zip_hash
from zip_bruteforce_tool.constants import TEST_ZIP_FILE, HASH_FILE


def test_run_fcrackzip(monkeypatch):
    """Test the run_fcrackzip function with a mock subprocess."""

    def mock_subprocess_run(*args, **kwargs):
        class MockCompletedProcess:
            def __init__(self):
                self.stdout = "PASSWORD FOUND!!!!: password123"

        return MockCompletedProcess()

    monkeypatch.setattr('subprocess.run', mock_subprocess_run)

    result = run_fcrackzip(TEST_ZIP_FILE)
    assert "PASSWORD FOUND!!!!: password123" in result


def test_run_john(monkeypatch):
    """Test the run_john function with a mock subprocess."""

    def mock_subprocess_run(*args, **kwargs):
        class MockCompletedProcess:
            def __init__(self):
                self.stdout = "password123 (test.zip)"

        return MockCompletedProcess()

    monkeypatch.setattr('subprocess.run', mock_subprocess_run)

    result = run_john(HASH_FILE)
    assert "password123 (test.zip)" in result


@pytest.fixture
def setup_test_zip():
    """Fixture to create a test ZIP file and extract its hash."""
    create_zip_file(TEST_ZIP_FILE, 'password123')
    extract_zip_hash(TEST_ZIP_FILE)


def test_full_bruteforce_flow(setup_test_zip, monkeypatch):
    """Test the full bruteforce flow using fcrackzip and John the Ripper."""
    test_run_fcrackzip(monkeypatch)
    test_run_john(monkeypatch)
