# Automation-API-Testing

![Static Badge](https://img.shields.io/badge/STATUS-IN%20DEVELOP-GREEN)

The current repository focuses on the automation of API tests provided by Postman collections. It is capable of executing pre-scripts and tests implemented within each API using the Newman tool. The repository is designed to be implemented using Python, specifically with Gherkin (through Behave, a library within Python capable of following the logic of Gherkin).

## Installation

For the installation of the repository and its dependencies, it is recommended to read:

[User manual](https://github.com/Aldo-Fonts/Automation-API-Testing/blob/main/docs/user_manual.md)

## Running Tests

To run tests, run the following command

```bash
  ./start.sh [-option value]
```

| Option      | Description     | Value       | Mandatory                     |
| :---------: | :-------------: | :---------: | :---------------------------: |
| t           | tag             | Title       | :white_check_mark:            |
| f           | file or feature | Text        | :negative_squared_cross_mark: |
