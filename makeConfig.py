import pickle
# The bot's Discord Bot token
<<<<<<< HEAD
BOT_TOKEN = 'ODAzNDU4NzQ2NDUzNDU4OTc0.YA-FRA.qdTDgnZnHScNmKTTKZyBMdroEwk'

# The ID of the spreadsheet that contains all of ERPL's current members
SPREADSHEET_ID = '1U9mnzy_PBXcv_LMXtQNfi9LvNrUTx_n9Lz9N1D-BRaA'
=======
BOT_TOKEN = ''

# The ID of the spreadsheet that contains all of ERPL's current members
SPREADSHEET_ID = ''
>>>>>>> ff9e4ae083d539b7e1ff4f0d87db81af52b71c11

# These specify when the member's data in the spreadsheet starts and ends
SHEET_NAME = 'Sheet1!'
RANGE_START = 'A2'
RANGE_END = 'D'

<<<<<<< HEAD
# This is Discord's ID that means the "Member" role
MEMBER_ROLE_ID = 805952653162709053
RECRUIT_ROLE_ID = 805952689452089384
=======
### This is Discord's ID that means the "Member" role
MEMBER_ROLE_ID = 000000000000000000
RECRUIT_ROLE_ID = 000000000000000000
OFFICER_ROLE_ID = 000000000000000000
PROJECT_ROLE_ID = 000000000000000000
BOT_COMMAND_CHANNEL = 000000000000000000
JOIN_CHANNEL = 000000000000000000
>>>>>>> ff9e4ae083d539b7e1ff4f0d87db81af52b71c11

#Use Pickle to write config.bin
with open('config.bin', 'wb') as fh:
    pickle.dump([BOT_TOKEN, SPREADSHEET_ID, SHEET_NAME, RANGE_START, RANGE_END, MEMBER_ROLE_ID, OFFICER_ROLE_ID, PROJECT_ROLE_ID, RECRUIT_ROLE_ID, JOIN_CHANNEL, BOT_COMMAND_CHANNEL], fh)
exit

