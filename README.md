# Zorua162's Advent of code 2024

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

## Plan

Get as far in AOC 2024 as I can, to learn how much I have improved during the year.

## Template

```bash
template/
├── data.txt
├── dayx_solution.py
├── part1_example_data.txt
├── part2_example_data.txt
└── test_dayx.py
```

### Day generation

Things that are updated in each template:

- Copy template folder
- Rename it to the current day name (for example dayx)
- Rename the solution file, so `dayx_solution.py` -> `day1_solution.py`
- Rename the test file, so `test_dayx.py` -> `test_day1.py`
- Update the import path in the test file
- Update the `current_day` variable in both files to be the name of the current folder

### Template automation

These steps are automated by the script `generate_new_day.py`, which is run by giving
it the day number which is wished to be generated

## Pipelines

I'm planning to add a GitHub actions pipeline in the future, which will provide future
validation that my unit tests continue to work.

## Code standards

Pre-commit has been setup for this repo, which provides the standards that should be
followed. These standards are all automated, so as long as valid Python code is
submitted then commiting once with errors should automatically resolve themselves.

### Setup pre-commit

To setup the pre-commits, first install pre-commit via the `requirements-dev.txt` file:
`python -m pip install -r requirements-dev.txt`

Now setup the pre-commits in your local environment:
`pre-commit install`

Lastly, it is often useful to let pre-commit catch any files that it may have missed,
run: `pre-commit run --all`, then pre-commit will only run on changed files when they
are commited.

### Pre-commits used

- black: Automatically ensures that flake-8 is followed with a standardized style

- end of file fixer: Automatically ensures that every file has a new line at the end of
 it

- trailing whitespace: Remove whitespace

### Pre-commit automation

Pre-commit.ci automatically runs these checks as an action on Github

## Notes on improvements


### Day 6

Had massive issues with this day, partially as I misunderstood part 2 to mean a loop which has only 4 corners (and not double or many loops).

I used the extra time I had from completing day 11 to re-visit this day, and through
some discussions with a colleague came up with a solution which solved the problem.

However, I am not entirely happy with this solution, as it takes far too long
to get the answer, so it would be nice to re-visit this again in the future to better
understand the more optimized ways of doing this.

### Day 7

Ended up using sub-optimal solution for part2, but optimized it enough that it could
solve the answer in a not unreasonable amount of time.

If I have spare time in the future (I probably won't), then I would like to implement
a more optimal solution.


### Day 9

Also very slow


### Day 10

No improvements needed, although I found getting the initial recursions right tricky I
found that for part 2 I had already coded for the general case, making it very fast

### Day 11

Also no improvements needed, wrote the optimized solution first try!
