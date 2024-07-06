
# AI Help Desk

This project is a template for setting up a Python environment using `pyenv` and `virtualenv` on macOS.

## Description

This project demonstrates how to set up a Python development environment using `pyenv` and `virtualenv`. It includes steps for installing the necessary tools and configuring the environment, making it easier to manage different Python versions and dependencies.

## Installation

Follow these instructions to set up your project.

### Prerequisites

- macOS
- Homebrew
- `pyenv`

### Steps

1. **Install Homebrew**

   If you don't have Homebrew installed, you can install it using the following command:

   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install `pyenv` and `pyenv-virtualenv`**

   Use Homebrew to install `pyenv` and `pyenv-virtualenv`:

   ```sh
   brew update
   brew install pyenv pyenv-virtualenv
   ```

3. **Configure your shell**

   Add the following lines to your `~/.zshrc` (or `~/.bashrc` if you are using bash):

   ```sh
   echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
   ```

   Then, reload your shell configuration:

   ```sh
   source ~/.zshrc
   ```

4. **Install Python 3.10.6**

   Use `pyenv` to install Python 3.10.6:

   ```sh
   pyenv install 3.10.6
   ```

5. **Create and activate a virtual environment**

   Create a virtual environment named `myenv`:

   ```sh
   pyenv virtualenv 3.10.6 myenv
   pyenv activate myenv
   ```

6. **Install dependencies**

   If you have a `requirements.txt` file, you can install dependencies using pip:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the environment, ensure it is activated:

```sh
pyenv activate myenv
```

Run your Python scripts as usual:

```sh
python script.py
```

## Contributing

To contribute to this project, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Homebrew](https://brew.sh/)
- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
