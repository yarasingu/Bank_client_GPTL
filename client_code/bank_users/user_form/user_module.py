import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


# this is the method for user_id generate ----> start hear

def generate_user_id():
    full_table = app_tables.user_profile.search()
    if full_table:
        highest_coustmer_id = find_highest_amigos_id()
        return highest_coustmer_id + 1
    else:
        return 1000

def find_highest_amigos_id():
    table_data = app_tables.user_profile.search()
    highest_id = 999
    for row in table_data:
        coustmer_id = row['coustmer_id']
        if coustmer_id > highest_id:
            highest_id = coustmer_id
    return highest_id

# It creates the ID for only new users
def add_email_and_user_id(email_id):
    generated_id = generate_user_id()
    app_tables.user_profile.add_row(email_user=email_id, coustmer_id=generated_id,registration_approve=False,profile_status=False,mobile_check=False,last_confirm=False)

#----- end hear ----- #

# The method check for new user or existing user using email from current user ---> start hear
def check_user_profile(email_id):
    user_check = app_tables.user_profile.search(email_user=email_id)
    if user_check:
      for user in user_check:
        if user['email_user'] == email_id:
          return True
    else:
        return False

# ---> end hear ----#

# -- this method is used to split the name --->start hear --->

def get_name(email):
  parts = email.split("@")
  if len(parts) == 2:
    split_name = parts[0]
    return split_name

#----end hear --->

# -- this method is used to find the user id based on current email --> start hear -->
def find_user_id(email):
  user_true = app_tables.user_profile.search(email_user=email)
  if user_true:
    coustmer_id = user_true[0]['coustmer_id']
    return coustmer_id
  else:
    return 0000000000

# --- end hear -->


def last_check_status(user_id):
  return False

def registration_engine():
  pass


# def check_user_registration_form_done_or_not_engine(email):
#   userId = find_user_id(email)
#   user_talble = app_tables.user_profile.get_by_id(userId)
#   print(user_talble)
#   if user_talble == None:
#     print("else statement was executed ")
#     return False
#   else:
#     check_one = user_talble['last_confirm']
#     print("check one form last check  ", check_one)
#     return check_one
  

def check_user_registration_form_done_or_not_engine(email):
  userId = find_user_id(email)
  print(userId)
  user_talble = app_tables.user_profile.get(coustmer_id=userId)
  print(user_talble)
  if user_talble == None:
    print("if statement was executed ")
    return False
  else:
    check_one = user_talble['last_confirm']
    print("else statement was executed ")
    return check_one