from django.db import models

# Create your models here.

class fitness_programs(models.Model):
   name = models.CharField(max_length=100, default='')
   key_focus = models.TextField()
   #week 1
   day1 = models.CharField(max_length=255, default='')
   day2 = models.CharField(max_length=255, default='')
   day3 = models.CharField(max_length=255, default='')
   day4 = models.CharField(max_length=255, default='')
   day5 = models.CharField(max_length=255, default='')
   day6 = models.CharField(max_length=255, default='')
   day7 = models.CharField(max_length=255, default='')
   #week 2
   day8 = models.CharField(max_length=255, default='')
   day9 = models.CharField(max_length=255, default='')
   day10 = models.CharField(max_length=255, default='')
   day11 = models.CharField(max_length=255, default='')
   day12 = models.CharField(max_length=255, default='')
   day13 = models.CharField(max_length=255, default='')
   day14 = models.CharField(max_length=255, default='')
   # week 3
   day15 = models.CharField(max_length=255, default='')
   day16 = models.CharField(max_length=255, default='')
   day17 = models.CharField(max_length=255, default='')
   day18 = models.CharField(max_length=255, default='')
   day19 = models.CharField(max_length=255, default='')
   day20 = models.CharField(max_length=255, default='')
   day21 = models.CharField(max_length=255, default='')
   # week 4
   day22 = models.CharField(max_length=255, default='')
   day23 = models.CharField(max_length=255, default='')
   day24 = models.CharField(max_length=255, default='')
   day25 = models.CharField(max_length=255, default='')
   day26 = models.CharField(max_length=255, default='')
   day27 = models.CharField(max_length=255, default='')
   day28 = models.CharField(max_length=255, default='')
   # week 5
   day29 = models.CharField(max_length=255, default='')
   day30 = models.CharField(max_length=255, default='')
   day31 = models.CharField(max_length=255, default='')
   day32 = models.CharField(max_length=255, default='')
   day33 = models.CharField(max_length=255, default='')
   day34 = models.CharField(max_length=255, default='')
   day35 = models.CharField(max_length=255, default='')
   #week 6
   day36 = models.CharField(max_length=255, default='')
   day37 = models.CharField(max_length=255, default='')
   day38 = models.CharField(max_length=255, default='')
   day39 = models.CharField(max_length=255, default='')
   day40 = models.CharField(max_length=255, default='')
   day41 = models.CharField(max_length=255, default='')
   day42 = models.CharField(max_length=255, default='')
   #week 7
   day43 = models.CharField(max_length=255, default='')
   day44 = models.CharField(max_length=255, default='')
   day45 = models.CharField(max_length=255, default='')
   day46 = models.CharField(max_length=255, default='')
   day47 = models.CharField(max_length=255, default='')
   day48 = models.CharField(max_length=255, default='')
   day49 = models.CharField(max_length=255, default='')
   #week 8
   day50 = models.CharField(max_length=255, default='')
   day51 = models.CharField(max_length=255, default='')
   day52 = models.CharField(max_length=255, default='')
   day53 = models.CharField(max_length=255, default='')
   day54 = models.CharField(max_length=255, default='')
   day55 = models.CharField(max_length=255, default='')
   day56 = models.CharField(max_length=255, default='')
   #week 9
   day57 = models.CharField(max_length=255, default='')
   day58 = models.CharField(max_length=255, default='')
   day59 = models.CharField(max_length=255, default='')
   day60 = models.CharField(max_length=255, default='')
   day61 = models.CharField(max_length=255, default='')
   day62 = models.CharField(max_length=255, default='')
   day63 = models.CharField(max_length=255, default='')
   #week 10
   day64 = models.CharField(max_length=255, default='')
   day65 = models.CharField(max_length=255, default='')
   day66 = models.CharField(max_length=255, default='')
   day67 = models.CharField(max_length=255, default='')
   day68 = models.CharField(max_length=255, default='')
   day69 = models.CharField(max_length=255, default='')
   day70 = models.CharField(max_length=255, default='')
   #week 11
   day71 = models.CharField(max_length=255, default='')
   day72 = models.CharField(max_length=255, default='')
   day73 = models.CharField(max_length=255, default='')
   day74 = models.CharField(max_length=255, default='')
   day75 = models.CharField(max_length=255, default='')
   day76 = models.CharField(max_length=255, default='')
   day77 = models.CharField(max_length=255, default='')
   #week 12
   day78 = models.CharField(max_length=255, default='')
   day79 = models.CharField(max_length=255, default='')
   day80 = models.CharField(max_length=255, default='')
   day81 = models.CharField(max_length=255, default='')
   day82 = models.CharField(max_length=255, default='')
   day83 = models.CharField(max_length=255, default='')
   day84 = models.CharField(max_length=255, default='')
   #additional columns
   level = models.CharField(max_length=20, default='')      
   price = models.PositiveSmallIntegerField()
   
   

    
   def __str__(self):
        return '%s %s' % (self.name, self.price) 
