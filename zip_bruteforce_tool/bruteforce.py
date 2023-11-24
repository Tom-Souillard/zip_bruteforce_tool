import subprocess

def run_fcrackzip(zip_path: str, min_length: int = 1, max_length: int = 8, charset: str = 'aA1') -> str:
    """Run fcrackzip to brute force a ZIP file password.

    Args:
        zip_path (str): The path to the ZIP file to brute force.
        min_length (int): The minimum length of the password to try.
        max_length (int): The maximum length of the password to try.
        charset (str): The character set to use for brute force (a=lowercase, A=uppercase, 1=digits).

    Returns:
        str: The result of the fcrackzip command.
    """
    try:
        result = subprocess.run(
            ['fcrackzip', '-v', '-b', '-l', f'{min_length}-{max_length}', '-c', charset, '-u', zip_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"An error occurred: {e}"


def run_john(hash_file: str) -> str:
    """Run John the Ripper to brute force a password hash.

    Args:
        hash_file (str): The path to the file containing the password hash.

    Returns:
        str: The result of the John the Ripper command.
    """
    try:
        result = subprocess.run(
            ['john', hash_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"An error occurred: {e}"
