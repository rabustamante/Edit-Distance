# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 7-unit test
Date of last modification: 12/02/2019
Purpose of program:test edit_distance.py file with hard code strings
"""
from edit_distance import edit_distance
import time
def main():
    start_time = time.time()
    print("min number of steps:",edit_distance('miner','money'))
    print('time:', (time.time()-start_time))
    
    start_time2 = time.time()
    print("min number of steps:",edit_distance('a', ''))
    print('time:', (time.time()-start_time2))
    
    start_time3 = time.time()
    print("min number of steps:",edit_distance('turn', 'ta'))
    print('time:', (time.time()-start_time3))
    
    start_time4 = time.time()
    print("min number of steps:",edit_distance('cat','Dogggz'))
    print('time:', (time.time()-start_time4))
    
    start_time5 = time.time()
    print("min number of steps:",edit_distance('zzz', 'sleepz'))
    print('time:', (time.time()-start_time5))
    
    start_time6 = time.time()
    print("min number of steps:",edit_distance('xzyzyzabc', 'y'))
    print('time:', (time.time()-start_time6))
    
    start_time7 = time.time()
    print("min number of steps:",edit_distance('albertsons','walmart'))
    print('time:', (time.time()-start_time7))
    
    start_time8 = time.time()
    print("min number of steps:",edit_distance('bye', 'hellworld'))
    print('time:', (time.time()-start_time8))
    
    start_time9 = time.time()
    print("min number of steps:",edit_distance('time', 'money'))
    print('time:', (time.time()-start_time9))
    
    start_time10 = time.time()
    print("min number of steps:",edit_distance('" "', '" "'))
    print('time:', (time.time()-start_time10))
main()