Getting Started
======================================

Installation
-----------------

To install run:

``pip install hypixelapi``


Usage
-------------------

First, run /api on the Hypixel server to get your own key.

.. code-block:: python
  :linenos:

  from hypixelapi import HypixelAPI
  api = HypixelAPI('your-key-here')
  response = api.get_player_json('uuid')
  print(response)

Some examples are provided on `GitHub <https://github.com/MylesMor/hypixelapi/tree/master/examples>`_.

For detailed documentation of each function see the `API documentation <https://hypixelapi.readthedocs.io/en/latest/api.html/>`_.

For documentation of the official API see `here <https://github.com/HypixelDev/PublicAPI/tree/master/Documentation/methods/>`_.
This will also provide details on the format of the response JSON, or you can print each JSON yourself (I recommend the ``pprint`` module) to see the format.
