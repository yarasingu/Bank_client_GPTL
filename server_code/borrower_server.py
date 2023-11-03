import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



@anvil.server.callable
def add_borrower_step1(full_name,mobile_no,dob,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['full_name'] = full_name
    row[0]['mobile'] = mobile_no
    row[0]['date_of_birth'] = dob
    

@anvil.server.callable
def add_borrower_step2(gender,user_photo,city,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['gender']=gender
    row[0]['user_photo']=user_photo
    row[0]['city']=city


@anvil.server.callable
def add_borrower_step3(aadhar,aadhar_card,pan,pan_card,user_id):
  row=app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['aadhaar_no']=aadhar
    row[0]['aadhaar_photo']=aadhar_card
    row[0]['pan_number']=pan
    row[0]['pan_photo']=pan_card
    