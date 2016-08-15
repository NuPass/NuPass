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

The script includes four user-configurable options: minimum word length, maximum word length, word list, and special 
character list. If the included word list is not comprehensive enough for you, you can change it to 
`/usr/share/dict/words`, which is the full word list on a Linux system.

```python
FILE_NAME = "wordlist.txt"
SPEC_CHARS = ['@', '#', '$', '%', '*', '-', "_"]
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 8
```

More (or fewer) special characters can be added to the list and the values of `MAX_WORD_LENGTH` and `MIN_WORD_LENGTH` can be 
adjusted to values to suit your needs.
