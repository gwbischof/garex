import threading
from collections import defaultdict
from queue import PriorityQueue

class Company:

    def __init__(self, name, assets=100, liabilities=0, total_shares=100, public_shares=50):

        self.name = name

        # Assets are things the business owns, including cash.
        self.assets = assets

        # Liabilities are things the business owes,
        # incuding wages, and loans.
        self.liabilities = liabilities

        # Number of total shares.
        self.total_shares = total_shares

        # Number of shares.
        self.public_shares = public_shares

    @property
    def float(self):
        # Float is the number of public shares.
        return self.public_shares


class Trader:

    def __init__(self, name, account={'cash': 1000}):

        self.name = name

        # A dictionary that tracks how much of each stock the trader has.
        self._account = account

    def bid(self):
        pass

    def ask(self):
        pass

    def put(self, stock_name, num_shares):
        if self._account.get(stock_name):
            self._account[stock_name] += num_shares
        else:
            self._account[stock_name] = num_shares

    def get(self):
        pass


class Exchange:

    def __init__(self, traders={}):
        self._traders = traders
        self._bids = defaultdict(lambda : PriorityQueue())
        self._asks = defaultdict(lambda : PriorityQueue())
        self._running = True
        thread = threading.Thread(target=self._exchanger)
        thread.start()

    def stop(self):
        self._running = False

    def _exchanger(self):
        while _running:
            if self._bids.queue[0] >= (-1 * self._asks.queue[0]):

                if self._bids.queue[0][1]['num_shares'] < self._asks.queue[0][1]['num_shares']:
                    self._asks.queue[0][1]['numshares'] -= self._bids.queue[0][1]['num_shares']
                    bid = self._bids.get()
                    self._traders[bid['trader_name']].put(bid['stock_name'], bid['num_shares']
                elif self._bids.queue[0][1]['num_shares'] > self._asks.queue[0][1]['num_shares']:
                    self._bids.queue[0][1]['num_shares'] -= self._asks.queue[0][1]['num_shares']
                    ask = self._asks.get()
                    self._traders[id['trader_name']].put(bid['stock_name'], bid['num_shares']
                else:
                    bid = self._bids.get()
                    self._asks.get()
                    traders[bid[1]['name']


    def bid(self, trader_name, stock_name, num_shares):

    def ask(self, trader_name, stock_name, num_shares):

