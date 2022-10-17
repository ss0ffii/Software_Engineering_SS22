from behave import given, when, then
import pexpect
import os


@given("Player 1 starts the game")
def step_impl(context):
    try:
        image_name = os.environ["CONNECT-FOUR_CONTAINER_IMAGE"]
    except KeyError:
        image_name = "connect-four:latest"
    context.proc = pexpect.spawn(f"docker-compose run --rm connect-four")


@when("Player 1 is prompted to enter their choice")
def step_impl(context):
    context.proc.expect("Welcome to Connect Four!")


@when("Player 1 chooses a new game ({option})")
def step_impl(context, option):
    context.proc.expect_exact("Enter your choice [0-1]: ")
    context.proc.sendline(option)


@when("Player 1 chooses to play against another player ({option})")
def step_impl(context, option):
    context.proc.expect_exact("Enter your choice [1-3]: ")
    context.proc.sendline(option)


@when("Player 1 chooses ({option})")
def step_impl(context, option):
    context.proc.expect_exact(f"Player 1, choose X or O: ")
    context.proc.sendline(option)


@when("Player 1 places their piece in column ({column})")
def step_impl(context, column):
    context.proc.expect_exact("Player 1, enter your move [1-7]: ")
    context.proc.sendline(column)


@when("Player 2 places their piece in column ({column})")
def step_impl(context, column):
    context.proc.expect_exact("Player 2, enter your move [1-7]: ")
    context.proc.sendline(column)


@when("Player 1 types ({option})")
def step_impl(context, option):
    context.proc.expect_exact("Player 1, enter your move [1-7]: ")
    context.proc.sendline(option)


@then("The current progress is saved")
def step_impl(context):
    context.proc.expect_exact(f"File saved.")
