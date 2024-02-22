# hypixelapi

[![PyPI version](https://badge.fury.io/py/hypixelapi.svg)](https://badge.fury.io/py/hypixelapi) [![Documentation Status](https://readthedocs.org/projects/hypixelapi/badge/?version=latest)](https://hypixelapi.readthedocs.io/en/latest/?badge=latest) [![CircleCI](https://circleci.com/gh/MylesMor/hypixelapi/tree/master.svg?style=svg)](https://circleci.com/gh/MylesMor/hypixelapi/tree/master)




This is an unofficial Python3 wrapper for the Hypixel API inspired by [Snuggle's hypixel.py](https://github.com/Snuggle/hypixel.py).

Current version: `0.1.4`

## Documentation

Documentation is available here: https://hypixelapi.readthedocs.io/

For the types of JSON received by each command, please reference [this official documentation](https://github.com/HypixelDev/PublicAPI/tree/master/Documentation/methods)],
or print the JSON response to view it yourself.


## Installation

To install run:

``pip install hypixelapi``

## Getting Started

First, run /api on the Hypixel server to get your own key.

```
from hypixelapi import HypixelAPI
api = HypixelAPI('your-key-here')
response = api.get_player_json('uuid')
print(response)
```

For more detailed documentation and available functions, visit:
https://hypixelapi.readthedocs.io/

## Examples

Various examples are available in the [examples folder](https://github.com/MylesMor/hypixelapi/tree/master/examples).

These currently include basic player and some of the Skyblock functions, with more to be added soon.
