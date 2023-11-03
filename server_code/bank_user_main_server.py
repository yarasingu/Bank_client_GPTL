import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
# @anvil.server.callable
# def get_next_user_id(self):
#   highest_user_id = anvil.server.database.query('User', {'user_id': anvil.server.database.ANY_VALUE})
#   highest_user_id = max([user['user_id'] for user in highest_user_id])
#   print("i added a one line")
# #   next_user_id = highest_user_id + 1 if highest_user_id else 1000
#   return next_user_id


