from tkinter import *
from tkinter import ttk, messagebox  #theme เพื่อความสวยงาม
GUI = Tk()  #เรียกใช้งานฟังก์ชั่น Tk
GUI.geometry('800x600')   # ขนาดหน้าจอ คำสั่งเหมือน Tk().geometry
GUI.title('โปรแกรมคำนวณค่าผลไม้') # Title หน้าจอ

#แทรกรูป
file = PhotoImage(file = 'watermelon.png')
IMG = Label(GUI, image=file , text='')
IMG.pack()

L1 = Label(GUI, text = 'โปรแกรมคำนวณค่าแตงโม', font = ('Angsana New',30,'bold')) # text1 กำหนดลง L1
L1.pack() #วางลงบนหน้าจอ

L2 = Label(GUI, text = 'กรุณากรอกน้ำหนักแตงโม : กิโลกรัมละ 20 บาท', font = ('Angsana New',20)) # text2 กำหนดลง L2
L2.pack() #วางลงบนหน้าจอ

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลจำนวนที่มาจาก ช่องกรอก
E1 = ttk.Entry(GUI, textvariable = v_quantity, font = ('impact', 25))    #ช่องกรอก ttk. คือการใช้ theme
E1.pack()

def Calculate():
    quantity = v_quantity.get() #.get คือ รับข้อมูลจากช่องนี้มา
    price = 20
    print('จำนวน', float(quantity)* price , 'บาท')
    cal = float(quantity) * price
    # โชว์เป็น alertbox
    messagebox.showinfo('ยอดเงินที่ต้องชำระ','แตงโมน้ำหนัก {} กิโลกรัม ราคาทั้งหมด : {:,.2f} บาท'.format(quantity, cal))


B1 = ttk.Button(GUI, text='คำนวณ', command = Calculate) #ปุ่ม คำนวณ + ใส่ฟังก์ชั่นคำนวณ ที่เราสร้างไว้
B1.pack(ipadx=30, ipady=20, pady=20) #วาง + ipad = internal padding ขอบในถึงตัวอักษร / pad = pad นอก





GUI.mainloop() #สั่งให้รันตลอดกาล