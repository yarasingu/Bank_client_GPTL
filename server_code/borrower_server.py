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


@anvil.server.callable
def add_borrower_step4(mother_toung,marital_status,spouse_name,marrege_date,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['mouther_tounge']=mother_toung
    row[0]['marital_status']=marital_status
    row[0]['spouse_name']=spouse_name
    row[0]['Date_mariage']=marrege_date


@anvil.server.callable
def add_borrower_step5(spouse_mobile,spouse_company_name,spouse_company_address,spouse_profficen,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['spouse_mobile']=spouse_mobile
    row[0]['spouse_company_name']=spouse_company_name
    row[0]['spouse_company_address']=spouse_company_address
    row[0]['spouse_profficen']=spouse_profficen

@anvil.server.callable
def add_user_profile(min_amount, tenure,max_amount):
  app_tables.user_profile.add_row(
    min_amount=min_amount,
    tenure=tenure,
    max_amount=max_amount
  
  )

@anvil.server.callable
def calculate_processing_fee(minimum_amount, tenure):
    # Define your processing fee calculation logic here
    processing_fee_percentage = 0.05  # 5% processing fee
    processing_fee = minimum_amount * processing_fee_percentage * tenure
    return processing_fee