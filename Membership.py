# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:21:48 2021

@author: yapto
"""
import sqlite3
import keyboard 
import colorama
from colorama import  Fore, Style
abc = True

conn=sqlite3.connect('C:\\Users\\yapto\\Desktop\\SQLiteDatabaseBrowserPortable\\Data\\membership.db')
conn.row_factory = sqlite3.Row
cur=conn.cursor()
cur.execute("select * from member")


print(f"{Style.BRIGHT}{Fore.RED}DT{Fore.GREEN}-{Fore.YELLOW}Apple{Fore.BLUE}Dog{Fore.MAGENTA}Outlet")
print(f"{Style.DIM}{Fore.WHITE}1.Member of CPBear")
print(f"{Style.DIM}{Fore.WHITE}2.Sign Up")
print(f"{Style.DIM}{Fore.WHITE}3.Database")
print(f"{Style.DIM}{Fore.WHITE}4.Exit")
print("\n")
running=True
while (running):
    if keyboard.is_pressed('1'):
        hp2 = input("Handphone number: ")
        newp = input("Payment: ")
        cur.execute('UPDATE member SET points=?/10+points WHERE hp=?', (newp , hp2))
        conn.commit()
        abc=True
    elif keyboard.is_pressed('2'):
        print("\n")
        print("Please fill in these info.")
        hp = input("Handphone no: ")
        name = input("Name: ")
        points = input("Payment: ")
        sql_str = "insert into member(hp, name, points) values('{}','{}',{}/10);".format(hp,name,points)
        conn.execute(sql_str)
        conn.commit()
        abc = True
    elif keyboard.is_pressed('3'):
        rows = cur.fetchall()
        hp3=input("HP: ")
        cur.execute("SELECT * FROM member WHERE hp='{}'".format(hp3))
        rows = cur.fetchall()
      
        print("{:25s} {:30s} {:5s}".format("Hp","Name","Points"))
        for row in rows:
            print("{:25s} {:30s} {:5d}".format(hp3, row['name'], row['points']))
        conn.commit()
        abc=True
    elif keyboard.is_pressed('4'):
        running =False 
else:
    print("\n")
    print('Shut Down.')
conn.close()