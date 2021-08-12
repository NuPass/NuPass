# NuPass 
> Readable, typable password generator script. Because your users can't deal with [pwmake](http://linux.die.net/man/1/pwmake).

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][pypi-downloads]][pypi-url]
[![Release Status][release-status]][pypi-url]

NuPass provides the `nupass` package and a command-line script for generating temporary 
passwords that your users can read and type. Passwords are provided by the `gen_pass()` 
function and are in the following format:

{number}{Capitalized_word}{special_character}{Capitalized_word}{number}

For example, `4Toffee@Buttercream7`.

## Installation

OS X & Linux:

```sh
pip install nupass
```

Windows:

```sh
python -m pip install nupass
```

## Usage example

Generate a single password:
```bash
$ nupass
```

Generate five passwords:
```bash
$ nupass 5
```

## Development setup

Using NuPass in your projects:
```python
import nupass
temp_pass = nupass.gen_pass() # returns a string containing your password
```

If you want to change the length of the words used in the password, you can set the parameters of `gen_pass()`.
```python
import nupass
temp_pass = nupass.gen_pass(min_w_len=4, max_w_len=10)
# functionally the same as nupass.genpass(4, 10)
```

## Release History
* 1.0.0
    * ADD: Include README as long description on PyPI.
    * CHANGE: Use native setuptools method for script installation.
* 0.2.1
    * ADD: Word length now set by function parameters.
    * CHANGE: Fixed an issue where the wordlist wasn't being closed.
    * CHANGE: Fixed an issue with invalid command-line arguments.
* 0.2.0
    * CHANGE: Converted to package
    * ADD: Script added to path when installed via `setup.py`
* 0.1.0
    * The first proper release

## Meta

Sean Callaway – [@smcallaway](https://twitter.com/smcallaway) – seancallaway@gmail.com

Distributed under the GNU GPL v2 license. See ``LICENSE`` for more information.

[https://github.com/NuPass/NuPass](https://github.com/nupass/nupass)

## Contributing

1. Fork it (<https://github.com/NuPass/NuPass/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[pypi-image]: https://img.shields.io/pypi/v/nupass.svg
[pypi-url]: https://pypi.python.org/pypi/nupass
[travis-image]: https://api.travis-ci.org/NuPass/NuPass.svg?branch=master
[travis-url]: https://travis-ci.org/NuPass/NuPass
[pypi-downloads]: https://img.shields.io/pypi/dm/nupass.svg
[release-status]: https://img.shields.io/pypi/status/nupass.svg
[wiki]: https://github.com/NuPass/NuPass/wiki
