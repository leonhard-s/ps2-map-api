"""Dataclass representations of payloads sent between the DB and API.

Types are not enforced as of this version.
"""

import dataclasses
from typing import List, Optional, Tuple

from .types import (BaseId, BaseTypeId, ContinentId, FactionId, FactionData,
                    OutfitId, OutfitTag, ResourceId, ServerId)


@dataclasses.dataclass(frozen=True)
class _Static:
    """Base class for static map data.

    This includes base or continent names, map hex outlines and other
    information that only changes with game upates (i.e. in-between app
    launches).
    """


@dataclasses.dataclass(frozen=True)
class _Dynamic:
    """Base class for dynamic map data.

    This includes current population, facility ownership and the
    continents available for each server. Data of this type can either
    be polled or received via a WebSocket interface whenever it
    changes.
    """


@dataclasses.dataclass(frozen=True)
class BaseInfo(_Static):
    """Static, unchanging base data."""

    id: BaseId
    continent_id: ContinentId
    name: str
    map_pos: Tuple[float, float]
    # Base type (BioLab, Small Outpost, etc.)
    type_id: BaseTypeId
    type_name: str
    # Outfit resources
    # NOTE: Rewards are not consistent within a base type.
    resource_amount: int
    resource_id: ResourceId
    resource_name: str


@dataclasses.dataclass(frozen=True)
class BaseUpdate(_Dynamic):
    """Dynamic base state update."""

    id: BaseId
    population: FactionData[int]
    owning_faction: FactionId
    owning_outfit: Optional[OutfitId]
    held_since: int


@dataclasses.dataclass(frozen=True)
class ContinentInfo(_Static):
    """Static, unchanging continent data."""

    id: ContinentId
    name: str
    description: str
    bases: List[BaseInfo]
    lattice_links: List[Tuple[int, int]]
    # TODO: Should these be part of this type? How'd the CDN work?
    map_outlines_svg: str  # Map outline SVG
    map_tileset: str  # Unique tileset identifier for the frontend


@dataclasses.dataclass(frozen=True)
class ContinentUpdate(_Dynamic):
    """Dynamic continent state update."""

    id: ContinentId
    population: FactionData[int]
    status: str
    locked_by: Optional[int]
    # Alert status
    alert_active: bool
    alert_started: int
    alert_ends: int
    alert_status: FactionData[float]


@dataclasses.dataclass(frozen=True)
class ServerInfo(_Static):
    """Static, unchanging server data."""

    id: ServerId
    name: str
    region: str


@dataclasses.dataclass(frozen=True)
class ServerUpdate(_Dynamic):
    """Dynamic server state update."""

    id: ServerId
    status: str
    population: FactionData[int]
    open_continents: List[ContinentId]


@dataclasses.dataclass(frozen=True)
class OutfitInfo(_Static):
    """Static, unchanging outfit data."""

    id: OutfitId
    faction_id: FactionId
    server_id: ServerId
    name: str
    tag: OutfitTag
