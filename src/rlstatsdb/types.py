"""Types used for ``models``, primarily to improve linting and autocomplete.

:copyright: (c) 2022 Tanner B. Corcoran
:license: MIT, see LICENSE for more details.

"""

number = int | float

class Rank:
    id: str
    tier: number
    division: number
    name: str

class Id:
    platform: str
    id: str

class Camera:
    fov: number
    height: number
    pitch: number
    distance: number
    stiffness: number
    swivel_speed: number
    transition_speed: number

class PStats_core:
    shots: number
    shots_against: number
    goals: number
    goals_against: number
    saves: number
    assists: number
    score: number
    mvp: bool
    shooting_percentage: number

class PStats_boost:
    bpm: number
    bcpm: number
    avg_amount: number
    amount_collected: number
    amount_stolen: number
    amount_collected_big: number
    amount_stolen_big: number
    amount_collected_small: number
    amount_stolen_small: number
    count_collected_big: number
    count_stolen_big: number
    count_collected_small: number
    count_stolen_small: number
    amount_overfill: number
    amount_overfill_stolen: number
    amount_used_while_supersonic: number
    time_zero_boost: number
    percent_zero_boost: number
    time_full_boost: number
    percent_full_boost: number
    time_boost_0_25: number
    time_boost_25_50: number
    time_boost_50_75: number
    time_boost_75_100: number
    percent_boost_0_25: number
    percent_boost_25_50: number
    percent_boost_50_75: number
    percent_boost_75_100: number

class PStats_movement:
    avg_speed: number
    total_distance: number
    time_supersonic_speed: number
    time_boost_speed: number
    time_slow_speed: number
    time_ground: number
    time_low_air: number
    time_high_air: number
    time_powerslide: number
    count_powerslide: number
    avg_powerslide_duration: number
    avg_speed_percentage: number
    percent_slow_speed: number
    percent_boost_speed: number
    percent_supersonic_speed: number
    percent_ground: number
    percent_low_air: number
    percent_high_air: number

class PStats_positioning:
    avg_distance_to_ball: number
    avg_distance_to_ball_possession: number
    avg_distance_to_ball_no_possession: number
    avg_distance_to_mates: number
    time_defensive_third: number
    time_neutral_third: number
    time_offensive_third: number
    time_defensive_half: number
    time_offensive_half: number
    time_behind_ball: number
    time_infront_ball: number
    time_most_back: number
    time_most_forward: number
    goals_against_while_last_defender: number
    time_closest_to_ball: number
    time_farthest_from_ball: number
    percent_defensive_third: number
    percent_offensive_third: number
    percent_neutral_third: number
    percent_defensive_half: number
    percent_offensive_half: number
    percent_behind_ball: number
    percent_infront_ball: number
    percent_most_back: number
    percent_most_forward: number
    percent_closest_to_ball: number
    percent_farthest_from_ball: number

class PStats_demo:
    inflicted: number
    taken: number

class PStats:
    class core(PStats_core): ...
    class boost(PStats_boost): ...
    class movement(PStats_movement): ...
    class positioning(PStats_positioning): ...
    class demo(PStats_demo): ...

class Player:
    start_time: number
    end_time: number
    name: str
    car_id: number
    car_name: str
    steering_sensitivity: number
    class id(Id): ...
    class rank(Rank): ...
    class camera(Camera): ...
    class stats(PStats): ...

class TStats_ball:
    possession_time: number
    time_in_side: number

class TStats_core:
    shots: number
    shots_against: number
    goals: number
    goals_against: number
    saves: number
    assists: number
    score: number
    shooting_percentage: number
    
class TStats_boost:
    bpm: number
    bcpm: number
    avg_amount: number
    amount_collected: number
    amount_stolen: number
    amount_collected_big: number
    amount_stolen_big: number
    amount_collected_small: number
    amount_stolen_small: number
    count_collected_big: number
    count_stolen_big: number
    count_collected_small: number
    count_stolen_small: number
    amount_overfill: number
    amount_overfill_stolen: number
    amount_used_while_supersonic: number
    time_zero_boost: number
    time_full_boost: number
    time_boost_0_25: number
    time_boost_25_50: number
    time_boost_50_75: number
    time_boost_75_100: number

class TStats_movement:
    total_distance: number
    time_supersonic_speed: number
    time_boost_speed: number
    time_slow_speed: number
    time_ground: number
    time_low_air: number
    time_high_air: number
    time_powerslide: number
    count_powerslide: number

class TStats_positioning:
    time_defensive_third: number
    time_neutral_third: number
    time_offensive_third: number
    time_defensive_half: number
    time_offensive_half: number
    time_behind_ball: number
    time_infront_ball: number

class TStats_demo:
    demo__inflicted: number
    demo__taken: number

class TStats:
    class ball(TStats_ball): ...
    class core(TStats_core): ...
    class boost(TStats_boost): ...
    class movement(TStats_movement): ...
    class positioning(TStats_positioning): ...
    class demo(TStats_demo): ...

class Team:
    color: str
    name: str
    players: list[Player]
    class stats(TStats): ...

class Game:
    id: int
    replay_id: str
    uploader__steam_id: str
    rocket_league_id: str
    match_guid: str
    title: str
    map_code: str
    match_type: str
    team_size: number
    playlist_id: str
    duration: number
    season: number
    season_type: str
    overtime_seconds: number | None
    created: number
    date: number
    class min_rank(Rank): ...
    class max_rank(Rank): ...
    class blue(Team): ...
    class orange(Team): ...
