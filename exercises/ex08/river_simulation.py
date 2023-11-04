"""River Simulation."""


from exercises.ex08.bear import Bear
from exercises.ex08.fish import Fish
from exercises.ex08.river import River

my_river: River = River(2, 10)
my_river.view_river()

my_river.one_river_week()