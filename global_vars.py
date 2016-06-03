# File to house all globally defined values.
# Variable to house users.

# List containing a list of users.
globalUsers = []
userIdToUser = {}

# List containing current active teams per time update (day).
globalTeams = []

# Used for leveling up.
# {"teamID"} = {"hits" : 123, "slices" = 123, "hitsReqPerSlice" : 123, "reqTotalHits" : 123}
teamLevelTracker = {}

# List containing current sessions per time update (day).
yesterday_globalUSessions 	= None
globalUSessions 			= None
hashmapUSessions = {} #userID -> session

# List containing current team assignments per time update (day).
yesterday_globalTeamAssignments = None
globalTeamAssignments 			= None
hasmapTeamAssignments = {}

# Day Duration
dayDuration = None

#collection of adID and categories
adDatabase = None

#collection of buyID and prices
buyDatabase = None

#global counter for generating unique IDs (increment this after every use)
counter = 5000
teamIDCounter = 0
eventIDCounter = 0

# Platform distributions
platforms	= ['iphone', 'android', 'mac', 'windows', 'linux']
freq 		= [0.4, 0.35, 0.05, 0.15, 0.05]

timestamp_format = "%Y-%m-%dT%H:%M:%S"

max_accuracy = 0.7

#FILES ["ad-clicks.log","buy-clicks.log","game-clicks.log","team-assignments.log","users.log", "user-session.log", "level-events.log", "team.log"]:
ad_clicks = None
buy_clicks = None
game_clicks = None
team_assignments = None
users = None
user_session = None
level_events = None
team = None

