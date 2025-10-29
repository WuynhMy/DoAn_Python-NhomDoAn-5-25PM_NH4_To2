import tkinter as tk 
from tkinter import ttk, messagebox 
from tkcalendar import DateEntry 
import mysql.connector 
 
# ====== Kết nối MySQL ====== 
def connect_db(): 
    return mysql.connector.connect( 
        host="localhost", 
        user="root",        # thay bằng user MySQL của bạn 
        password="2703",        # thay bằng password MySQL của bạn 
        database="QLBN" 
    ) 