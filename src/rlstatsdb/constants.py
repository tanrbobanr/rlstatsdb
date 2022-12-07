"""Constants used primarily by ``models``.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

colnames_players = [
    "id",
    "manifest_id",
    "team",
    "start_time",
    "end_time",
    "name",
    "car_id",
    "car_name",
    "steering_sensitivity",
    "id__platform",
    "id__id",
    "rank__id",
    "rank__tier",
    "rank__division",
    "rank__name",
    "camera__fov",
    "camera__height",
    "camera__pitch",
    "camera__distance",
    "camera__stiffness",
    "camera__swivel_speed",
    "camera__transition_speed",
    "stats__core__shots",
    "stats__core__shots_against",
    "stats__core__goals",
    "stats__core__goals_against",
    "stats__core__saves",
    "stats__core__assists",
    "stats__core__score",
    "stats__core__mvp",
    "stats__core__shooting_percentage",
    "stats__boost__bpm",
    "stats__boost__bcpm",
    "stats__boost__avg_amount",
    "stats__boost__amount_collected",
    "stats__boost__amount_stolen",
    "stats__boost__amount_collected_big",
    "stats__boost__amount_stolen_big",
    "stats__boost__amount_collected_small",
    "stats__boost__amount_stolen_small",
    "stats__boost__count_collected_big",
    "stats__boost__count_stolen_big",
    "stats__boost__count_collected_small",
    "stats__boost__count_stolen_small",
    "stats__boost__amount_overfill",
    "stats__boost__amount_overfill_stolen",
    "stats__boost__amount_used_while_supersonic",
    "stats__boost__time_zero_boost",
    "stats__boost__percent_zero_boost",
    "stats__boost__time_full_boost",
    "stats__boost__percent_full_boost",
    "stats__boost__time_boost_0_25",
    "stats__boost__time_boost_25_50",
    "stats__boost__time_boost_50_75",
    "stats__boost__time_boost_75_100",
    "stats__boost__percent_boost_0_25",
    "stats__boost__percent_boost_25_50",
    "stats__boost__percent_boost_50_75",
    "stats__boost__percent_boost_75_100",
    "stats__movement__avg_speed",
    "stats__movement__total_distance",
    "stats__movement__time_supersonic_speed",
    "stats__movement__time_boost_speed",
    "stats__movement__time_slow_speed",
    "stats__movement__time_ground",
    "stats__movement__time_low_air",
    "stats__movement__time_high_air",
    "stats__movement__time_powerslide",
    "stats__movement__count_powerslide",
    "stats__movement__avg_powerslide_duration",
    "stats__movement__avg_speed_percentage",
    "stats__movement__percent_slow_speed",
    "stats__movement__percent_boost_speed",
    "stats__movement__percent_supersonic_speed",
    "stats__movement__percent_ground",
    "stats__movement__percent_low_air",
    "stats__movement__percent_high_air",
    "stats__positioning__avg_distance_to_ball",
    "stats__positioning__avg_distance_to_ball_possession",
    "stats__positioning__avg_distance_to_ball_no_possession",
    "stats__positioning__avg_distance_to_mates",
    "stats__positioning__time_defensive_third",
    "stats__positioning__time_neutral_third",
    "stats__positioning__time_offensive_third",
    "stats__positioning__time_defensive_half",
    "stats__positioning__time_offensive_half",
    "stats__positioning__time_behind_ball",
    "stats__positioning__time_infront_ball",
    "stats__positioning__time_most_back",
    "stats__positioning__time_most_forward",
    "stats__positioning__goals_against_while_last_defender",
    "stats__positioning__time_closest_to_ball",
    "stats__positioning__time_farthest_from_ball",
    "stats__positioning__percent_defensive_third",
    "stats__positioning__percent_offensive_third",
    "stats__positioning__percent_neutral_third",
    "stats__positioning__percent_defensive_half",
    "stats__positioning__percent_offensive_half",
    "stats__positioning__percent_behind_ball",
    "stats__positioning__percent_infront_ball",
    "stats__positioning__percent_most_back",
    "stats__positioning__percent_most_forward",
    "stats__positioning__percent_closest_to_ball",
    "stats__positioning__percent_farthest_from_ball",
    "stats__demo__inflicted",
    "stats__demo__taken"
]

coltypes_players = [
    "INTEGER PRIMARY KEY AUTOINCREMENT", # id
    "INTEGER", # manifest_id
    "TEXT", # team
    "INTEGER", # start_time
    "INTEGER", # end_time
    "TEXT", # name
    "INTEGER", # car_id
    "TEXT", # car_name
    "INTEGER", # steering_sensitivity
    "TEXT", # id__platform
    "TEXT", # id__id
    "INTEGER", # rank__id
    "INTEGER", # rank__tier
    "INTEGER", # rank__division
    "INTEGER", # rank__name
    "INTEGER", # camera__fov
    "INTEGER", # camera__height
    "INTEGER", # camera__pitch
    "INTEGER", # camera__distance
    "INTEGER", # camera__stiffness
    "INTEGER", # camera__swivel_speed
    "INTEGER", # camera__transition_speed
    "INTEGER", # stats__core__shots
    "INTEGER", # stats__core__shots_against
    "INTEGER", # stats__core__goals
    "INTEGER", # stats__core__goals_against
    "INTEGER", # stats__core__saves
    "INTEGER", # stats__core__assists
    "INTEGER", # stats__core__score
    "INTEGER", # stats__core__mvp
    "INTEGER", # stats__core__shooting_percentage
    "INTEGER", # stats__boost__bpm
    "INTEGER", # stats__boost__bcpm
    "INTEGER", # stats__boost__avg_amount
    "INTEGER", # stats__boost__amount_collected
    "INTEGER", # stats__boost__amount_stolen
    "INTEGER", # stats__boost__amount_collected_big
    "INTEGER", # stats__boost__amount_stolen_big
    "INTEGER", # stats__boost__amount_collected_small
    "INTEGER", # stats__boost__amount_stolen_small
    "INTEGER", # stats__boost__count_collected_big
    "INTEGER", # stats__boost__count_stolen_big
    "INTEGER", # stats__boost__count_collected_small
    "INTEGER", # stats__boost__count_stolen_small
    "INTEGER", # stats__boost__amount_overfill
    "INTEGER", # stats__boost__amount_overfill_stolen
    "INTEGER", # stats__boost__amount_used_while_supersonic
    "INTEGER", # stats__boost__time_zero_boost
    "INTEGER", # stats__boost__percent_zero_boost
    "INTEGER", # stats__boost__time_full_boost
    "INTEGER", # stats__boost__percent_full_boost
    "INTEGER", # stats__boost__time_boost_0_25
    "INTEGER", # stats__boost__time_boost_25_50
    "INTEGER", # stats__boost__time_boost_50_75
    "INTEGER", # stats__boost__time_boost_75_100
    "INTEGER", # stats__boost__percent_boost_0_25
    "INTEGER", # stats__boost__percent_boost_25_50
    "INTEGER", # stats__boost__percent_boost_50_75
    "INTEGER", # stats__boost__percent_boost_75_100
    "INTEGER", # stats__movement__avg_speed
    "INTEGER", # stats__movement__total_distance
    "INTEGER", # stats__movement__time_supersonic_speed
    "INTEGER", # stats__movement__time_boost_speed
    "INTEGER", # stats__movement__time_slow_speed
    "INTEGER", # stats__movement__time_ground
    "INTEGER", # stats__movement__time_low_air
    "INTEGER", # stats__movement__time_high_air
    "INTEGER", # stats__movement__time_powerslide
    "INTEGER", # stats__movement__count_powerslide
    "INTEGER", # stats__movement__avg_powerslide_duration
    "INTEGER", # stats__movement__avg_speed_percentage
    "INTEGER", # stats__movement__percent_slow_speed
    "INTEGER", # stats__movement__percent_boost_speed
    "INTEGER", # stats__movement__percent_supersonic_speed
    "INTEGER", # stats__movement__percent_ground
    "INTEGER", # stats__movement__percent_low_air
    "INTEGER", # stats__movement__percent_high_air
    "INTEGER", # stats__positioning__avg_distance_to_ball
    "INTEGER", # stats__positioning__avg_distance_to_ball_possession
    "INTEGER", # stats__positioning__avg_distance_to_ball_no_possession
    "INTEGER", # stats__positioning__avg_distance_to_mates
    "INTEGER", # stats__positioning__time_defensive_third
    "INTEGER", # stats__positioning__time_neutral_third
    "INTEGER", # stats__positioning__time_offensive_third
    "INTEGER", # stats__positioning__time_defensive_half
    "INTEGER", # stats__positioning__time_offensive_half
    "INTEGER", # stats__positioning__time_behind_ball
    "INTEGER", # stats__positioning__time_infront_ball
    "INTEGER", # stats__positioning__time_most_back
    "INTEGER", # stats__positioning__time_most_forward
    "INTEGER", # stats__positioning__goals_against_while_last_defender
    "INTEGER", # stats__positioning__time_closest_to_ball
    "INTEGER", # stats__positioning__time_farthest_from_ball
    "INTEGER", # stats__positioning__percent_defensive_third
    "INTEGER", # stats__positioning__percent_offensive_third
    "INTEGER", # stats__positioning__percent_neutral_third
    "INTEGER", # stats__positioning__percent_defensive_half
    "INTEGER", # stats__positioning__percent_offensive_half
    "INTEGER", # stats__positioning__percent_behind_ball
    "INTEGER", # stats__positioning__percent_infront_ball
    "INTEGER", # stats__positioning__percent_most_back
    "INTEGER", # stats__positioning__percent_most_forward
    "INTEGER", # stats__positioning__percent_closest_to_ball
    "INTEGER", # stats__positioning__percent_farthest_from_ball
    "INTEGER", # stats__demo__inflicted
    "INTEGER" # stats__demo__taken
]

dictlocs_players = [
    ("start_time",),
    ("end_time",),
    ("name",),
    ("car_id",),
    ("car_name",),
    ("steering_sensitivity",),
    ("id", "platform"),
    ("id", "id"),
    ("rank", "id"),
    ("rank", "tier"),
    ("rank", "division"),
    ("rank", "name"),
    ("camera", "fov"),
    ("camera", "height"),
    ("camera", "pitch"),
    ("camera", "distance"),
    ("camera", "stiffness"),
    ("camera", "swivel_speed"),
    ("camera", "transition_speed"),
    ("stats", "core", "shots"),
    ("stats", "core", "shots_against"),
    ("stats", "core", "goals"),
    ("stats", "core", "goals_against"),
    ("stats", "core", "saves"),
    ("stats", "core", "assists"),
    ("stats", "core", "score"),
    ("stats", "core", "mvp"),
    ("stats", "core", "shooting_percentage"),
    ("stats", "boost", "bpm"),
    ("stats", "boost", "bcpm"),
    ("stats", "boost", "avg_amount"),
    ("stats", "boost", "amount_collected"),
    ("stats", "boost", "amount_stolen"),
    ("stats", "boost", "amount_collected_big"),
    ("stats", "boost", "amount_stolen_big"),
    ("stats", "boost", "amount_collected_small"),
    ("stats", "boost", "amount_stolen_small"),
    ("stats", "boost", "count_collected_big"),
    ("stats", "boost", "count_stolen_big"),
    ("stats", "boost", "count_collected_small"),
    ("stats", "boost", "count_stolen_small"),
    ("stats", "boost", "amount_overfill"),
    ("stats", "boost", "amount_overfill_stolen"),
    ("stats", "boost", "amount_used_while_supersonic"),
    ("stats", "boost", "time_zero_boost"),
    ("stats", "boost", "percent_zero_boost"),
    ("stats", "boost", "time_full_boost"),
    ("stats", "boost", "percent_full_boost"),
    ("stats", "boost", "time_boost_0_25"),
    ("stats", "boost", "time_boost_25_50"),
    ("stats", "boost", "time_boost_50_75"),
    ("stats", "boost", "time_boost_75_100"),
    ("stats", "boost", "percent_boost_0_25"),
    ("stats", "boost", "percent_boost_25_50"),
    ("stats", "boost", "percent_boost_50_75"),
    ("stats", "boost", "percent_boost_75_100"),
    ("stats", "movement", "avg_speed"),
    ("stats", "movement", "total_distance"),
    ("stats", "movement", "time_supersonic_speed"),
    ("stats", "movement", "time_boost_speed"),
    ("stats", "movement", "time_slow_speed"),
    ("stats", "movement", "time_ground"),
    ("stats", "movement", "time_low_air"),
    ("stats", "movement", "time_high_air"),
    ("stats", "movement", "time_powerslide"),
    ("stats", "movement", "count_powerslide"),
    ("stats", "movement", "avg_powerslide_duration"),
    ("stats", "movement", "avg_speed_percentage"),
    ("stats", "movement", "percent_slow_speed"),
    ("stats", "movement", "percent_boost_speed"),
    ("stats", "movement", "percent_supersonic_speed"),
    ("stats", "movement", "percent_ground"),
    ("stats", "movement", "percent_low_air"),
    ("stats", "movement", "percent_high_air"),
    ("stats", "positioning", "avg_distance_to_ball"),
    ("stats", "positioning", "avg_distance_to_ball_possession"),
    ("stats", "positioning", "avg_distance_to_ball_no_possession"),
    ("stats", "positioning", "avg_distance_to_mates"),
    ("stats", "positioning", "time_defensive_third"),
    ("stats", "positioning", "time_neutral_third"),
    ("stats", "positioning", "time_offensive_third"),
    ("stats", "positioning", "time_defensive_half"),
    ("stats", "positioning", "time_offensive_half"),
    ("stats", "positioning", "time_behind_ball"),
    ("stats", "positioning", "time_infront_ball"),
    ("stats", "positioning", "time_most_back"),
    ("stats", "positioning", "time_most_forward"),
    ("stats", "positioning", "goals_against_while_last_defender"),
    ("stats", "positioning", "time_closest_to_ball"),
    ("stats", "positioning", "time_farthest_from_ball"),
    ("stats", "positioning", "percent_defensive_third"),
    ("stats", "positioning", "percent_offensive_third"),
    ("stats", "positioning", "percent_neutral_third"),
    ("stats", "positioning", "percent_defensive_half"),
    ("stats", "positioning", "percent_offensive_half"),
    ("stats", "positioning", "percent_behind_ball"),
    ("stats", "positioning", "percent_infront_ball"),
    ("stats", "positioning", "percent_most_back"),
    ("stats", "positioning", "percent_most_forward"),
    ("stats", "positioning", "percent_closest_to_ball"),
    ("stats", "positioning", "percent_farthest_from_ball"),
    ("stats", "demo", "inflicted"),
    ("stats", "demo", "taken")
]

colnames_teams = [
    "id",
    "manifest_id",
    "team",
    "color",
    "name",
    "stats__ball__possession_time",
    "stats__ball__time_in_side",
    "stats__core__shots",
    "stats__core__shots_against",
    "stats__core__goals",
    "stats__core__goals_against",
    "stats__core__saves",
    "stats__core__assists",
    "stats__core__score",
    "stats__core__shooting_percentage",
    "stats__boost__bpm",
    "stats__boost__bcpm",
    "stats__boost__avg_amount",
    "stats__boost__amount_collected",
    "stats__boost__amount_stolen",
    "stats__boost__amount_collected_big",
    "stats__boost__amount_stolen_big",
    "stats__boost__amount_collected_small",
    "stats__boost__amount_stolen_small",
    "stats__boost__count_collected_big",
    "stats__boost__count_stolen_big",
    "stats__boost__count_collected_small",
    "stats__boost__count_stolen_small",
    "stats__boost__amount_overfill",
    "stats__boost__amount_overfill_stolen",
    "stats__boost__amount_used_while_supersonic",
    "stats__boost__time_zero_boost",
    "stats__boost__time_full_boost",
    "stats__boost__time_boost_0_25",
    "stats__boost__time_boost_25_50",
    "stats__boost__time_boost_50_75",
    "stats__boost__time_boost_75_100",
    "stats__movement__total_distance",
    "stats__movement__time_supersonic_speed",
    "stats__movement__time_boost_speed",
    "stats__movement__time_slow_speed",
    "stats__movement__time_ground",
    "stats__movement__time_low_air",
    "stats__movement__time_high_air",
    "stats__movement__time_powerslide",
    "stats__movement__count_powerslide",
    "stats__positioning__time_defensive_third",
    "stats__positioning__time_neutral_third",
    "stats__positioning__time_offensive_third",
    "stats__positioning__time_defensive_half",
    "stats__positioning__time_offensive_half",
    "stats__positioning__time_behind_ball",
    "stats__positioning__time_infront_ball",
    "stats__demo__inflicted",
    "stats__demo__taken"
]

coltypes_teams = [
    "INTEGER PRIMARY KEY AUTOINCREMENT", # id
    "INTEGER", # manifest_id
    "INTEGER", # team
    "TEXT", # color
    "TEXT", # name
    "INTEGER", # stats__ball__possession_time
    "INTEGER", # stats__ball__time_in_side
    "INTEGER", # stats__core__shots
    "INTEGER", # stats__core__shots_against
    "INTEGER", # stats__core__goals
    "INTEGER", # stats__core__goals_against
    "INTEGER", # stats__core__saves
    "INTEGER", # stats__core__assists
    "INTEGER", # stats__core__score
    "INTEGER", # stats__core__shooting_percentage
    "INTEGER", # stats__boost__bpm
    "INTEGER", # stats__boost__bcpm
    "INTEGER", # stats__boost__avg_amount
    "INTEGER", # stats__boost__amount_collected
    "INTEGER", # stats__boost__amount_stolen
    "INTEGER", # stats__boost__amount_collected_big
    "INTEGER", # stats__boost__amount_stolen_big
    "INTEGER", # stats__boost__amount_collected_small
    "INTEGER", # stats__boost__amount_stolen_small
    "INTEGER", # stats__boost__count_collected_big
    "INTEGER", # stats__boost__count_stolen_big
    "INTEGER", # stats__boost__count_collected_small
    "INTEGER", # stats__boost__count_stolen_small
    "INTEGER", # stats__boost__amount_overfill
    "INTEGER", # stats__boost__amount_overfill_stolen
    "INTEGER", # stats__boost__amount_used_while_supersonic
    "INTEGER", # stats__boost__time_zero_boost
    "INTEGER", # stats__boost__time_full_boost
    "INTEGER", # stats__boost__time_boost_0_25
    "INTEGER", # stats__boost__time_boost_25_50
    "INTEGER", # stats__boost__time_boost_50_75
    "INTEGER", # stats__boost__time_boost_75_100
    "INTEGER", # stats__movement__total_distance
    "INTEGER", # stats__movement__time_supersonic_speed
    "INTEGER", # stats__movement__time_boost_speed
    "INTEGER", # stats__movement__time_slow_speed
    "INTEGER", # stats__movement__time_ground
    "INTEGER", # stats__movement__time_low_air
    "INTEGER", # stats__movement__time_high_air
    "INTEGER", # stats__movement__time_powerslide
    "INTEGER", # stats__movement__count_powerslide
    "INTEGER", # stats__positioning__time_defensive_third
    "INTEGER", # stats__positioning__time_neutral_third
    "INTEGER", # stats__positioning__time_offensive_third
    "INTEGER", # stats__positioning__time_defensive_half
    "INTEGER", # stats__positioning__time_offensive_half
    "INTEGER", # stats__positioning__time_behind_ball
    "INTEGER", # stats__positioning__time_infront_ball
    "INTEGER", # stats__demo__inflicted
    "INTEGER" # stats__demo__taken
]

dictlocs_teams = [
    ("color",),
    ("name",),
    ("stats", "ball", "possession_time"),
    ("stats", "ball", "time_in_side"),
    ("stats", "core", "shots"),
    ("stats", "core", "shots_against"),
    ("stats", "core", "goals"),
    ("stats", "core", "goals_against"),
    ("stats", "core", "saves"),
    ("stats", "core", "assists"),
    ("stats", "core", "score"),
    ("stats", "core", "shooting_percentage"),
    ("stats", "boost", "bpm"),
    ("stats", "boost", "bcpm"),
    ("stats", "boost", "avg_amount"),
    ("stats", "boost", "amount_collected"),
    ("stats", "boost", "amount_stolen"),
    ("stats", "boost", "amount_collected_big"),
    ("stats", "boost", "amount_stolen_big"),
    ("stats", "boost", "amount_collected_small"),
    ("stats", "boost", "amount_stolen_small"),
    ("stats", "boost", "count_collected_big"),
    ("stats", "boost", "count_stolen_big"),
    ("stats", "boost", "count_collected_small"),
    ("stats", "boost", "count_stolen_small"),
    ("stats", "boost", "amount_overfill"),
    ("stats", "boost", "amount_overfill_stolen"),
    ("stats", "boost", "amount_used_while_supersonic"),
    ("stats", "boost", "time_zero_boost"),
    ("stats", "boost", "time_full_boost"),
    ("stats", "boost", "time_boost_0_25"),
    ("stats", "boost", "time_boost_25_50"),
    ("stats", "boost", "time_boost_50_75"),
    ("stats", "boost", "time_boost_75_100"),
    ("stats", "movement", "total_distance"),
    ("stats", "movement", "time_supersonic_speed"),
    ("stats", "movement", "time_boost_speed"),
    ("stats", "movement", "time_slow_speed"),
    ("stats", "movement", "time_ground"),
    ("stats", "movement", "time_low_air"),
    ("stats", "movement", "time_high_air"),
    ("stats", "movement", "time_powerslide"),
    ("stats", "movement", "count_powerslide"),
    ("stats", "positioning", "time_defensive_third"),
    ("stats", "positioning", "time_neutral_third"),
    ("stats", "positioning", "time_offensive_third"),
    ("stats", "positioning", "time_defensive_half"),
    ("stats", "positioning", "time_offensive_half"),
    ("stats", "positioning", "time_behind_ball"),
    ("stats", "positioning", "time_infront_ball"),
    ("stats", "demo", "inflicted"),
    ("stats", "demo", "taken")
]

colnames_manifest = [
    "id",
    "replay_id",
    "uploader__steam_id",
    "rocket_league_id",
    "match_guid",
    "title",
    "map_code",
    "match_type",
    "team_size",
    "playlist_id",
    "duration",
    "season",
    "season_type",
    "overtime_seconds",
    "created",
    "date",
    "min_rank__id",
    "min_rank__tier",
    "min_rank__division",
    "min_rank__name",
    "max_rank__id",
    "max_rank__tier",
    "max_rank__division",
    "max_rank__name"
]

coltypes_manifest = [
    "INTEGER PRIMARY KEY AUTOINCREMENT", # id
    "TEXT", # replay_id
    "TEXT", # uploader__steam_id
    "TEXT", # rocket_league_id
    "TEXT", # match_guid
    "TEXT", # title
    "TEXT", # map_code
    "TEXT", # match_type
    "INTEGER", # team_size
    "TEXT", # playlist_id
    "INTEGER", # duration
    "INTEGER", # season
    "TEXT", # season_type
    "INTEGER", # overtime_seconds
    "INTEGER", # created
    "INTEGER", # date
    "TEXT", # min_rank__id
    "INTEGER", # min_rank__tier
    "INTEGER", # min_rank__division
    "TEXT", # min_rank__name
    "TEXT", # max_rank__id
    "INTEGER", # max_rank__tier
    "INTEGER", # max_rank__division
    "TEXT" # max_rank__name
]

dictlocs_manifest = [
    ("id",),
    ("uploader", "steam_id",),
    ("rocket_league_id",),
    ("match_guid",),
    ("title",),
    ("map_code",),
    ("match_type",),
    ("team_size",),
    ("playlist_id",),
    ("duration",),
    ("season",),
    ("season_type",),
    ("overtime_seconds",),
    # ("created",),
    # ("date",),
    ("min_rank", "id"),
    ("min_rank", "tier"),
    ("min_rank", "division"),
    ("min_rank", "name"),
    ("max_rank", "id"),
    ("max_rank", "tier"),
    ("max_rank", "division"),
    ("max_rank", "name")
]

attrs_Rank = [
    "id",
    "tier",
    "division",
    "name"
]

attrs_Player = [
    "start_time",
    "end_time",
    "name",
    "car_id",
    "car_name",
    "steering_sensitivity"
]

attrs_Id = [
    "platform",
    "id"
]

attrs_Camera = [
    "fov",
    "height",
    "pitch",
    "distance",
    "stiffness",
    "swivel_speed",
    "transition_speed"
]

attrs_PStats_core = [
    "shots",
    "shots_against",
    "goals",
    "goals_against",
    "saves",
    "assists",
    "score",
    "mvp",
    "shooting_percentage"
]

attrs_PStats_boost = [
    "bpm",
    "bcpm",
    "avg_amount",
    "amount_collected",
    "amount_stolen",
    "amount_collected_big",
    "amount_stolen_big",
    "amount_collected_small",
    "amount_stolen_small",
    "count_collected_big",
    "count_stolen_big",
    "count_collected_small",
    "count_stolen_small",
    "amount_overfill",
    "amount_overfill_stolen",
    "amount_used_while_supersonic",
    "time_zero_boost",
    "percent_zero_boost",
    "time_full_boost",
    "percent_full_boost",
    "time_boost_0_25",
    "time_boost_25_50",
    "time_boost_50_75",
    "time_boost_75_100",
    "percent_boost_0_25",
    "percent_boost_25_50",
    "percent_boost_50_75",
    "percent_boost_75_100"
]

attrs_PStats_movement = [
    "avg_speed",
    "total_distance",
    "time_supersonic_speed",
    "time_boost_speed",
    "time_slow_speed",
    "time_ground",
    "time_low_air",
    "time_high_air",
    "time_powerslide",
    "count_powerslide",
    "avg_powerslide_duration",
    "avg_speed_percentage",
    "percent_slow_speed",
    "percent_boost_speed",
    "percent_supersonic_speed",
    "percent_ground",
    "percent_low_air",
    "percent_high_air"
]

attrs_PStats_positioning = [
    "avg_distance_to_ball",
    "avg_distance_to_ball_possession",
    "avg_distance_to_ball_no_possession",
    "avg_distance_to_mates",
    "time_defensive_third",
    "time_neutral_third",
    "time_offensive_third",
    "time_defensive_half",
    "time_offensive_half",
    "time_behind_ball",
    "time_infront_ball",
    "time_most_back",
    "time_most_forward",
    "goals_against_while_last_defender",
    "time_closest_to_ball",
    "time_farthest_from_ball",
    "percent_defensive_third",
    "percent_offensive_third",
    "percent_neutral_third",
    "percent_defensive_half",
    "percent_offensive_half",
    "percent_behind_ball",
    "percent_infront_ball",
    "percent_most_back",
    "percent_most_forward",
    "percent_closest_to_ball",
    "percent_farthest_from_ball"
]

attrs_PStats_demo = [
    "inflicted",
    "taken"
]

attrs_TStats_ball = [
    "possession_time",
    "time_in_side"
]

attrs_TStats_core = [
    "shots",
    "shots_against",
    "goals",
    "goals_against",
    "saves",
    "assists",
    "score",
    "shooting_percentage"
]

attrs_TStats_boost = [
    "bpm",
    "bcpm",
    "avg_amount",
    "amount_collected",
    "amount_stolen",
    "amount_collected_big",
    "amount_stolen_big",
    "amount_collected_small",
    "amount_stolen_small",
    "count_collected_big",
    "count_stolen_big",
    "count_collected_small",
    "count_stolen_small",
    "amount_overfill",
    "amount_overfill_stolen",
    "amount_used_while_supersonic",
    "time_zero_boost",
    "time_full_boost",
    "time_boost_0_25",
    "time_boost_25_50",
    "time_boost_50_75",
    "time_boost_75_100"
]

attrs_TStats_movement = [
    "total_distance",
    "time_supersonic_speed",
    "time_boost_speed",
    "time_slow_speed",
    "time_ground",
    "time_low_air",
    "time_high_air",
    "time_powerslide",
    "count_powerslide"
]

attrs_TStats_positioning = [
    "time_defensive_third",
    "time_neutral_third",
    "time_offensive_third",
    "time_defensive_half",
    "time_offensive_half",
    "time_behind_ball",
    "time_infront_ball"
]

attrs_TStats_demo = [
    "inflicted",
    "taken"
]

attrs_Team = [
    "color",
    "name"
]

attrs_Game = [
    "id",
    "replay_id",
    "uploader__steam_id",
    "rocket_league_id",
    "match_guid",
    "title",
    "map_code",
    "match_type",
    "team_size",
    "playlist_id",
    "duration",
    "season",
    "season_type",
    "overtime_seconds",
    "created",
    "date"
]
