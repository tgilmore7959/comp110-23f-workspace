"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    
    
    def __init__(self, num_fish: int, num_bears:int) -> None:
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self) -> None:
        keep_fish = []
        keep_bears = []  
        for fish in self.fish:
            if fish.age <= 3:
               keep_fish.append(fish)

        for bear in self.bears:
            if bear.age <= 5:
                keep_bears.append(bear)

        self.fish = keep_fish
        self.bears = keep_bears 
        return None

    def bears_eating(self) -> None:
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self) -> None:
        """Removes bears with hunger score below zero."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self) -> None:
        new_fish = (len(self.fish) //2) * 4
        for fishies in range(new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self) -> None:
        new_bears = (len(self.bears) //2)
        for x in range(new_bears):
            self.bears.append(Bear())
        return None
    
    def view_river(self) -> None:
        """Prints how many in each class"""
        print(f"~~~Day {self.day}~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Runs one day 7 times."""
        for x in range(7):
            self.one_river_day()
        return None
    
    def remove_fish(self, amount: int):
        """removes front fish."""
        for x in range (amount):
            if len(self.fish) >= 1:
                self.fish.pop(0)
        return None
      
