# Regular Expressions

Regular Expression or RE, mathematically, can be defined as a set strings accepted by a finite automaton.

Regular Expressions, also `regex` or `regexp`, has been widely adopted into modern computing to find matches of a substring or a pattern from a main string, it is also used for lexical analysis. Most modern languages support a common syntax, but with minor differences.

## Flags
> `regex`*es* are usually enclosed in between slashes, such as `/regex/`, one or more flags can be specifed at the end to manipulate its overall behavior.

|   |   |
|---|---|
| g | **g**lobal search, allows iterative searches   |
| i | case **i**nsensitive                           |
| m | **m**ulti-line, anchors searches on every line |

**NOTE:**
 1. If `g` is unspecified, it will return the first occurrence if matched.
 2. Ommitting `i` means all characters or classes are literraly in exact casing.
 3. Other flags are available, but may not be universally supported.


## Anchors
> When searching for patterns, it can be specified in the `regex` whether to search through the whole string or anchors from the first and/or the last character of the string.

|   |   |
|---|---|
| x  | all `x`s            |
| ^  | start of the string |
| $  | end of the string   |
| \b | word boundary, not specifically the beginning of a string      |
| \B | not-word boundary, not specifically the beginning of a string  |


## Character Classes
> Instead of specifying each character, `regex`*es* can be simplified using character classes.

|   |   |
|---|---|
| .      | any character except newline             |
| \w     | a single character in `a-z`, `A-Z`, `0-9`, and `_` |
| \d     | a single digit, `0-9`                    |
| \s     | a whitespace, see `\t`, `\r`, `\n`, `\f` |
| \W     | not a character                          |
| \D     | non-digit character                      |
| \S     | non-whitespace character                 |


## Escaped Characters
> In programming there are reserved words (or symbols) that has certain meanings or will perform certain operations.

|   |   |
|---|---|
| \\.  | escaped period    |
| \\*  | escaped asterisk  |
| \\\\ | escaped backslash |
| \t   | tab               |
| \r   | carriage return   |
| \n   | new line          |

**NOTE:**
 1. `\n` simulates mechanical roller up, line feed or new line in files.
 1. `\r` simulates carriage return (cursor to the left) in CLI, means end-of-line in older OSs.
 2. `\r\n` simulates mechanical carriage return then roller up (in that sequence)

## Capture Group
> Grouping and nesting sub-`regex`*es* allows more complex pattern matching and may even shorten `regex`*es*.

|   |   |
|---|---|
| ()    | capture group              |
| (\n)  | Back reference to group #n |

**NOTE:** Groups must exist before referencing, otherwise may treated as an escaped character.

## Lookahead and Look Behind
> Provide additional logic whether a sub-pattern must exist (or not) before the previous sub-`regex`.

|   |   |
|---|---|
| (?:x)  | treats `x` a literal character and not a capture group      |
| (?=x)  | positive lookahead, finds a match before the `x`            |
| (?!x)  | negative lookahead, finds a match where `x` is not after it |
| (?<=x) | positive look behind, finds a match where `x` is before the next sub-`regex` |

## Bracket Expressions
> The characters insides the brackets must find at most one match.

|   |   |
|---|---|
| [abc]  | any a, b, or c                |
| [a-z]  | any character from `a` to `z` |
| [e-u]  | any character from `e` to `u` |
| [^abc] | negation, not a, b, or c      |

## Quantifiers & Alternation

|   |   |
|---|---|
| x*     | 0 or more x       |
| x+     | 1 or more x       |
| x?     | x or nothing      |
| x{n}   | exactly n         |
| x{n,}  | exactly x or more |
| x{n,m} | between n & m     |
| x\|y   | match x or y      |

**NOTE:**
 1. Greedy match: The quantifiers `*`, `+`, and `{}` expands searches as far the pattern can.
 2. Lazy match: The `?` only captures until the first match if found.