[![Coverage][coverage-shield]][coverage-url]
[![GPL3 License][license-shield]][license-url]

<br />
<p align="center">

  <h1 align="center">AdReg</h1>

  <p align="center">
    Advertisement database system
    <br />
    <a href="https://github.com/Aledosim/adreg"><strong>Explore the docs »</strong></a>
    <br />
    <br />
   <a href="https://github.com/Aledosim/adreg/issues">Report Bug</a>
    ·
    <a href="https://github.com/Aledosim/adreg/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About The Project

This program creates a database of advertisements that accepts the name of the advertisement, the name of the client, the
start and the end dates and the investment per day in BRL. You can create reports on each entry filtered by client and period of time.

### Built With

* [Peewee](http://docs.peewee-orm.com/en/latest/)
* [SQLite](https://sqlite.org/index.html)
* [Schema](https://github.com/keleshev/schema)
* [python-tabulate](https://github.com/astanin/python-tabulate)
* [pytest](https://docs.pytest.org/en/6.2.x/)

## Getting Started

### Prerequisites

You will need [pip](https://pip.pypa.io/en/stable/installing/) to install the packages. It's **strongly recommended** that you use a [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments). Developed in Python 3.7.3.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Aledosim/adreg.git
   ```
2. Enter the directory
   ```sh
   cd adreg
   ```
3. Install the packages **after activate the virtual environment**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the adreg shell  script that lives in the root directory. **You can't run it out of this location** (it's in beta version yet). It will create the database file in root folder as well.

### Add entry
At the root directory:
```sh
./adreg add -n NAME -c CLIENT -s START -e END -i INVESTMENT
```
Being that:

 - NAME: the name of the advertisement
 - CLIENT: the client name
 - START: the starting date in the format dd-mm-yyyy
 - END: the ending date in the format dd-mm-yyy
 - INVESTMENT: the investment per day
 
 The START parameter defaults to the current day, you can omit it.

### Visualizing reports
You can visualize the reports with
```sh
./adreg report
```
To filter the results, use the optional parameters
```sh
./adreg report -c CLIENT -s START -e END
```
Being that:
- CLIENT: the client name
- START: starting date in the format dd-mm-yyyy
- END: ending date in the format dd-mm-yyy
On this command, END defaults to the current day and his value can be omitted.

### Getting help
You can add the -h flag on the commands to see the informations.

### Testing
To run the tests execute on the root directory:
```sh
pytest
```

## License

Distributed under the GPL3 License. See `LICENSE` for more information.

## Contact

Alexandre do Sim - [LinkedIn](https://www.linkedin.com/in/alexandre-do-sim/) - aledosim@yahoo.com.br

Checkout my git projects: [https://github.com/Aledosim](https://github.com/Aledosim)


## Acknowledgements
This application is part of Capgemini Brasil's trainee selection program.

### Future tasks
- Implement config module (not fully done)
- Make list and delete functionalities
- Prettier output


[license-shield]: https://img.shields.io/badge/license-GPL3-green
[license-url]: https://raw.githubusercontent.com/Aledosim/adreg/master/LICENSE
[coverage-shield]: https://raw.githubusercontent.com/Aledosim/adreg/master/.github/coverage.svg
[coverage-url]: https://raw.githubusercontent.com/Aledosim/adreg/master/.github/coverage.txt
