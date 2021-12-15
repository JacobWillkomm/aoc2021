from pathlib import Path

with Path(Path(__file__).parent, 'input').open() as file:
    input = [line for line in file.read().strip().split(',')]

class School:
    def __init__(self, school):
        self.total_fish = 0
        self.school = self.get_school(school)
        self.parent_cycle = 6
        self.years_to_maturity = 8

    def get_school(self, school):
        current_fish = {}
        for fish in school:
            self.total_fish += 1
            if int(fish) not in current_fish:
                current_fish[int(fish)] = 1
            else:
                current_fish[int(fish)] += 1
        return current_fish

    def next(self):
        for cohort in sorted(self.school):
            if cohort == 0:
                #add fish and reset counter
                self.school['new_parents'] = self.school.pop(cohort)
                self.school['new_fish'] = self.school['new_parents']
                self.total_fish += self.school['new_parents']

            else:
                self.school[cohort-1] = self.school.pop(cohort)
        if 'new_parents' in self.school:
            if self.parent_cycle in self.school:
                self.school[self.parent_cycle] += self.school.pop('new_parents')
            else:
                self.school[self.parent_cycle] = self.school.pop('new_parents')
        if 'new_fish' in self.school:
            self.school[self.years_to_maturity] = self.school.pop('new_fish')

    def calculate_size(self, time):
        for i in range(time):
            self.next()


lanternfish = School(input)
lanternfish.calculate_size(256)
print(lanternfish.total_fish)
