# PWGen
Readable, typable password generator script. Because your users can't deal with [pwmake](http://linux.die.net/man/1/pwmake).

## Usage

Generate a single password:
```bash
$ ./pwgen.py
```

Generate five passwords:
```bash
$ ./pwgen.py 5
```
## Configuration

The script includes three user-configurable options: minimum word length, maximum word length, and special character list. 
Technically, there are four, if you need to point to a word list somewhere other than `/usr/share/dict/words`.

```python
spec_chars = ['@', '#', '$', '%', '*', '-', "_"]
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 8
```

More (or fewer) special characters can be added to the list and the values of `MAX_WORD_LENGTH` and `MIN_WORD_LENGTH` can be 
adjusted to values to suit your needs.