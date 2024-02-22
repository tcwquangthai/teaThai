from hypixelapi import HypixelAPI, HypixelError, PlayerNotFoundError

# Run /api on Hypixel to get your API token
api = HypixelAPI("your-token-here")


# Basic collated stats, including current rank and name.
basic_player_dict = api.get_player_info("7b892af879f64e12a3ed6a895415212a")

rank = basic_player_dict['rank']['current_rank']
name = basic_player_dict['displayname']
print(rank, name)

# Full player JSON, please see documentation for specific keys
full_player_dict = api.get_player_json("7b892af879f64e12a3ed6a895415212a")

# Check for achievement using the full JSON
if "general_first_friend" in full_player_dict['player']['achievementsOneTime']:
    print(True)

# Get Skywars wins
player = full_player_dict['player']
if "stats" in player:
    if "SkyWars" in player['stats']:
        if "wins" in player['stats']['SkyWars']:
            print(player['stats']['SkyWars']['wins'])
