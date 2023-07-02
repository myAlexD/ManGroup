# Random Number Generator

This is a Python project that implements a weighted random number generator. The random numbers and their corresponding probabilities are customizable.

## Prerequisites

This project requires Python 3.6+ and the numpy library.

## Installation

1. Clone this repository to your local machine.

    \`\`\`sh
    git clone https://github.com/myAlexD/random-number-generator.git
    cd random-number-generator
    \`\`\`

2. (Optional) Create and activate a virtual environment.

    \`\`\`sh
    python3 -m venv venv
    source venv/bin/activate
    \`\`\`

3. Install the necessary packages.

    \`\`\`sh
    pip install -r requirements.txt
    \`\`\`

## Usage

The main class in this project is `RandomGen`, which is defined in `src/random_gen/random_gen.py`. Here is an example of how to use it:

\`\`\`python
from src.random_gen.random_gen import RandomGen

random_numbers = [-1, 0, 1, 2, 3]
probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

rng = RandomGen(random_numbers, probabilities)

# Generate a random number
print(rng.next_num())
\`\`\`

This will print a random number chosen from `random_numbers`, with the probability of each number determined by `probabilities`.

## Running Tests

This project includes a suite of tests that you can run to check the functionality of the `RandomGen` class. To run these tests, navigate to the root directory of the project and run:

\`\`\`sh
python -m unittest discover tests
\`\`\`

## Contributing

If you're interested in contributing to this project, please feel free to open a pull request. If you have any questions or run into any issues, don't hesitate to open an issue.

## License

This project is licensed under the terms of the MIT license.

## Contact

If you have any questions about this project, please feel free to reach out to me at <alexander.dimitrov123@gmail.com>.
