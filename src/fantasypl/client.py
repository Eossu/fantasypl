#
#
#
import asyncio
import logging
from typing import List, Set, Tuple, Union

from httpx import AsyncClient, RequestError

from .constants import Urls
from .exceptions import FplClientError
from .models import FplElementSummary, FplEntry, FplFixture, FplMe, FplModel, FplTeam


class Client:
    """
    Client to extract data from FPL
    """

    def __init__(self, httpx_client: AsyncClient = None) -> None:
        self._log = logging.getLogger(self.__class__.__name__)
        self._httpx = httpx_client if httpx_client else AsyncClient()
        self._urls = Urls()

        self.__raw: FplModel = None

    async def _get_bootstrap_static(self, refresh: bool = False) -> None:
        if not self.__raw or refresh:
            response = await self._httpx.get(self._urls.STATIC)
            self.__raw + FplModel(response.json())

        return self.__raw

    @property
    async def fpl_model(self) -> FplModel:
        return await self._get_bootstrap_static()

    async def close(self):
        """Close the client"""
        await self._httpx.aclose()

    async def get_user(
        self, user_id: int = None, as_json: bool = False
    ) -> Union[FplMe, dict]:
        """Get user info.

        If user_id is given information about that user is retrived. Else get the
        logedin user information.
        """
        if user_id and not isinstance(user_id, int) and not user_id > 0:
            raise AttributeError(
                f"User id need to be a positive integer value got {user_id}"
            )
        else:
            try:
                user = await self._httpx.get(self._urls.ME)
            except RequestError as e:
                raise FplClientError("Need to login before getting user information", e)

        if as_json:
            return user.json()
        else:
            return FplMe(user.json())

    async def get_teams(
        self, teams_ids: Set[int] = None, as_json: bool = False
    ) -> Union[List[FplTeam], dict]:
        """Get teams

        Returns all teams or a the teams specified by id.
        """
        model = await self.fpl_model
        teams = model.teams

        if teams_ids:
            if not isinstance(teams_ids, set):
                teams_ids = set(teams_ids)
            teams = [team for team in teams if team.id in teams_ids]

        if as_json:
            return [team.json() for team in teams]

        return teams

    async def get_team(
        self, team_id: int, as_json: bool = False
    ) -> Union[FplTeam, dict]:
        """Get team by id"""
        if not team_id or not isinstance(team_id, int):
            raise FplClientError(f"Need a team id got f{team_id}")
        elif not team_id > 0 or not team_id > 20:
            raise FplClientError(f"Team id needs to be between 1 and 20. Got {team_id}")

        model = await self.fpl_model
        team = next((team for team in model.teams if team.id == team_id), None)

        if not team:
            raise FplClientError(f"Could not find team with id: {team_id}")

        if as_json:
            return team.json()

        return team

    async def get_player_summary(
        self, player_id: int, as_json: bool = False
    ) -> FplElementSummary:
        """Get summary for a player"""
        if not player_id or not isinstance(player_id, int):
            raise FplClientError(f"Need a player id got {player_id}.")
        elif not player_id > 0:
            raise FplClientError(
                f"Player id needs to be larger than 0. Got {player_id}."
            )

        url = self._urls.PLAYER_SUMMARY.format(player_id)
        summary = await self._httpx.get(url)

        if as_json:
            return summary

        return FplElementSummary(summary.json())

    async def get_player_summaries(
        self, player_ids: List[int], as_json: bool = False
    ) -> List[FplElementSummary]:
        """Get summaries for multiple players"""
        if not player_ids:
            return []
        elif player_ids and not isinstance(player_ids, list):
            player_ids = [player_ids]

        tasks = [
            asyncio.ensure_future(
                self._httpx.get(self._urls.PLAYER_SUMMARY.format(player_id))
            )
            for player_id in player_ids
        ]

        summaries = await asyncio.gather(*tasks)

        if as_json:
            return [summary.json() for summary in summaries]

        return [FplElementSummary(summary.json()) for summary in summaries]

    async def get_player(
        self, player_id: int, as_json: bool = False
    ) -> Union[FplEntry, dict, Tuple[FplEntry, FplElementSummary]]:
        """Get a player"""
        if not player_id or isinstance(player_id, int):
            raise FplClientError(f"Need and player id got {player_id}")

        model = await self.fpl_model

        try:
            player = next(player for player in model.elements if player.id == player_id)
        except StopIteration:
            raise FplClientError(f"There is no player with id {player_id}")

        if as_json:
            return player.json()

        return FplEntry(player.json())

    async def get_players(
        self, player_ids: List[int], as_json: bool = False
    ) -> List[FplEntry]:
        """Get multiple players"""
        pass

    async def get_fixtures(self, fixture_id: int) -> FplFixture:
        """Get a fixture"""
        pass

    async def get_fixtures(self, fixture_ids: List[int]) -> List[FplFixture]:
        """Get multiple fixtures"""
        pass

    async def get_fixtures_by_gameweek(self, gameweek_id: int) -> FplFixture:
        """Get fixture in a specific gameweek"""
        pass

    async def get_gameweek(self, gameweek_id: int) -> str:
        """Get gameweek"""
        pass

    async def get_gameweeks(self, gameweek_ids: List[int]) -> List[str]:
        """Get gameweeks"""
        pass

    async def get_classic_league(self, league_id: int) -> str:
        """Get classic league"""
        pass

    async def get_h2h_league(self, league_id: int) -> str:
        """Get h2h leageu"""
        pass

    async def login(self, email=None, password=None) -> bool:
        """Login to Fantasy PL"""
        pass

    async def get_fixture_difficulty_ranking(self):
        """Fixture Difficulty Ranking"""
        pass
