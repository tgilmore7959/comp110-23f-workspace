"""River Simulation."""
__author__ = "730585444"


from exercises.ex08.river import River

my_river: River = River(10, 2)
my_river.view_river()

my_river.one_river_week()