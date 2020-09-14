#
#
#
from datetime import date, datetime
from typing import Any, List
from pydantic import Model


class FplChipPlay(Model):
    """Chip Play Model -> Event"""

    chip_name: str
    num_played: int


class FplTopPlayerInfo(Model):
    """Top Player Info -> Event"""

    id: int
    points: int


class FplEvent(Model):
    """Event Model"""

    id: int
    name: str
    deadline_time: str
    average_entry_score: float
    finished: bool
    data_checked: bool
    highest_scoring_entry: float
    deadline_time_epoch: int
    deadline_time_game_offset: int
    highest_score: int
    is_previous: bool
    is_current: bool
    is_next: bool
    chip_plays: List[FplChipPlay]
    most_selected: int
    most_transferred_in: int
    top_element: int
    top_element_info: FplTopPlayerInfo
    transfers_made: int
    most_captained: int
    most_vice_captained: int


class FplGameSettings(Model):
    """Game Settings Model"""

    league_join_private_max: int
    league_join_public_max: int
    league_max_size_public_classic: int
    league_max_size_public_h2h: int
    league_max_size_private_h2h: int
    league_max_ko_rounds_private_h2h: int
    league_prefix_public: str
    league_points_h2h_win: int
    league_points_h2h_lose: int
    league_points_h2h_draw: int
    league_ko_first_instead_of_random: bool
    cup_start_event_id: int
    cup_stop_event_id: int
    cup_qualifying_method: str
    cup_type: str
    squad_squadplay: int
    squad_squadsize: int
    squad_team_limit: int
    squad_total_spend: float
    ui_currency_multiplier: int
    ui_use_special_shirts: bool
    ui_special_shirt_exclusions: List[Any]
    stats_form_days: int
    sys_vice_captain_enabled: bool
    transfers_sell_on_fee: float
    league_h2h_tiebreak_stats: List[str]
    timezone: str


class FplPhases(Model):
    """Phases Model"""

    id: int
    name: str
    start_event: int
    stop_event: int


class FplEntryStat(Model):
    """Player Stat Model"""

    label: str
    name: str


class FplEntryType(Model):
    """Player Type Model"""

    id: int
    plural_name: str
    plural_name_short: str
    singular_name: str
    singular_name_short: str
    squad_select: int
    squad_min_play: int
    squad_max_play: int
    ui_shirt_specific: str
    sub_positions_locked: List[int]
    element_count: int


class FplTeam(Model):
    """Team model"""

    code: int
    draw: int
    form: Any
    id: int
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: Any
    unavailable: bool
    win: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int
    pulse_id: int


class FplEntry(Model):
    """Player model"""

    chance_of_playing_next_round: str
    chance_of_playing_this_round: str
    code: int
    cost_change_event: int
    cost_change_event_fall: int
    cost_change_start: int
    cost_change_start_fall: int
    dreamteam_count: int
    element_type: int
    ep_next: float
    ep_this: float
    event_points: int
    first_name: str
    form: float
    id: int
    in_dreamteam: bool
    news: str
    news_added: str
    now_cost: float
    photo: str
    points_per_game: float
    second_name: str
    selected_by_percent: float
    special: bool
    squad_number: int
    status: str
    team: int
    team_code: int
    total_points: int
    transfers_in: int
    transfers_in_event: int
    transfers_out: int
    transfers_out_event: int
    value_form: float
    value_season: float
    web_name: str
    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: float
    creativity: float
    threat: float
    ict_index: float
    influence_rank: int
    influence_rank_type: int
    creativity_rank: int
    creativity_rank_type: int
    threat_rank: int
    threat_rank_type: int
    ict_index_rank: int
    ict_index_rank_type: int
    corners_and_indirect_freekicks_order: int
    corners_and_indirect_freekicks_text: str
    direct_freekicks_order: int
    direct_freekicks_text: str
    penalties_order: int
    penalties_text: str


class FplModel(Model):
    """The FPL model"""

    events: List[FplEvent]
    game_settings: FplGameSettings
    phases: List[FplPhases]
    teams: List[FplTeam]
    elements: List[FplEntry]
    element_stats: List[FplEntryStat]
    element_types: List[FplEntryType]
    total_players: int

    class Config:
        allow_mutation = False
        extra = "forbid"


class FplUserPlayer(Model):
    """User Player Model"""

    date_of_birth: str
    dirty: bool
    first_name: str
    gender: str
    id: int
    last_name: str
    region: int
    email: str
    entry: int
    entry_email: bool


class FplMe(Model):
    """Me Model"""

    player: FplUserPlayer
    watched: List[Any]


class FplMyTeamPicks(Model):
    """My Team Picks Model"""

    element: int
    position: int
    selling_price: float
    multiplier: int
    purchase_price: float
    is_captain: bool
    is_vice_captain: bool


class FplMyTeamChips(Model):
    """My Team Chip Model"""

    status_for_entry: str
    played_by_entry: List[Any]
    name: str
    number: int
    start_event: int
    stop_event: int
    chip_type: str


class FplMyTeamTransfers(Model):
    """My Team Transfers Model"""

    cost: int
    status: str
    limit: int
    made: int
    bank: float
    value: float


class FplMyTeam(Model):
    """My Team Model"""

    picks: List[FplMyTeamPicks]
    chips: List[FplMyTeamChips]
    transfers: FplMyTeamTransfers


class FplEntryLeaguesClassic(Model):
    """Entry Leagues Classic Model"""

    id: int
    name: str
    short_name: str
    created: str
    closed: bool
    rank: int
    max_entries: float
    league_type: str
    scoring: str
    admin_entry: Any
    start_event: int
    entry_rank: int
    entry_last_rank: int
    entry_can_leave: bool
    entry_can_admin: bool
    entry_can_invite: bool


class FplEntryCupStatus(Model):
    """Entry Cup Status Model"""

    qualification_event: int
    qualification_numbers: int
    qualification_rank: int
    qualification_state: str


class FplEntryCup(Model):
    """Entry Cup Model"""

    matches: List[Any]
    status: FplEntryCupStatus


class FplEntryLeagues(Model):
    """Entry Leagues Model"""

    classic: List[FplEntryLeaguesClassic]
    h2h: List[Any]
    cup: FplEntryCup


class FplEntry(Model):
    """Entry Model"""

    id: int
    joined_time: str
    started_event: int
    favourite_team: int
    player_first_name: str
    player_last_name: str
    player_region_id: int
    player_region_iso_code_short: str
    player_region_iso_code_long: str
    summary_overall_points: int
    summary_overall_rank: int
    summary_event_points: int
    summary_event_rank: int
    current_event: int
    leagues: ...
    name: str
    kit: Any
    last_deadline_bank: float
    last_deadline_value: float
    last_deadline_total_transfers: int


class FplEntryHistoryCurrent(Model):
    """Entry History Current Model"""

    event: int
    points: int
    total_points: int
    rank: int
    rank_sort: int
    overall_rank: int
    bank: float
    value: float
    event_transfers: int
    event_transgers_cost: int
    points_on_bench: int


class FplEntryHistoryPast(Model):
    """Entry History Past Model"""

    season_name: str
    total_points: int
    rank: int


class FplEntryHistory(Model):
    """Entry History Model"""

    current: List[FplEntryHistoryCurrent]
    past: List[FplEntryHistoryPast]
    chips: List[Any]


class FplElementSummaryFixtures(Model):
    """Element Summary Fixtures Model"""

    id: int
    code: int
    team_h: int
    team_h_score: int
    team_a: int
    team_a_score: int
    event: int
    finished: bool
    minutes: int
    provisional_start_time: bool
    kickoff_time: datetime
    event_name: str
    is_home: bool
    difficulty: int


class FplElementSummaryHistory(Model):
    """Element Summary History Model"""

    element: int
    fixtures: int
    opponent_team: int
    was_home: bool
    kickoff_time: datetime
    team_h_score: int
    team_a_score: int
    round: int
    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: float
    creativity: float
    threat: float
    ict_index: float
    value: float
    transfers_balance: float
    selected: int
    transfers_in: int
    transfers_out: int


class FplElementSummaryHistoryPast(Model):
    """Element Summary History Past"""

    season_name: str
    element_code: int
    start_cost: float
    end_cost: float
    total_points: int
    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: float
    creativity: float
    threat: float
    ict_index: float


class FplElementSummary(Model):
    """Element Summary Model"""

    fixtures: List[FplElementSummaryFixtures]
    history: List[FplElementSummaryHistory]
    history_past: List[FplElementSummaryHistoryPast]


class FplFixture(Model):
    code: int
    event: int
    finished: bool
    finished_provisional: bool
    id: int
    kickoff_time: datetime
    minutes: int
    provisinal_start_time: bool
    started: bool
    team_a: int
    team_a_score: int
    team_h: int
    team_h_score: int
    stats: List[Any]
    team_h_difficulty: int
    team_a_difficulty: int