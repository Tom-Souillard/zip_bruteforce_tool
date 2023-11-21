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


if __name__ == "__main__":
    create_zip_file('test.zip', 'password123')
    print("Test ZIP file 'test.zip' created with password 'password123'")
