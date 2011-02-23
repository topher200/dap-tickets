gmail_to_db.py
Script for retrieving gmail messages and saving them to disk.

Will eventually be used to push the messages to a database using POST.

= Requirements = 
config file gmail_to_db.cfg in this dir with the following elements:
  - last_id_processed: int for the id of the last successful email that was
      downloaded and saved
  - gmail_username
  - gmail_encrypted_password: password, encrypted with base64.b64encode(1)

= Usage =
  Just run the script with python:
    python gmail_to_db.py

= Algorithm =
  - Creates a lck directory to ensure only one of this script runs at a time
  - Retrieves the ID of every email on the gmail server
  - For each ID after the last successful email processed:
    - Retrieves all the data (message headers, body, and attachments)
      associated with the message
    - Makes sure the email is from PhonePeople and contains a .wav attachment
      - Skips to the next one if not
    - Parses the relevent information from message body
    - Saves the .wav attachment to disk
    - Updates the last_id in the config file
  - Releases the lck directory
