NO_COLOR=\x1b[0m
OK_COLOR=\x1b[32;01m
ERROR_COLOR=\x1b[31;01m
INFO_COLOR=\x1b[96;01m
WARN_COLOR=\x1b[33;01m

all: check

qa: format check
	@echo "$(OK_COLOR)QA checks completed!$(NO_COLOR)"

check:
	@echo "$(INFO_COLOR)==> Testing...$(NO_COLOR)"
	poetry run python -m py.test --quiet

format:
	@echo "$(INFO_COLOR)==> Formatting...$(NO_COLOR)"
	poetry run black .

doctor:
	@echo "$(INFO_COLOR)==> Checking maintainability...$(NO_COLOR)"
	poetry run radon cc src
	poetry run radon cc tests

	@echo "$(INFO_COLOR)==> Checking for dead code...$(NO_COLOR)"
	poetry run vulture src tests

	@echo "$(INFO_COLOR)==> Checking for security vulnerabilities...$(NO_COLOR)"
	poetry run bandit --quiet -r src
