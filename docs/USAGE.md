### English 

# Usage Instructions

Follow these steps to use the `zip_bruteforce_tool`:

## Generate Test Archives

This script generates a test ZIP archive with a known password, useful for testing purposes.

```bash
python scripts/generate_test_archives.py
```

- **Output**: A file named `test.zip` is created with the password `password123`.

## Run Brute Force Attack with fcrackzip

This script performs a brute force attack on a password-protected ZIP file using `fcrackzip`.

```bash
python scripts/run_fcrackzip.py path/to/your/test.zip
```

- **Input**: Path to the ZIP file to be brute forced.
- **Output**: Prints the result of the brute force attempt, including the discovered password if successful.

## Run Brute Force Attack with John the Ripper

### Step 1: Extract the Hash from the ZIP File

This script uses `zip2john` to extract the hash from the ZIP file, which is then used by John the Ripper.

```bash
python scripts/extract_zip_hash.py path/to/your/test.zip
```

- **Input**: Path to the ZIP file.
- **Output**: A file named `zip_hash.txt` containing the hash of the ZIP file.

### Step 2: Run John the Ripper

This script uses John the Ripper to brute force the password hash extracted from the ZIP file.

```bash
python scripts/run_john.py zip_hash.txt
```

- **Input**: Path to the hash file (`zip_hash.txt`).
- **Output**: Prints the result of the brute force attempt, including the discovered password if successful.

## Run Unit Tests

To ensure everything is working correctly, run the unit tests provided with the project.

```bash
pytest
```

- **Output**: Results of the tests, indicating pass or fail status for each test case.

---
<p>&nbsp;</p>
<p>&nbsp;</p>

#### Français

# Instructions d'Utilisation

Suivez ces étapes pour utiliser le `zip_bruteforce_tool` :

## Générer des Archives de Test

Ce script génère une archive ZIP de test avec un mot de passe connu, utile pour les tests.

```bash
python scripts/generate_test_archives.py
```

- **Sortie** : Un fichier nommé `test.zip` est créé avec le mot de passe `password123`.

## Exécuter une Attaque par Brute Force avec fcrackzip

Ce script effectue une attaque par brute force sur un fichier ZIP protégé par mot de passe en utilisant `fcrackzip`.

```bash
python scripts/run_fcrackzip.py path/to/your/test.zip
```

- **Entrée** : Chemin vers le fichier ZIP à attaquer par brute force.
- **Sortie** : Affiche le résultat de la tentative de brute force, y compris le mot de passe découvert si l'attaque réussit.

## Exécuter une Attaque par Brute Force avec John the Ripper

### Étape 1 : Extraire le Hash du Fichier ZIP

Ce script utilise `zip2john` pour extraire le hash du fichier ZIP, qui est ensuite utilisé par John the Ripper.

```bash
python scripts/extract_zip_hash.py path/to/your/test.zip
```

- **Entrée** : Chemin vers le fichier ZIP.
- **Sortie** : Un fichier nommé `zip_hash.txt` contenant le hash du fichier ZIP.

### Étape 2 : Exécuter John the Ripper

Ce script utilise John the Ripper pour attaquer par brute force le hash du mot de passe extrait du fichier ZIP.

```bash
python scripts/run_john.py zip_hash.txt
```

- **Entrée** : Chemin vers le fichier contenant le hash (`zip_hash.txt`).
- **Sortie** : Affiche le résultat de la tentative de brute force, y compris le mot de passe découvert si l'attaque réussit.

## Exécuter les Tests Unitaires

Pour s'assurer que tout fonctionne correctement, exécutez les tests unitaires fournis avec le projet.

```bash
pytest
```

- **Sortie** : Résultats des tests, indiquant le statut de réussite ou d'échec de chaque cas de test.