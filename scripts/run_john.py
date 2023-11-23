import subprocess
import sys


def run_john(hash_file: str) -> None:
    """Run John the Ripper to brute force a password hash.

    Args:
        hash_file (str): The path to the file containing the password hash.
    """
    try:
        result = subprocess.run(
            ['john', hash_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_john.py <path_to_hash_file>")
    else:
        run_john(sys.argv[1])
