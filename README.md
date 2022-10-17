# connect-four

Classic Connect Four in Python. Developed for Software Engineering SS22 @ TH Deggendorf.

## Getting Started

### For Users

[Docker](https://www.docker.com/get-started/) is required.

To launch the app in a Docker container, run the following:

```bash
cd connect-four
docker-compose build
docker-compose run --rm connect-four
```

### For Developers

[Pipenv](https://pipenv.pypa.io/en/latest/) is required for testing.

To run tests:

```bash
# Run unit tests
pipenv run pytest

# Run e2e tests
pipenv run behave
```
