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
        """Регистрация игрока"""
        p = Player(name, initial_balance)
        self.players.add(p)
        self.balance[p.name] = p.balance
        return p

    def register_goose(self, goose: Goose) -> Goose:
        """Регистрация гуся"""
        self.geese.add(goose)
        logger.info(f"Добавлен гусь '{goose.name}' (тип={goose.__class__.__name__}, honk={goose.honk_volume})")
        return goose

    def event_player_bet(self):
        """Игрок делает ставку"""
        if len(self.players) == 0:
            logger.info("Пока нет игроков")
            return

        idx = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(idx)
        bet = random.randint(5, 50)

        player.change_balance(-bet)

        logger.info(f"{player.name} делает ставку {bet}$")
        self.balance[player.name] = player.balance

    def event_player_win(self):
        """Игрок победил"""
        if len(self.players) == 0:
            logger.info("Пока нет игроков")
            return

        idx = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(idx)
        win = random.randint(0, 100)

        player.change_balance(win)

        logger.info(f"{player.name} выигрывает {win}$")
        self.balance[player.name] = player.balance

    def event_goose_attack(self):
        """Гусь атакует"""
        war_geese = [g for g in self.geese if isinstance(g, WarGoose)]
        if len(war_geese) == 0 or len(self.players) == 0:
            logger.info("Пока нет WarGoose или игроков")
            return

        goose = random.choice(war_geese)
        idx = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(idx)

        damage = goose.attack(player)

        logger.info(f"{goose.name} атакует {player.name} и отнимает {damage}$!")
        self.balance[player.name] = player.balance

    def event_goose_super_honk(self):
        """Гусь громко кричит, все игроки теряют деньги"""
        honk_geese = [g for g in self.geese if isinstance(g, HonkGoose)]
        if len(honk_geese) == 0 or len(self.players) == 0:
            logger.info("Пока нет HonkGoose или игроков")
            return

        goose = random.choice(honk_geese)

        msg = goose.super_honk(self.players)
        logger.info(msg)

        for p in self.players:
            self.balance[p.name] = p.balance

    def event_steal(self):
        """Гусь крадёт деньги"""
        if len(self.geese) == 0 or len(self.players) == 0:
            logger.info("Пока нет гусей или игроков")
            return

        goose = random.choice(list(self.geese))
        idx = random.randint(0, len(self.players) - 1)
        player = self.players.get_by_index(idx)

        stolen = random.randint(1, 20)
        player.change_balance(-stolen)

        logger.info(f"{goose.name} крадёт {stolen}$ у {player.name}")
        self.balance[player.name] = player.balance

    def simulate_step(self):
        """Рандомно выбирает и запускает действие"""
        events = [
            self.event_player_bet,
            self.event_player_win,
            self.event_goose_attack,
            self.event_goose_super_honk,
            self.event_steal,
        ]
        random.choice(events)()
