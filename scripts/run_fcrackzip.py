import subprocess
import sys


def run_fcrackzip(zip_path: str) -> None:
    """Run fcrackzip to brute force a ZIP file password.

    Args:
        zip_path (str): The path to the ZIP file to brute force.
    """
    try:
        result = subprocess.run(
            ['fcrackzip', '-v', '-b', '-l', '1-8', '-c', 'aA1', '-u', zip_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_fcrackzip.py <path_to_zip>")
    else:
        run_fcrackzip(sys.argv[1])
