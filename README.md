# Student structure to dictionary

This Python exercise converts a structured student record into a dictionary, then displays its fields.

## How it works

`Student` is a standard-library dataclass with `name`, `roll`, and `marks` fields. `student_to_dict()` calls `dataclasses.asdict()` to convert that record to a separate dictionary. The sample grades and roll number are fictional.

## Run

Requires Python 3.7 or newer; no external packages.

```sh
python dictionary.py
python -m unittest -v
```

Example output:

```text
Student Details:
Name  : Example Student
Roll  : 10
Marks : 90.99
```

The tests verify field conversion and that editing the returned dictionary does not change the original record.

## Project history

The original shared coursework stored a dictionary directly. The October 2026 update adds actual dataclass-to-dictionary conversion and tests with AI assistance. Original Git history and the Colab reference in the source are preserved.

## License

No license has been specified for this project.
