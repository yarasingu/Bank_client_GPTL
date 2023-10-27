import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



email = ""
name =""




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
    app_tables.user_profile.add_row(email_user=email_id, coustmer_id=generated_id)


# The method checks whether the user exists or not
def check_user_profile(email_id):
    user_check = app_tables.user_profile.search(email_user=email_id)
    if user_check:
        return True
    else:
        return False

