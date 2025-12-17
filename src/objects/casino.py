import logging
import random

from src.my_collections.casino_balance import CasinoBalance
from src.my_collections.goose_collection import GooseCollection
from src.my_collections.player_collection import PlayerCollection
from src.objects.goose import Goose, HonkGoose, WarGoose
from src.objects.player import Player

logger = logging.getLogger(__name__)


class Casino:
    def __init__(self):
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balance = CasinoBalance()

    def register_player(self, name: str, initial_balance: int) -> Player:
        p = Player(name, initial_balance)
        self.players.add(p)
        self.balance[p.name] = p.balance
        return p

    def register_goose(self, goose: Goose) -> Goose:
        self.geese.add(goose)
        logger.info(
            f"Добавлен гусь '{goose.name}' (тип={goose.__class__.__name__}, honk={goose.honk_volume})"
        )
        return goose

    def event_player_bet(self):
        if len(self.players) == 0:
            logger.info("Пока нет игроков")
            return

        random_player_index = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(random_player_index)
        bet = random.randint(5, 50)
        player.change_balance(-bet)

        logger.info(f"{player.name} делает ставку {bet}$")
        self.balance[player.name] = player.balance

    def event_player_win(self):
        if len(self.players) == 0:
            logger.info("Пока нет игроков")
            return

        random_player_index = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(random_player_index)
        win = random.randint(0, 100)
        player.change_balance(win)

        logger.info(f"{player.name} выигрывает {win}$")
        self.balance[player.name] = player.balance

    def event_goose_attack(self):
        war_geese = [g for g in self.geese if isinstance(g, WarGoose)]
        if len(war_geese) == 0 or len(self.players) == 0:
            logger.info("Пока нет WarGoose или игроков")
            return

        goose = random.choice(war_geese)
        random_player_index = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(random_player_index)
        stolen = goose.attack(player)

        logger.info(f"{stolen}")
        self.balance[player.name] = player.balance

    def event_goose_super_honk(self):
        honk_geese = [g for g in self.geese if isinstance(g, HonkGoose)]
        if len(honk_geese) == 0 or len(self.players) == 0:
            logger.info("Пока нет HonkGoose или игроков")
            return

        goose = random.choice(honk_geese)
        special_goose = goose.super_honk(self.players)
        logger.info(f"{special_goose}")
        # обновляем balance казино после super_honk
        for p in self.players:
            self.balance[p.name] = p.balance

    def event_steal(self):
        if len(self.geese) == 0 or len(self.players) == 0:
            logger.info("Пока нет гусей или игроков")
            return

        goose = random.choice(self.geese)
        random_player_index = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(random_player_index)

        stolen = random.randint(1, 20)
        player.change_balance(-stolen)

        logger.info(f"{goose.name} крадёт {stolen}$ у {player.name}")
        self.balance[player.name] = player.balance

    def simulate_step(self):
        events = [
            self.event_player_bet,
            self.event_player_win,
            self.event_goose_attack,
            self.event_goose_super_honk,
            self.event_steal,
        ]
        random.choice(events)()
