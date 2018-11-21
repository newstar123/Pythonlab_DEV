#!/usr/bin/env python
#coding:utf-8
#定义一个类来计算旅馆租房费用，包括所有州销售税和房税。

class HotelRoomCalc(object):
    'Hotel room rate calculator'
    def __init__(self, rt, sales=0.085, rm=0.1):
        '''HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

#San Francisco
sfo = HotelRoomCalc(299)
print 'San Francisco 1 day:', sfo.calcTotal()
print 'San Francisco 2 days:', sfo.calcTotal(2)

#Seattle
sea = HotelRoomCalc(189, 0.086, 0.058)
print 'Seattle 1 day:', sea.calcTotal()
print 'Seattle 4 days:', sea.calcTotal(4)

#Washington DC
wasWkDay = HotelRoomCalc(169, 0.045, 0.02)
wasWkEnd = HotelRoomCalc(119, 0.045, 0.02)
print 'Washinton DC 5 weekdays and 1 weekend:', wasWkDay.calcTotal(5) + wasWkEnd.calcTotal()


'''
运行结果：
San Francisco 1 day: 354.31
San Francisco 2 days: 708.62
Seattle 1 day: 216.22
Seattle 4 days: 864.88
Washinton DC 5 weekdays and 1 weekend: 1026.63
'''