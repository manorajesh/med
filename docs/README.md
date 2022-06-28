# med - <ins>M</ins>ano's <ins>Ed</ins>itor

A Pythonic recreation of a the ubiquitous, line-oriented [GNU ed](https://www.gnu.org/software/ed/) text editor

## Installation
`git clone https://github.com/manorajesh/med.git` <br>
`pip install —r requirements.txt` <br><br>
Additionally, you can add `alias med='path/to/repo/med.py'` to your shell config file, so that you can type `med` as if it were a command.

## Usage
`./med.py [FILE] [—p prompt]`

## Tutorial
`r [FILE] ![COMMAND]` — read and append given file or shell command to end of text buffer <br>
`a (INTEGER)` - append stdin after given line or current line <br>
`i (INTEGER)` — insert stdin before given line or current line <br>
`c (INTEGER)` - change current or given line to stdin and append new lines if given <br>
`p (INTEGER)` — print current or given line to stdout <br>
`,p` - print entire buffer to stdout <br>
`s/old/new/` - replace /*old*/ with /*new*/ on current line <br>
`,s/old/new/` - replace /*old*/ with /*new*/ on entire buffer <br>
`u` - revert to last change (including the last undo) <br>
`d (INTEGER)` - delete current or given line <br>
`w [FILE]` — write text buffer to file (overwriting if it already exists) <br>
`W [FILE]` — append text buffer to file (creating one if it doesn't exists) <br>
`q` — quit (losing any unsaved work) <br>
`P (STRING)` - set prompt to `STRING` or `*` if none given <br>
`y (INTEGER)` - *yank* (copy) current or given line to copy buffer <br>
`x (INTEGER)` - cut (copy and delete) current or given line to copy buffer <br>
`m (INTEGER)` - *mash* (aka paste) copy buffer to given or current line <br>
`h` - print explanation for last error <br>
`!` - a *bang* followed by a shell command will print the command's output to stdout <br>
`wq` - same as executing `w` and `q` successively <br>
`INTEGER` - switch current line to integer <br>
`n (INTEGER)` — print current or given line number and its coinciding line value <br>
`,n` - print entire text buffer with line numbers <br>
`pr` and `,pr` - print the raw text buffer (debug only) <br>

##### Contents of requirements.txt
`click==8.1.3`

<sub>Part of the M-Commands Line</sub>
