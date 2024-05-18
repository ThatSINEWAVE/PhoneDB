<div align="center">

# PhoneDB

PhoneDB aims to create a comprehensive database of every possible phone number on the planet. Currently, the database includes all possible phone numbers in Romania. The Romanian phone numbers are organized into individual folders by area code, each containing zip files with unique phone numbers in JSON format. This project is strictly for educational and data research purposes and contains no personal data linked to any phone number.

</div>

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Project Structure

### Romania
- The `Romania` folder contains all possible phone numbers for the following area codes:

  <details>
  <summary>Click to expand the list of area codes</summary>
  
  - 021: Bucharest
  - 031: Ilfov County
  - 230: Suceava County
  - 231: Botoșani County
  - 232: Iași County
  - 233: Neamț County
  - 234: Bacău County
  - 235: Vaslui County
  - 236: Galați County
  - 237: Vrancea County
  - 238: Buzău County
  - 239: Brăila County
  - 240: Tulcea County
  - 241: Constanța County
  - 242: Călărași County
  - 243: Ialomița County
  - 244: Prahova County
  - 245: Dâmbovița County
  - 246: Giurgiu County
  - 247: Teleorman County
  - 248: Argeș County
  - 249: Olt County
  - 250: Dolj County
  - 251: Mehedinți County
  - 252: Gorj County
  - 253: Vâlcea County
  - 254: Hunedoara County
  - 255: Caraș-Severin County
  - 256: Timiș County
  - 257: Arad County
  - 258: Alba County
  - 259: Bihor County
  - 260: Satu Mare County
  - 261: Maramureș County
  - 262: Sălaj County
  - 263: Bistrița-Năsăud County
  - 264: Cluj County
  - 265: Mureș County
  - 266: Harghita County
  - 267: Covasna County
  - 268: Brașov County
  - 269: Sibiu County
  </details>


- Each area code has its own folder named in the format `(AREA_CODE)_NUMBERS`, containing 10 zip files. Each zip file includes a JSON file with either 1 million or 10 million unique numbers, depending on the area code. Specifically, the 07 area code has 10 million numbers per zip file, while the others have 1 million numbers per zip file.

### Generators

- The `Generators` folder within the `Romania` directory contains all 43 Python scripts used to create the database. Each script corresponds to a specific area code.

<div align="center">

## [Join my discord server](https://discord.gg/2nHHHBWNDw)

</div>

## Usage

### Cloning Specific Parts of the Database

Due to the large size of the database, it is not feasible or efficient to clone the entire repository. To clone specific parts of the repository, use sparse checkout.

#### Steps to Perform a Sparse Checkout

1. **Initialize a new Git repository:**
   ```sh
   git init PhoneDB
   cd PhoneDB
   ```

2. **Set up sparse checkout:**
   ```sh
   git remote add origin <repository-url>
   git config core.sparseCheckout true
   ```

3. **Specify the directories to clone:**
   ```sh
   echo "Romania/021_NUMBERS/" >> .git/info/sparse-checkout
   echo "Romania/031_NUMBERS/" >> .git/info/sparse-checkout
   # Add additional lines for other directories as needed
   ```

4. **Pull the specified content:**
   ```sh
   git pull origin main
   ```

### Example

To clone only the Bucharest and Ilfov County numbers:
1. Follow steps 1 and 2 above.
2. Specify the directories:
   ```sh
   echo "Romania/021_NUMBERS/" >> .git/info/sparse-checkout
   echo "Romania/031_NUMBERS/" >> .git/info/sparse-checkout
   ```
3. Pull the specified content:
   ```sh
   git pull origin main
   ```

## Disclaimer

This project is strictly for educational and data research purposes. The database will always contain only the phone numbers, with no other data, ensuring there is no link between the numbers and real people. The intention is not to cause any harm or breach privacy.

## Contributions

Contributions are welcome! If you have any ideas for improvement or want to fix a bug, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).