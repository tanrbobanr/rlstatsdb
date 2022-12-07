# Install
`pip install rlstatsdb`

# Description
`rlstatsdb` is a simple and easy-to-implement SQLite database manager equipped for storing and fetching Rocket League replay data (as returned from ballchasing.com's API). When fetching data from the database (through the manager) is incredibly easy to navigate, meaning you don't need to memorize the entire dictionary structure of ballchasing's get-replay response.

# Usage
For the below example, `replay_data` is the response dict from `https://ballchasing.com/api/replays/<replay_id>`. In reality, this can be acquired through various means, such as `requests` and `aiohttp`, or through API wrappers such as `pychasing` and `python-ballchasing`. 
```py
import rlstatsdb

# The database file needs to either be non-existant, empty, or a valid
# SQLite database. If the file is non-existant, a new file will be created
sdb = rlstatsdb.Manager("path_to_database_file")

manifest_id = sdb.add(replay_data)
game = sdb.get(manifest_id)

game.replay_id
game.max_rank.division
game.orange.players[0].stats.core.goals
game.blue.color
# etc.
```