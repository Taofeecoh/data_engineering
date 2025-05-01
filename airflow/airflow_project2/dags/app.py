from dotenv import load_dotenv
import utils as ut

load_dotenv()

endpoint = "https://randomuser.me/api"
count = "/?results=20"
gender = "&gender=female"

first_request =ut.send_request(endpoint,(count+gender))
first_json_list = ut.extract_json_inlist(first_request)
first_df = ut.list_to_df(first_json_list)
s3_write = ut.write_s3(first_df)