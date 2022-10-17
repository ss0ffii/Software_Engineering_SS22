from behave import given, when, then
import pexpect
import os

@given('The game starts')
def start_game(context):
    try:
        image_name = os.environ["connect-four"]
    except KeyError:
        image_name = "connect-four:latest"
    context.proc = pexpect.spawn(f"docker-compose run -i --rm {image_name}")

@given('New game is started')
def start_new_game(context):
    context.proc.sendline("0")

@when('The game mode 2 is chosen')
def test_choose_game_mode(context):
    context.proc.sendline("2")

@when('player chooses a piece {piece}')
def setup_players(context, piece):
    context.proc.sendline(piece)

@when('Player {number} chooses column {column}')
def playing(context, number, column):
    context.proc.sendline(column)

@then('Player {number} wins')
def winner(context, number):
    context.proc.sendline(f"Player {number} wins")
    