
import simpy
import statistics
import random


class ExchangeMarket:
    def __init__(self, initialPrice: int, totalVendors: int, totalBuyers: int, speculators: int, desperate: int, normal: int) -> None:
        self.initialPrice = initialPrice
        self.currentPrice = initialPrice
        self.totalVendors = totalVendors
        self.totalBuyers = totalBuyers
        self.speculators = speculators
        self.desperate = desperate
        self.normal = normal
        self.sellOffers = []    
        self.buyOffers = []

    
    def get_mean(self):
        sellMean  = statistics.mean(self.sellOffers)
        # buyMean = statistics.mean(self.buyOffers)
        return sellMean
    

    def get_mode(self):
        sellMode = statistics.mode(self.sellOffers)
        # buyMode = statistics.mode(self.buyOffers)
        return sellMode


    def get_median(self):
        sellMedian = statistics.mean(self.sellOffers)
        # buyMedian = statistics.mean(self.buyOffers)
        return sellMedian


    def get_sell_offers_queue(self):
        speculators = [0 for i in range(self.speculators)]
        desperatePeople = [1 for i in range(self.desperate)]
        normalPeople = [2 for i in range(self.normal)]
        queue = speculators + desperatePeople + normalPeople
        random.shuffle(queue)
        return queue 


    def assign_offer(self, index):
        if index == 0:
            speculation = int(self.currentPrice * random.randint(1,5) / 100)
            # print("SPECULATION")
            # print(speculation)
            return self.currentPrice + speculation
        
        if index == 1:
            desperation = int(self.currentPrice * random.randint(1,5) / 100)
            return self.currentPrice - desperation

        return self.currentPrice


    def publish_sell_offers(self):
        self.sellOffers = []
        sellQueue = self.get_sell_offers_queue()
        for x in sellQueue:
            offer = self.assign_offer(x)
            self.sellOffers.append(offer)

    
    def simulate_market(self, days: int):
        registry = []
        for i in range(days):
            x=0
            while(x<2):
                self.publish_sell_offers()
                sell_median = self.get_median()
                self.currentPrice = sell_median
                registry.append(self.currentPrice)
                x+=1
        return registry





market = ExchangeMarket(24, 1000, 400, 375, 275, 350)
result = market.simulate_market(500)
print(result)
print('/n')



        



