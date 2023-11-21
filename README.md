### English

# ZIP Brute Force Tool

Welcome to the `zip_bruteforce_tool` project. This professional-grade Python tool is designed to perform brute force attacks on password-protected ZIP archives using powerful tools like John the Ripper and fcrackzip.

## Features
- Perform brute force attacks on ZIP files
- Leverage John the Ripper and fcrackzip for efficient password cracking
- Comprehensive scripts and utilities for generating test archives and running attacks
- Easy to extend and customize

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Tom-Souillard/zip_bruteforce_tool.git
    cd zip_bruteforce_tool
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install fcrackzip and John the Ripper:
    ```bash
    sudo apt-get install fcrackzip john
    ```

## Usage

### Generate Test Archives

Generate a test ZIP archive with a known password:
```bash
python scripts/generate_test_archives.py
```

### Run Brute Force Attack with fcrackzip

```bash
python scripts/run_fcrackzip.py path/to/your/test.zip
```

### Run Brute Force Attack with John the Ripper

First, extract the hash from the ZIP file:
```bash
python scripts/extract_zip_hash.py path/to/your/test.zip
```

Then, run John the Ripper:
```bash
python scripts/run_john.py zip_hash.txt
```

## Testing

Run unit tests to ensure the tool works correctly:
```bash
pytest
```

## Documentation

For detailed usage and customization instructions, please refer to the [documentation](docs/README.md).

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

---

<p>&nbsp;</p>
<p>&nbsp;</p>

### Française

# Outil de Bruteforce ZIP

Bienvenue dans le projet `zip_bruteforce_tool`. Cet outil Python de qualité professionnelle est conçu pour effectuer des attaques par brute force sur des archives ZIP protégées par mot de passe en utilisant des outils puissants comme John the Ripper et fcrackzip.

## Fonctionnalités
- Effectuer des attaques par brute force sur des fichiers ZIP
- Utiliser John the Ripper et fcrackzip pour un craquage de mot de passe efficace
- Scripts et utilitaires complets pour générer des archives de test et exécuter des attaques
- Facile à étendre et à personnaliser

## Installation

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/Tom-Souillard/zip_bruteforce_tool.git
    cd zip_bruteforce_tool
    ```

2. Installer les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

3. Installer fcrackzip et John the Ripper :
    ```bash
    sudo apt-get install fcrackzip john
    ```

## Utilisation

### Générer des Archives de Test

Générer une archive ZIP de test avec un mot de passe connu :
```bash
python scripts/generate_test_archives.py
```

### Exécuter une Attaque par Brute Force avec fcrackzip

```bash
python scripts/run_fcrackzip.py path/to/your/test.zip
```

### Exécuter une Attaque par Brute Force avec John the Ripper

Tout d'abord, extraire le hash du fichier ZIP :
```bash
python scripts/extract_zip_hash.py path/to/your/test.zip
```

Ensuite, exécuter John the Ripper :
```bash
python scripts/run_john.py zip_hash.txt
```

## Tests

Exécuter les tests unitaires pour s'assurer que l'outil fonctionne correctement :
```bash
pytest
```

## Documentation

Pour des instructions détaillées sur l'utilisation et la personnalisation, veuillez consulter la [documentation](docs/README.md).

## Licence

Ce projet est sous licence Apache License 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contribuer

Les contributions sont les bienvenues ! Veuillez lire les lignes directrices de [CONTRIBUTING](CONTRIBUTING.md) avant de soumettre une demande de tirage.