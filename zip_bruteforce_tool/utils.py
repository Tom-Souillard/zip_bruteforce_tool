import zipfile

def create_zip_file(file_name: str, password: str) -> None:
    """Create a ZIP file with a single text file inside.

    Args:
        file_name (str): The name of the ZIP file to create.
        password (str): The password to protect the ZIP file.
    """
    with zipfile.ZipFile(file_name, 'w') as zipf:
        zipf.writestr('test.txt', 'This is a test file.')
        zipf.setpassword(password.encode())


def extract_zip_hash(zip_path: str, output_file: str = 'zip_hash.txt') -> None:
    """Extract the hash from a ZIP file using zip2john.

    Args:
        zip_path (str): The path to the ZIP file to extract the hash from.
        output_file (str): The file to write the hash to.
    """
    import subprocess
    try:
        with open(output_file, 'w') as f:
            result = subprocess.run(
                ['zip2john', zip_path],
                stdout=f,
                stderr=subprocess.PIPE,
                text=True
            )
    except Exception as e:
        print(f"An error occurred: {e}")
