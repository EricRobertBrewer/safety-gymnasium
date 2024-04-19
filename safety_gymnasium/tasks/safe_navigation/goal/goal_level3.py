from safety_gymnasium.assets.geoms import Hazards
from safety_gymnasium.tasks.safe_navigation.goal.goal_level1 import GoalLevel0


class GoalLevel3(GoalLevel0):
    """An agent must navigate to a goal while avoiding more hazards and vases."""

    def __init__(self, config) -> None:
        super().__init__(config=config)
        # pylint: disable=no-member

        # self.placements_conf.extents = [-2, -2, 2, 2]
        self.placements_conf.extents = [-1, -1, 1, 1]

        self._add_geoms(Hazards(num=1, keepout=0.18))
