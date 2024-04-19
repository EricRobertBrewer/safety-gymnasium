from safety_gymnasium.assets.free_geoms import Vases
from safety_gymnasium.tasks.safe_navigation.goal.goal_level1 import GoalLevel1


class GoalLevel4(GoalLevel1):
    """An agent must navigate to a goal while avoiding more hazards and vases."""

    def __init__(self, config) -> None:
        super().__init__(config=config)
        # pylint: disable=no-member

        # self.placements_conf.extents = [-2, -2, 2, 2]
        self.placements_conf.extents = [-1, -1, 1, 1]

        self._add_free_geoms(Vases(num=1, is_constrained=False))
