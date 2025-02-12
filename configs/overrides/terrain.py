from dataclasses import dataclass, field
from configs.definitions import TerrainConfig
from typing import Tuple, Dict, Any

@dataclass
class FlatTerrainConfig(TerrainConfig):
    mesh_type: str = "plane"
    curriculum: bool = False 

@dataclass
class TrimeshTerrainConfig(TerrainConfig):
    mesh_type: str = "trimesh"
    curriculum: bool = True
    terrain_type: str = "flat"
    horizontal_scale: float = 0.1 # [m]
    vertical_scale: float = 0.005 # [m]
    border_size: float = 25. # [m]

    # measured points constitute 1m x 1.6m rectangle (without center line)
    measured_points_x: Tuple[float, ...] = (-0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8)
    measured_points_y: Tuple[float, ...] = (-0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5)

    max_init_terrain_level: int = 5
    tile_length: float = 8.
    tile_width: float = 8.
    num_rows: int = 10
    num_cols: int = 20
    slope_threshold: float = 0.75
