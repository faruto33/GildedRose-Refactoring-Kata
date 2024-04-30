# -*- coding: utf-8 -*-

# dictionnary to define age/quality update rule per item
age_quality = {
    'Aged Brie' : {100:'+1',0:'+2'},
    'Backstage passes' : {100:'+1',10:'+2',5:'+3',0:'*0'},
    'Conjured': {100:'-2',0:'-4'},
    # legendary item, defined integer value
    'Sulfuras' : {100:80,0:80},
    # default value
    '':{100:'-1',0:'-2'},
    # new item to add here
    #'Item.name' : { nb_days : quality_update_rule, ... },
    }

# max quality per item
min_quality = 0
# min quality per item
max_quality = 50

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # for each item do
        for item in self.items:
            # get item index in dictionnary
            index = [x for x in age_quality.keys() if x in item.name][0]
            # get related rule
            rule = age_quality[index][[dl for dl in age_quality[index] if item.sell_in <= dl][-1]]
            # if the rule is not an integer (not legendary item)
            if type(rule) == str:
                item.sell_in = item.sell_in - 1
                item.quality = min(max(eval(str(item.quality) + rule), min_quality), max_quality)
            # else the rule is an integer (a legendary item)
            else :
                item.quality = rule

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
