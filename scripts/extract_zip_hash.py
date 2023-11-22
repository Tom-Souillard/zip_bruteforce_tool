import subprocess
import sys


def extract_zip_hash(zip_path: str) -> None:
    """Extract the hash from a ZIP file using zip2john.

    Args:
        zip_path (str): The path to the ZIP file to extract the hash from.
    """
    try:
        with open('zip_hash.txt', 'w') as f:
            result = subprocess.run(
                ['zip2john', zip_path],
                stdout=f,
                stderr=subprocess.PIPE,
                text=True
            )
        print("Hash extracted to zip_hash.txt")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_zip_hash.py <path_to_zip>")
    else:
        extract_zip_hash(sys.argv[1])
