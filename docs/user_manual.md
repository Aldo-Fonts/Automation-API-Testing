# Automation API testing

The current repository focuses on the automation of API tests provided by Postman collections. It is capable of executing pre-scripts and tests implemented within each API using the Newman tool. The repository is designed to be implemented using Python, specifically with Gherkin (through Behave, a library within Python capable of following the logic of Gherkin).

## System requirements

Newman is the command-line collection runner for Postman, and its system requirements are typically aligned with the requirements for running Postman collections. Here are the general system requirements for Newman:

* **Node.js**:
Newman is built on Node.js. Ensure that Node.js is installed on your system.
Minimum version: Node.js 10 or later.

* **Operating System**:
Newman is designed to work on various operating systems, including Windows, macOS, and Linux.

* **Memory**:
The memory requirements are similar to those of Postman. A minimum of 4 GB RAM is recommended.

* **Processor**:
Newman's processor requirements are not explicitly specified but typically align with standard system requirements for running Node.js applications.

## Installation

As a first step, it is necessary to have the current repository:

```bash
  git clone -b development https://github.com/Aldo-Fonts/Automation-API-Testing.git
```


Once the repository is installed, you need to navigate to the config folder of the repository:

```bash
  cd YOUR_PATH/Automation-API-Testing/config
```

Subsequently, the following command will install the necessary tools for the execution of automated tests:

```bash
  ./basic_setup.sh
```

If the above command returns permission denied: ./basic_setup.sh, it is necessary to change the permissions for the file:

```bash
  chmod +x basic_setup.sh
```

And try running the configuration shell again.

This command will install the following dependencies:

* Node
* npm 10.2.4
* newman
* newman - reporter html
* Python 3.11
* Python - behave
* Python - tkinter
* Python - requests

## Running Tests

To verify the functionality of all dependencies, execute the following command, which will send a simple request based on the example collections.

```bash
  ./demo.sh
```

This command will run a test script to check the proper functioning of the installed dependencies using example collections.

To run tests, run the following command

```bash
  ./start.sh
```
