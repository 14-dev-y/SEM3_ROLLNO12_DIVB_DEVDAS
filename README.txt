PYTHON FILE HANDLING & EXCEPTIONS — 25 SOLVED PROGRAMS
Reference names used: Dev, Tanish, Dhruv, Maahi, Keya

HOW TO USE
1. Extract this ZIP file.
2. Open any .py file in IDLE, VS Code, or another Python editor.
3. Run it with Python 3.
4. Files created by the programs are saved in the current working directory.

TOPICS COVERED
- Why files are used for permanent data storage
- open() and modes r, w, a, r+
- read(), readline(), readlines()
- write(), writelines(), close(), with
- Student names and marks files
- Syntax errors vs runtime exceptions (see notes below)
- try/except and ValueError, TypeError, ZeroDivisionError,
  FileNotFoundError, IndexError
- Multiple except clauses, else, finally, and raise

IMPORTANT NOTES
- 'w' creates a file or overwrites existing contents.
- 'a' adds content at the end of a file.
- 'r' reads an existing file; it raises FileNotFoundError if missing.
- 'r+' reads and writes an existing file without automatically truncating it.
- with open(...) automatically closes a file when the block ends.
- A syntax error is a problem with Python code structure and is generally
  detected before the program runs. An exception is an error raised while
  the program is executing; try/except can handle many exceptions.
- Programs that use input() ask you to type values while running.
