# med - <ins>M</ins>ano's <ins>Ed</ins>itor

A Pythonic recreation of a the ubiquitous, line-oriented [GNU ed](https://www.gnu.org/software/ed/) text editor

## Installation
`git clone https://github.com/manorajesh/med.git` <br>
`pip install —r requirements.txt`

## Usage
`./med.py [FILE] [—p prompt]`

## Tutorial
`r [FILE] ![COMMAND]` — read and append given file or shell command to end of text buffer <br>
`a (INTEGER)` - append stdin after given line or current line <br>
`i (INTEGER)` — insert stdin before given line or current line <br>
`c (INTEGER)` - change current or given line to stdin and append new lines if given <br>
`p (INTEGER)` — print current or given line to stdout <br>
`,p` - print entire buffer to stdout <br>
`s` - replace /*old*/ with /*new*/ on current line <br>
`,s` - replace /*old*/ with /*new*/ on entire buffer <br>
`u` - revert to last change (including the last undo) <br>
`d (INTEGER)` - delete current or given line <br>
`w [FILE]` — write text buffer to file (overwriting if it already exists) <br>
`W [FILE]` — append text buffer to file (creating one if it doesn't exists) <br>
`q` — quit (losing any unsaved work) <br>
`P` - set prompt to `*` <br>
`!` - a *bang* followed by a shell command will print the command's output to stdout <br>
`wq` - same as executing `w` and `q` successively <br>
`INTEGER` - switch current line to integer <br>
`n (INTEGER)` — print current or given line number and its coinciding line value <br>
`,n` - print entire text buffer with line numbers <br>
`pr` and `,pr` - print the raw text buffer (debug only) <br>

##### Contents of requirements.txt
`click==8.1.3`

<sub>Part of the M-Commands Line</sub>
