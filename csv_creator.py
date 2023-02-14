import os
import json


class FileHandler:

    def __init__(self, game: str, bosses: dict):
        self.game = game
        self.bosses = bosses
        self.filename = f'data/{self.game}'

    def create_file(self):
        if os.path(f'data/{self.game}').exists():
            pass
        else:
            with open(self.filename, 'w') as f:
                json.dump({key: 0 for key in self.bosses.keys()}, f, indent=4)

    def update(self):
        with open(self.filename, 'r') as data:
            data = json.load(data)
        data.pop('Total')
        data['Total'] = sum(data.values())
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    def increment_boss(self, boss: str = 'Other'):
        with open(self.filename, 'r') as data:
            data = json.load(data)
        boss_data = data.pop(boss)
        data[boss] = boss_data + 1
        data.pop('Total')
        data['Total'] = sum(data.values())
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
