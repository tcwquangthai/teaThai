from hypixelapi import HypixelAPI, HypixelError, PlayerNotFoundError
import re

# Run /api on Hypixel to get your API token
api = HypixelAPI("your-token-here")


# Get all profiles by player UUID
# IMPORTANT: This uses (number of profiles a user has) + 1 API requests
profile_dict = api.get_all_skyblock_profiles("7b892af879f64e12a3ed6a895415212a")


# Find highest of a certain collection a player has across all profiles (IF PLAYER HAS ENABLED IT)
wheat_collection = 0

# Create regex to match the wheat collection
regex = re.compile('WHEAT.*')
for key, value in profile_dict.items():
    if "unlocked_coll_tiers" in value:
        for coll in value['unlocked_coll_tiers']:
            if re.match(regex, coll):
                # Retrieve the collection number
                number = int(coll.split('_')[1])
                if number > wheat_collection:
                    wheat_collection = number
print(wheat_collection) # 9


# Get total number of deaths across all profiles
total_deaths = 0
for key, value in profile_dict.items():
        total_deaths += value['stats']['deaths']
print(total_deaths)
