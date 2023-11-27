### English

# Installation Instructions

Follow these steps to install the `zip_bruteforce_tool`:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Tom-Souillard/zip_bruteforce_tool.git
    cd zip_bruteforce_tool
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install fcrackzip and John the Ripper**:
    - On Debian/Ubuntu:
      ```bash
      sudo apt-get install fcrackzip john
      ```

4. **Install the package in editable mode**:
    ```bash
    pip install -e .
    ```

5. **Verify the installation by running one of the scripts**:
    ```bash
    generate_test_archives
    ```

6. **Run the unit tests to ensure everything is working correctly**:
    ```bash
    pytest
    ```

---
<p>&nbsp;</p>
<p>&nbsp;</p>

### Français

# Instructions d'Installation

Suivez ces étapes pour installer le `zip_bruteforce_tool` :

1. **Cloner le dépôt** :
    ```bash
    git clone https://github.com/Tom-Souillard/zip_bruteforce_tool.git
    cd zip_bruteforce_tool
    ```

2. **Installer les packages Python requis** :
    ```bash
    pip install -r requirements.txt
    ```

3. **Installer fcrackzip et John the Ripper** :
    - Sur Debian/Ubuntu :
      ```bash
      sudo apt-get install fcrackzip john
      ```

4. **Installer le package en mode édition** :
    ```bash
    pip install -e .
    ```

5. **Vérifier l'installation en exécutant un des scripts** :
    ```bash
    generate_test_archives
    ```

6. **Exécuter les tests unitaires pour s'assurer que tout fonctionne correctement** :
    ```bash
    pytest
    ```