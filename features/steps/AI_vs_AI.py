from behave import given, when, then
import pexpect
import os

@given('Start the programm')
def start_game(context):
    try:
        image_name = os.environ["connect-four"]
    except KeyError:
        image_name = "connect-four:latest"
    context.proc = pexpect.spawn(f"docker-compose run -i --rm {image_name}")

@given('New game starts')
def start_new_game(context):
    context.proc.sendline("0")

@when('The game mode 3 is chosen')
def test_choose_game_mode(context):
    context.proc.sendline("3")

@when('for Computer 1 is chosen level of difficulty {level}')
def choose_difficulty(context, level):
    context.proc.sendline(level)

@when('for Computer 2 is chosen level of difficulty {level}')
def choose_difficulty(context, level):
    context.proc.sendline(level)

@when('Computer {number} chooses column {column}')
def playing(context, number, column):
    context.proc.sendline(column)

@then('Computer {number} wins')
def winner(context, number):
    context.proc.sendline(f"Player {number} wins")
    