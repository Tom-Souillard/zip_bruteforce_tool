import pytest
import os
from zip_bruteforce_tool.utils import create_zip_file, extract_zip_hash
from zip_bruteforce_tool.constants import TEST_ZIP_FILE, HASH_FILE


def test_create_zip_file():
    """Test creating a ZIP file."""
    create_zip_file(TEST_ZIP_FILE, 'password123')
    assert os.path.exists(TEST_ZIP_FILE), "The ZIP file should be created."


def test_extract_zip_hash(monkeypatch):
    """Test extracting the hash from a ZIP file."""

    def mock_subprocess_run(*args, **kwargs):
        with open(HASH_FILE, 'w') as f:
            f.write("test.zip:$pkzip$1*1*2*0*8*24*69d5*e3d7*0000*0000*dfed*1848*0*12b8*0447*0000*0000")

        class MockCompletedProcess:
            def __init__(self):
                self.stderr = ""

        return MockCompletedProcess()

    monkeypatch.setattr('subprocess.run', mock_subprocess_run)

    extract_zip_hash(TEST_ZIP_FILE)
    assert os.path.exists(HASH_FILE), "The hash file should be created."
    with open(HASH_FILE, 'r') as f:
        content = f.read()
    assert "test.zip:$pkzip$1*1*2*0*8*24*69d5*e3d7*0000*0000*dfed*1848*0*12b8*0447*0000*0000" in content


@pytest.fixture
def setup_test_zip():
    """Fixture to create a test ZIP file."""
    create_zip_file(TEST_ZIP_FILE, 'password123')


def test_full_utils_flow(setup_test_zip, monkeypatch):
    """Test the full utility flow from creating a ZIP file to extracting its hash."""
    test_create_zip_file()
    test_extract_zip_hash(monkeypatch)
