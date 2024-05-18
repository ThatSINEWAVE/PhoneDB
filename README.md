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
  <summary>Click to expand the list of Romanian area codes</summary>

  |         REGION        |   CODE    |
  |:---------------------:|:---------:|
  |   Bucharest Capital   |   021    |
  |      Ilfov County     |   031    |
  |     Suceava County    |   230    |
  |    Botoșani County    |   231    |
  |      Iași County      |   232    |
  |      Neamț County     |   233    |
  |      Bacău County     |   234    |
  |     Vaslui County     |   235    |
  |     Galați County     |   236    |
  |     Vrancea County    |   237    |
  |      Buzău County     |   238    |
  |     Brăila County     |   239    |
  |     Tulcea County     |   240    |
  |    Constanța County   |   241    |
  |    Călărași County    |   242    |
  |    Ialomița County    |   243    |
  |     Prahova County    |   244    |
  |    Dâmbovița County   |   245    |
  |     Giurgiu County    |   246    |
  |    Teleorman County   |   247    |
  |      Argeș County     |   248    |
  |       Olt County      |   249    |
  |      Dolj County      |   250    |
  |    Mehedinți County   |   251    |
  |      Gorj County      |   252    |
  |     Vâlcea County     |   253    |
  |    Hunedoara County   |   254    |
  |  Caraș-Severin County |   255    |
  |      Timiș County     |   256    |
  |      Arad County      |   257    |
  |      Alba County      |   258    |
  |      Bihor County     |   259    |
  |    Satu Mare County   |   260    |
  |    Maramureș County   |   261    |
  |      Sălaj County     |   262    |
  | Bistrița-Năsăud County |   263    |
  |      Cluj County      |   264    |
  |      Mureș County     |   265    |
  |    Harghita County    |   266    |
  |     Covasna County    |   267    |
  |     Brașov County     |   268    |
  |     Sibiu County      |   269    |
</details>

- Each area code has its own folder named in the format `(AREA_CODE)_NUMBERS`, containing 10 zip files. Each zip file includes a JSON file with either 1 million or 10 million unique numbers, depending on the area code. Specifically, the 07 area code has 10 million numbers per zip file, while the others have 1 million numbers per zip file.

### Generators

- The `Generators` folder within the `Romania` directory contains all 43 Python scripts used to create the database. Each script corresponds to a specific area code.

### Global list
- Below you can find a list of all countries and their phone number code used aswell as a checkmark on those that have been indexed inside the database.

<details>
  <summary>Click to expand the list of countries and codes</summary>

  |        COUNTRY         |   CODE    |  INDEXED  |
  |:----------------------:|:---------:|:---------:|
  |        Canada          |     1     |     ❌     |
  |    United States       |     1     |     ❌     |
  |     Kazakhstan         |     7     |     ❌     |
  |        Russia          |     7     |     ❌     |
  |        Egypt           |    20     |     ❌     |
  |     South Africa       |    27     |     ❌     |
  |        Greece          |    30     |     ❌     |
  |     Netherlands        |    31     |     ❌     |
  |       Belgium          |    32     |     ❌     |
  |        France          |    33     |     ❌     |
  |        Spain           |    34     |     ❌     |
  |       Hungary          |    36     |     ❌     |
  |        Italy           |    39     |     ❌     |
  |       Romania          |    40     |     ✅     |
  |     Switzerland        |    41     |     ❌     |
  |       Austria          |    43     |     ❌     |
  |    United Kingdom      |    44     |     ❌     |
  |       Denmark          |    45     |     ❌     |
  |        Sweden          |    46     |     ❌     |
  |        Norway          |    47     |     ❌     |
  | Svalbard and Jan Mayen |    47     |     ❌     |
  |        Poland          |    48     |     ❌     |
  |       Germany          |    49     |     ❌     |
  |        Peru            |    51     |     ❌     |
  |        Mexico          |    52     |     ❌     |
  |        Cuba            |    53     |     ❌     |
  |      Argentina         |    54     |     ❌     |
  |        Brazil          |    55     |     ❌     |
  |        Chile           |    56     |     ❌     |
  |      Colombia          |    57     |     ❌     |
  |      Venezuela         |    58     |     ❌     |
  |      Malaysia          |    60     |     ❌     |
  |      Australia         |    61     |     ❌     |
  |   Christmas Island     |    61     |     ❌     |
  |    Cocos Islands       |    61     |     ❌     |
  |     Indonesia          |    62     |     ❌     |
  |     Philippines        |    63     |     ❌     |
  |    New Zealand         |    64     |     ❌     |
  |       Pitcairn         |    64     |     ❌     |
  |      Singapore         |    65     |     ❌     |
  |      Thailand          |    66     |     ❌     |
  |        Japan           |    81     |     ❌     |
  |     South Korea        |    82     |     ❌     |
  |      Vietnam           |    84     |     ❌     |
  |        China           |    86     |     ❌     |
  |       Turkey           |    90     |     ❌     |
  |        India           |    91     |     ❌     |
  |      Pakistan          |    92     |     ❌     |
  |     Afghanistan        |    93     |     ❌     |
  |      Sri Lanka         |    94     |     ❌     |
  |       Myanmar          |    95     |     ❌     |
  |        Iran            |    98     |     ❌     |
  |     South Sudan        |   211     |     ❌     |
  |       Morocco          |   212     |     ❌     |
  |   Western Sahara       |   212     |     ❌     |
  |       Algeria          |   213     |     ❌     |
  |       Tunisia          |   216     |     ❌     |
  |        Libya           |   218     |     ❌     |
  |       Gambia           |   220     |     ❌     |
  |       Senegal          |   221     |     ❌     |
  |     Mauritania         |   222     |     ❌     |
  |        Mali            |   223     |     ❌     |
  |       Guinea           |   224     |     ❌     |
  |     Ivory Coast        |   225     |     ❌     |
  |     Burkina Faso       |   226     |     ❌     |
  |        Niger           |   227     |     ❌     |
  |        Togo            |   228     |     ❌     |
  |        Benin           |   229     |     ❌     |
  |      Mauritius         |   230     |     ❌     |
  |       Liberia          |   231     |     ❌     |
  |    Sierra Leone        |   232     |     ❌     |
  |       Ghana            |   233     |     ❌     |
  |       Nigeria          |   234     |     ❌     |
  |        Chad            |   235     |     ❌     |
  | Central African Republic|  236     |     ❌     |
  |      Cameroon          |   237     |     ❌     |
  |     Cape Verde         |   238     |     ❌     |
  | Sao Tome and Principe  |   239     |     ❌     |
  | Equatorial Guinea      |   240     |     ❌     |
  |       Gabon            |   241     |     ❌     |
  | Republic of the Congo  |   242     |     ❌     |
  |Democratic Republic of the Congo| 243|    ❌     |
  |       Angola           |   244     |     ❌     |
  |    Guinea-Bissau       |   245     |     ❌     |
  |British Indian Ocean Territory| 246|    ❌     |
  |      Seychelles        |   248     |     ❌     |
  |        Sudan           |   249     |     ❌     |
  |       Rwanda           |   250     |     ❌     |
  |      Ethiopia          |   251     |     ❌     |
  |       Somalia          |   252     |     ❌     |
  |      Djibouti          |   253     |     ❌     |
  |        Kenya           |   254     |     ❌     |
  |      Tanzania          |   255     |     ❌     |
  |       Uganda           |   256     |     ❌     |
  |       Burundi          |   257     |     ❌     |
  |     Mozambique         |   258     |     ❌     |
  |       Zambia           |   260     |     ❌     |
  |     Madagascar         |   261     |     ❌     |
  |       Mayotte          |   262     |     ❌     |
  |       Reunion          |   262     |     ❌     |
  |      Zimbabwe          |   263     |     ❌     |
  |       Namibia          |   264     |     ❌     |
  |       Malawi           |   265     |     ❌     |
  |       Lesotho          |   266     |     ❌     |
  |      Botswana          |   267     |     ❌     |
  |      Swaziland         |   268     |     ❌     |
  |       Comoros          |   269     |     ❌     |
  |    Saint Helena        |   290     |     ❌     |
  |       Eritrea          |   291     |     ❌     |
  |        Aruba           |   297     |     ❌     |
  |   Faroe Islands        |   298     |     ❌     |
  |      Greenland         |   299     |     ❌     |
  |      Gibraltar         |   350     |     ❌     |
  |      Portugal          |   351     |     ❌     |
  |     Luxembourg         |   352     |     ❌     |
  |       Ireland          |   353     |     ❌     |
  |      Iceland           |   354     |     ❌     |
  |      Albania           |   355     |     ❌     |
  |       Malta            |   356     |     ❌     |
  |       Cyprus           |   357     |     ❌     |
  |      Finland           |   358     |     ❌     |
  |      Bulgaria          |   359     |     ❌     |
  |     Lithuania          |   370     |     ❌     |
  |       Latvia           |   371     |     ❌     |
  |      Estonia           |   372     |     ❌     |
  |      Moldova           |   373     |     ❌     |
  |      Armenia           |   374     |     ❌     |
  |      Belarus           |   375     |     ❌     |
  |       Andorra          |   376     |     ❌     |
  |       Monaco           |   377     |     ❌     |
  |     San Marino         |   378     |     ❌     |
  |       Vatican          |   379     |     ❌     |
  |      Ukraine           |   380     |     ❌     |
  |       Serbia           |   381     |     ❌     |
  |     Montenegro         |   382     |     ❌     |
  |       Kosovo           |   383     |     ❌     |
  |      Croatia           |   385     |     ❌     |
  |      Slovenia          |   386     |     ❌     |
  | Bosnia and Herzegovina |   387     |     ❌     |
  |     Macedonia          |   389     |     ❌     |
  |  Czech Republic        |   420     |     ❌     |
  |     Slovakia           |   421     |     ❌     |
  |   Liechtenstein        |   423     |     ❌     |
  |  Falkland Islands      |   500     |     ❌     |
  |       Belize           |   501     |     ❌     |
  |     Guatemala          |   502     |     ❌     |
  |    El Salvador         |   503     |     ❌     |
  |      Honduras          |   504     |     ❌     |
  |     Nicaragua          |   505     |     ❌     |
  |     Costa Rica         |   506     |     ❌     |
  |       Panama           |   507     |     ❌     |
  |Saint Pierre and Miquelon|  508     |     ❌     |
  |       Haiti            |   509     |     ❌     |
  |   Saint Barthelemy     |   590     |     ❌     |
  |    Saint Martin        |   590     |     ❌     |
  |       Bolivia          |   591     |     ❌     |
  |       Guyana           |   592     |     ❌     |
  |       Ecuador          |   593     |     ❌     |
  |      Paraguay          |   595     |     ❌     |
  |      Suriname          |   597     |     ❌     |
  |      Uruguay           |   598     |     ❌     |
  |       Curacao          |   599     |     ❌     |
  |Netherlands Antilles    |   599     |     ❌     |
  |     East Timor         |   670     |     ❌     |
  |     Antarctica         |   672     |     ❌     |
  |       Brunei           |   673     |     ❌     |
  |       Nauru            |   674     |     ❌     |
  | Papua New Guinea       |   675     |     ❌     |
  |       Tonga            |   676     |     ❌     |
  |  Solomon Islands       |   677     |     ❌     |
  |      Vanuatu           |   678     |     ❌     |
  |        Fiji            |   679     |     ❌     |
  |       Palau            |   680     |     ❌     |
  | Wallis and Futuna      |   681     |     ❌     |
  |    Cook Islands        |   682     |     ❌     |
  |        Niue            |   683     |     ❌     |
  |       Samoa            |   685     |     ❌     |
  |      Kiribati          |   686     |     ❌     |
  |  New Caledonia         |   687     |     ❌     |
  |       Tuvalu           |   688     |     ❌     |
  |  French Polynesia      |   689     |     ❌     |
  |      Tokelau           |   690     |     ❌     |
  |     Micronesia         |   691     |     ❌     |
  |  Marshall Islands      |   692     |     ❌     |
  |    North Korea         |   850     |     ❌     |
  |     Hong Kong          |   852     |     ❌     |
  |       Macau            |   853     |     ❌     |
  |      Cambodia          |   855     |     ❌     |
  |        Laos            |   856     |     ❌     |
  |     Bangladesh         |   880     |     ❌     |
  |       Taiwan           |   886     |     ❌     |
  |      Maldives          |   960     |     ❌     |
  |      Lebanon           |   961     |     ❌     |
  |       Jordan           |   962     |     ❌     |
  |        Syria           |   963     |     ❌     |
  |        Iraq            |   964     |     ❌     |
  |       Kuwait           |   965     |     ❌     |
  |    Saudi Arabia        |   966     |     ❌     |
  |       Yemen            |   967     |     ❌     |
  |        Oman            |   968     |     ❌     |
  |     Palestine          |   970     |     ❌     |
  |United Arab Emirates    |   971     |     ❌     |
  |       Israel           |   972     |     ❌     |
  |      Bahrain           |   973     |     ❌     |
  |       Qatar            |   974     |     ❌     |
  |       Bhutan           |   975     |     ❌     |
  |      Mongolia          |   976     |     ❌     |
  |       Nepal            |   977     |     ❌     |
  |    Tajikistan          |   992     |     ❌     |
  |  Turkmenistan          |   993     |     ❌     |
  |    Azerbaijan          |   994     |     ❌     |
  |      Georgia           |   995     |     ❌     |
  |    Kyrgyzstan          |   996     |     ❌     |
  |    Uzbekistan          |   998     |     ❌     |
  |      Bahamas           |  1-242    |     ❌     |
  |      Barbados          |  1-246    |     ❌     |
  |      Anguilla          |  1-264    |     ❌     |
  |Antigua and Barbuda     |  1-268    |     ❌     |
  |British Virgin Islands  |  1-284    |     ❌     |
  | U.S. Virgin Islands    |  1-340    |     ❌     |
  |  Cayman Islands        |  1-345    |     ❌     |
  |      Bermuda           |  1-441    |     ❌     |
  |      Grenada           |  1-473    |     ❌     |
  |Turks and Caicos Islands|  1-649    |     ❌     |
  |     Montserrat         |  1-664    |     ❌     |
  |Northern Mariana Islands|  1-670    |     ❌     |
  |        Guam            |  1-671    |     ❌     |
  |  American Samoa        |  1-684    |     ❌     |
  |    Sint Maarten        |  1-721    |     ❌     |
  |    Saint Lucia         |  1-758    |     ❌     |
  |     Dominica           |  1-767    |     ❌     |
  |Saint Vincent and the Grenadines|1-784| ❌     |
  |    Puerto Rico         |1-787, 1-939|    ❌     |
  |Dominican Republic      |1-809, 1-829, 1-849|❌  |
  | Trinidad and Tobago    |  1-868    |     ❌     |
  |Saint Kitts and Nevis   |  1-869    |     ❌     |
  |      Jamaica           |  1-876    |     ❌     |
  |      Guernsey          |44-1481    |     ❌     |
  |        Jersey          |44-1534    |     ❌     |
  |     Isle of Man        |44-1624    |     ❌     |
</details>


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