from hypixelapi import HypixelAPI, HypixelError, PlayerNotFoundError
import re

# Run /api on Hypixel to get your API token
api = HypixelAPI("your-token-here")

# Get a singular skyblock profile by its profile uuid
# This includes all profile members in the JSON, unless you specify the player UUID in
# the second argument
skyblock_profile = api.get_skyblock_profile_by_profileid("16ffee3b157b427192e888f01fd128ce", player_uuid="7b892af879f64e12a3ed6a895415212a")

# Find highest of a certain collection a player has
wheat_collection = 0

# Create regex to match the wheat collection
regex = re.compile('WHEAT.*')
if "unlocked_coll_tiers" in skyblock_profile:
    for coll in skyblock_profile['unlocked_coll_tiers']:
        if re.match(regex, coll):
            # Retrieve the collection number
            number = int(coll.split('_')[1])
            if number > wheat_collection:
                wheat_collection = number
print(wheat_collection) # 9



# Get number of deaths for this singular profile
print(skyblock_profile['stats']['deaths'])


# Get UUIDs of all members of a profile
# NOTE: This time, we don't include the second argument to get all members
skyblock_profile = api.get_skyblock_profile_by_profileid("16ffee3b157b427192e888f01fd128ce")
for key, value in skyblock_profile['profile']['members'].items():
    print(key)
