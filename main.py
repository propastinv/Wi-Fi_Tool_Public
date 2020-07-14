from settings import *
from imports import *


root = Tk()
# root.attributes('-alpha', 0.9)
root.title("PointChecker v1.6 Beta")
root.geometry("810x460")
root.resizable(False, False)
root.iconbitmap('src/supericon.ico')


def open_browser(Point_third_octet,Point_fourth_octet):
     if Point_third_octet.get() and Point_fourth_octet.get():
          host = "10.110." + Point_third_octet.get() + '.' + Point_fourth_octet.get()
          text2.insert(1.0, host + '\n')
          point = Selenium_chromedriver(host)
          point.open()
          point.authorize()
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")

def open_browser_sector(Sector_third_octet,Sector_fourth_octet,Sector_selector):

     if Sector_third_octet.get() and Sector_fourth_octet.get():
          host = "10.100." + Sector_third_octet.get() + '.' + Sector_fourth_octet.get()
          text2.insert(1.0, host + '\n')

          if Sector_selector.get() == "1":
               httpport = 8002
          if Sector_selector.get() == "2":
               httpport = 8003
          if Sector_selector.get() == "3":
               httpport = 8004
          if Sector_selector.get() == "4":
               httpport = 8005
          
          sector = (str(host) + ':' + str(httpport))
          sectordriver = Selenium_chromedriver(sector)
          sectordriver.open()
          sectordriver.authorize()
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")

def pingpoint(Ping_third_octet,Ping_fourth_octet,ping_count,minustvar):
     if Point_third_octet.get() and Point_fourth_octet.get():
          count = ping_count.get()
          host = "10.110." + Point_third_octet.get() + '.' + Point_fourth_octet.get()
          text2.insert(1.0, host + '\n')
          if minustvar.get() == True:
               response = os.system("ping -t" + ' ' + host)
          else:
               response = os.system("ping -n " + count + ' ' + host)
          if response == 0:
               text.insert(1.0, (host +  ' is up!' + '\n' + '-----------------------------------------------------------------------' + '\n'))
          else:
               text.insert(1.0, (host +  ' is down!' + '\n' + '----------------------------------------------------------------------' + '\n'))
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")

def pingsector(Sector_third_octet,Sector_fourth_octet,ping_count,minustvar):
     if Sector_third_octet.get() and Sector_fourth_octet.get():
          count = ping_count.get()
          host = "10.100." + Sector_third_octet.get() + '.' + Sector_fourth_octet.get()
          text2.insert(1.0, host + '\n')
          if minustvar.get() == True:
               response = os.system("ping -t" + ' ' + host)
          else:
               response = os.system("ping -n " + count + ' ' + host)
          if response == 0:
               text.insert(1.0, (host +  ' is up!' + '\n' + '-----------------------------------------------------------------------' + '\n'))
          else:
               text.insert(1.0, (host +  ' is down!' + '\n' + '----------------------------------------------------------------------' + '\n'))
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")


def reboot(Point_third_octet,Point_fourth_octet):
     host = "10.110." + Point_third_octet.get() + '.' + Point_fourth_octet.get()
     user = UBNT_LOGIN
     secret = UBNT_PASSWORD
     port = 22
     command = 'reboot'
     success = ("success reboot device!")
     error = ("error reboot device!" )
     if Point_third_octet.get() and Point_fourth_octet.get():
          text2.insert(1.0, host + '\n')
          answer = mb.askyesno(title="Warning", message=("Reboot device " + host + "?"))
          CREATE_NO_WINDOW = 0x08000000
          response = subprocess.call("ping -n 1 " + host, creationflags=CREATE_NO_WINDOW)
          if answer == True:
               if response == 0:
                    reboot = Paramiko_SSH(host,user,secret,port,command)
                    reboot.execute()
                    reboot.close_connect()
                    text.insert(1.0, (host  + ' ' + success + '\n' + '----------------------------------------------------------------------' + '\n')) 
               else:
                    text.insert(1.0, (host  + ' ' + error + '\n'  + '-----------------------------------------------------------------------' + '\n'))   
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")


def reboot_sector(Sector_third_octet,Sector_fourth_octet,Sector_selector):
          host = "10.100." + Sector_third_octet.get() + '.' + Sector_fourth_octet.get()
          user = UBNT_LOGIN
          secret = UBNT_PASSWORD
          if Sector_selector.get() == "1":
               port = 2222
          if Sector_selector.get() == "2":
               port = 2223
          if Sector_selector.get() == "3":
               port = 2224
          if Sector_selector.get() == "4":
               port = 2225
          command = 'reboot'
          success = ("success reboot device!")
          error = ("error reboot device!" )
          if Sector_third_octet.get() and Sector_fourth_octet.get():
               text2.insert(1.0, host + '\n')
               answer = mb.askyesno(title="Warning", message=("Reboot device " + host + "?"))
               response = 0
               if answer == True:
                    if response == 0:
                         reboot = Paramiko_SSH(host,user,secret,port,command)
                         reboot.execute()
                         reboot.close_connect()
                         text.insert(1.0, (host  + ' ' + success + '\n' + '----------------------------------------------------------------------' + '\n')) 
                    else:
                         text.insert(1.0, (host  + ' ' + error + '\n'  + '-----------------------------------------------------------------------' + '\n'))   
          else:
               mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the sector!")


def SpeedTest(message):
     mb.showerror("Error!", "This functionality is under development!")
     # host = ("10.110." + message.get())
     # if message.get():
     #      pass
     # elif not message.get():
     #      mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")



          

def check_point(Point_third_octet,Point_fourth_octet,var,event=None):
     host = "10.110." + Point_third_octet.get() + '.' + Point_fourth_octet.get()
     user = UBNT_LOGIN
     secret = UBNT_PASSWORD
     port = 22
     command = 'mca-status'
     success = ("Success connection to network nodes " + host + ' !' +  "\n")
     error = ("Error connection to network nodes " + host + ' !' +  "\n")
     if Point_third_octet.get() and Point_fourth_octet.get():
          text2.insert(1.0, host + '\n')
          CREATE_NO_WINDOW = 0x08000000
          response = subprocess.call("ping -n 1 -i 1 " + host, creationflags=CREATE_NO_WINDOW)
          if response == 0:
                    Ssh_get_parameters = Paramiko_SSH(host,user,secret,port,command)
                    datadecode = Ssh_get_parameters.execute()
                    datasplit = datadecode.split('\n') 
                    if var.get() == 1:
                         pointparameters = PrettyTable()
                         pointparameters.field_names = ['Key', 'Value','Unit of measure']
                         for n in datasplit:
                              if n.startswith('deviceName'):
                                   device = n.split(',')
                                   devicename_value = device[0].split('=')
                                   apMac_value = device[1].split('=')
                                   deviceplatform_value = device[3].split('=')

                              if n.startswith('signal'): 
                                   signal_value = n.split('=')
                                   
                              if n.startswith('ccq'):
                                   ccq_value = n.split('=')
                                   ccq_split_percent_value = (int(ccq_value[1]) / 10)

                              if n.startswith('freq'):
                                   freq_value = n.split('=')

                              if n.startswith('distance'): 
                                   distance_value = n.split('=')
                                   distance_split_percent_value = (int(distance_value[1]) / 1000)

                              if n.startswith('wlanTxRate'):
                                   wlanTxRate_value = n.split('=')

                              if n.startswith('wlanRxRate'):
                                   wlanRxRate_value = n.split('=')

                              if n.startswith('lanSpeed'):

                                   landifspeed = n.split('=')
                                   if landifspeed == "Unplugged":
                                        lanSpeed_value = "Unplugged"
                                        
                                   else:
                                        lanSpeed_value0 = landifspeed[1].split('M')
                                        lanSpeed_value = lanSpeed_value0[0]


                              if n.startswith('uptime'):
                                   uptime_value = n.split('=')
                                   uptime_split_percent_value = float('{:.3f}'.format(int(uptime_value[1]) / 3600))

                              if n.startswith('latitude'):
                                   latitude = n.split('=')

                              if n.startswith('longitude'):
                                   longitude = n.split('=')
                                   

                         pointparameters.add_row(["Device name:", str(devicename_value[1]), 'str' ])
                         pointparameters.add_row(["Platform:", str(deviceplatform_value[1]), 'hardware type'])
                         pointparameters.add_row(["Signal:", int(signal_value[1]), 'dBm'])
                         pointparameters.add_row(["CCQ:", float(ccq_split_percent_value), '%'])
                         pointparameters.add_row(["Frequency:", int(freq_value[1]), 'mHz'])
                         pointparameters.add_row(["Distance:", float(distance_split_percent_value), 'kilometers'])
                         pointparameters.add_row(["Wlan Tx Rate:", float(wlanTxRate_value[1]), 'Mbps'])
                         pointparameters.add_row(["Wlan Rx Rate:", float(wlanRxRate_value[1]),'Mbps'])
                         pointparameters.add_row(["Uptime:", float(uptime_split_percent_value), 'hours'])
                         lat = re.search(r'\d{2}.\d{4,6}', latitude[1]) 
                         long = re.search(r'\d{2}.\d{4,6}', longitude[1]) 
                         if lat and long:    
                              latitude_value = lat[0]
                              longitude_value = long[0]
                              address = reverse_geocode(latitude_value,longitude_value)
                              address_split = address.split(',')
                              pointparameters.add_row(["latitude/Longitude:", str(latitude_value ), str(longitude_value )])
                              pointparameters.add_row(["Address:", ' ', 'str'])
                              for i in address_split:
                                  pointparameters.add_row([" ", (i.replace(' ','') + ','), 'str'])
                         else:
                              pointparameters.add_row(["latitude/Longitude:", 'None', 'None'])
                              pointparameters.add_row(["Address:", 'None', 'str'])


                         if lanSpeed_value.isdigit():
                              pointparameters.add_row(["Lan speed:", int(lanSpeed_value), 'Mbps'])
                         else:
                              pointparameters.add_row(["Lan speed:", "Unplugged", 'Mbps'])
                         

                         pointparameters.add_row(["Mac address:",(str(apMac_value[1]) + ' '), 'str'])
                         pointparameters.align = 'l'

                         text.insert(1.0,success  + str(pointparameters) + '\n')
                         Ssh_get_parameters.close_connect()
                    elif var.get() == 0:
                         pointparameters = PrettyTable()
                         pointparameters.field_names = ['Key', 'Value', 'Unit of measure']
                         for n in datasplit:
                              if n.startswith('deviceName'):
                                   device = n.split(',')
                                   devicename_value = device[0].split('=')
                                   deviceplatform_value = device[3].split('=')

                              if n.startswith('signal'): 
                                   signal_value = n.split('=')

                              if n.startswith('ccq'):
                                   ccq_value = n.split('=')
                                   ccq_split_percent_value = (int(ccq_value[1]) / 10)

                         pointparameters.add_row(["Device name:", str(devicename_value[1]), 'str' ])
                         pointparameters.add_row(["Signal:", int(signal_value[1]), 'dBm'])
                         pointparameters.add_row(["CCQ:", float(ccq_split_percent_value), '%'])
                         pointparameters.align = 'l'
                         text.insert(1.0,success  + str(pointparameters) + '\n')
                         Ssh_get_parameters.close_connect()
                         
          else:
               text.insert(1.0, (host +  ' is down!' + '\n' + '----------------------------------------------------------------------' + '\n' + error))
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")
          

def check_sector(Sector_third_octet,Sector_fourth_octet,Sector_selector):
     host = "10.100." + Sector_third_octet.get() + '.' + Sector_fourth_octet.get()
     user = UBNT_LOGIN
     secret = UBNT_PASSWORD
     text2.insert(1.0, host + '\n')
     # host = "192.168." + Sector_third_octet.get() + '.' + Sector_fourth_octet.get()
     # user = 'artem'
     # secret = 'madenci'
     if Sector_selector.get() == "1":
          port = 2222
     if Sector_selector.get() == "2":
          port = 2223
     if Sector_selector.get() == "3":
          port = 2224
     if Sector_selector.get() == "4":
          port = 2225

     command = 'wstalist'
     success = ( "\n" + "Success connection to network nodes " + host + ' !' +  "\n")
     error = ("Error connection to network nodes " + host + ' !' +  "\n")
     if Sector_third_octet.get() and Sector_fourth_octet.get():
          response = 0
          if response == 0:
               text.insert(1.0,success + '\n')
               Ssh_get_parameters_sector = Paramiko_SSH(host,user,secret,port,command)
               datadecode = Ssh_get_parameters_sector.execute()
               json_data = json.loads(datadecode)
               sectorparameters = PrettyTable()
               sectorparameters.field_names = ['MAC address', 'Device name','Signal','Distance','TX latency']
               for sector in json_data:
                    sectorparameters.add_row([str(sector['mac']), str(sector['remote']['hostname']), str(sector['remote']['signal']),str(sector['distance']),str(sector['remote']['tx_latency']) ])
                    text.insert(1.0,str(sectorparameters))
          else:
               text.insert(1.0, (host +  ' is down!' + '\n' + '----------------------------------------------------------------------' + '\n' + error))
     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the sector point!")      

def ubntpass():
     pyperclip.copy('04874311')    


def testpass():
     pyperclip.copy('testtest') 


def rootpass():
     pyperclip.copy('mbrbbashpd2000')


def atelpass():
     pyperclip.copy('gP^JevrIcLRXq')


def freq():
     pyperclip.copy('5250,5255,5260,5265,5270,5275,5280,5285,5290,5295,5300,5305,5310,5315,5320,5325,5330,5335,5340,5345,5350,5560,5580,5740,5745,5750,5755,5760,5765,5770,5775,5780,5785,5790,5795,5800,5805,5810,5815,5820,5825,5830,5835,5840')

def routeros():
     pyperclip.copy('0487430184')  

def enable_compliance_test(Point_third_octet,Point_fourth_octet):
     host = "10.110." + Point_third_octet.get() + '.' + Point_fourth_octet.get()
     user = UBNT_LOGIN
     secret = UBNT_PASSWORD
     text2.insert(1.0, host + '\n')
     port = 22
     enablect = 'enable_ct && cfgmtd -f /tmp/system.cfg -w'

     if Point_third_octet.get() and Point_third_octet.get():
          EnableCT = Paramiko_SSH(host,user,secret,port,enablect)
          b = EnableCT.execute()
          text.insert(1.0, b)
          EnableCT.close_connect()

     else:
          mb.showerror("Error!", "Please enter the last 2 octets of the IP address of the access point!")

def delete_all_form():
    text.delete(1.0, END)









Point_third_octet = StringVar()
Point_fourth_octet = StringVar()


Ip3 = Entry(textvariable=Point_third_octet, width=6)
Ip3.grid(row=0, column=2, sticky="w",padx="1", pady="1")

Ip4 = Entry(textvariable=Point_fourth_octet, width=6)
Ip4.grid(row=0, column=3, sticky="w",padx="1", pady="1")


Sector_third_octet = StringVar()
Sector_fourth_octet = StringVar()

Ip3Sector = Entry(textvariable=Sector_third_octet, width=6)
Ip3Sector.grid(row=1,column=2, sticky="w",padx="1", pady="1")

Ip4Sector = Entry(textvariable=Sector_fourth_octet, width=6)
Ip4Sector.grid(row=1,column=3, sticky="w",padx="1", pady="1")


var = IntVar()
var.set(0)


Minimal = Radiobutton(text="Min", variable=var, value=0)
Minimal.grid(row=2,column=1, padx=1, pady=1, sticky="w")


Advanced = Radiobutton(text="Adv", variable=var, value=1)
Advanced.grid(row=2,column=2, padx=1, pady=1, sticky="w")


PointIP = Label(text="Point:",font='Helvetica 9 bold')
PointIP.grid(row=0, column=0, sticky="w",padx="2", pady="5")


PointIPLabel = Label(text="10.110. + ",font='Helvetica 9 bold')
PointIPLabel.grid(row=0, column=1, sticky="w",padx="2", pady="5")


Get_button = Button(text="Get",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(check_point,Point_third_octet,Point_fourth_octet,var))
Get_button.grid(row=0,column=4, padx=5, pady=10, sticky="w")
root.bind('<Return>', partial(check_point,Point_third_octet,Point_fourth_octet,var))


ping_count_label = Label(text="Ping pack:",font='Helvetica 7 bold')
ping_count_label.grid(row=2, column=5, sticky="w",padx="2", pady="2")
ping_count = Spinbox(width=4, from_=15, to=30)
ping_count.grid(row=2, column=6)


# t = threading.Thread(target=pingpoint, name="Thread1", args=(message,ping_count))

# SpeedTest_button = Button(text="SpeedTest",background="#555", foreground="#ccc",height = 0, width = 11, command=partial(SpeedTest,message))
# SpeedTest_button.grid(row=0,column=7, padx=5, pady=10, sticky="w")


Clear_button = Button(text="ClLog",background="#CCF7F5", foreground="#555",height = 0, width = 6, command=delete_all_form)
Clear_button.grid(row=2,column=4, padx=5, pady=10, sticky="w")

Browser_button = Button(text="Browser",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(open_browser,Point_third_octet,Point_fourth_octet))
Browser_button.grid(row=0,column=6, padx=5, pady=10, sticky="w")

Reboot_button = Button(text="Reboot Point",background="#7d4845", foreground="#ccc",height = 0, width = 10, command=partial(reboot,Point_third_octet,Point_fourth_octet))
Reboot_button.grid(row=0,column=8, padx=5, pady=10, sticky="w")

minustvar = BooleanVar()
minustvar.set(0)
minustvarbutton = Checkbutton(text="-t", variable=minustvar, onvalue=1, offvalue=0)
minustvarbutton.grid(row=2,column=8, padx=5, pady=10, sticky="w")

Ping_button = Button(text="Ping",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(pingpoint,Point_fourth_octet,Point_fourth_octet,ping_count,minustvar))
Ping_button.grid(row=0,column=5, padx=5, pady=10, sticky="w")

Log = Label(text="Log:",font='Helvetica 7 bold')
Log.grid(row=2, column=0, sticky="w",padx="5", pady="5")


Owner = Label(text="achelak@it.od.ua | +380487877187 | Artem Chelak - senior pzdbol++ software engineer!",font='Helvetica 7 bold')
Owner.grid(row=6, column=1, columnspan=7, rowspan=1,padx=5, sticky=E+W+S+N)


History = Label(text="History:",font='Helvetica 7 bold')
History.grid(row=2, column=11, sticky="w",padx="5", pady="5")


text = Text(bg="#FFFFFF", width=30, height=23, fg='black',font='consolas 8 bold')
text.grid(row=3, column=0, columnspan=11, rowspan=2,padx=5, sticky=E+W+S+N)

text2 = Text(bg="#FFFFFF", width=14, height=16, fg='black',font='Helvetica 8 bold')
text2.grid(row=3, column=11, columnspan=2, rowspan=2,padx=5, sticky=E+W+S+N)


Sector_selector = Spinbox(width=5, from_=1, to=4)
Sector_selector.grid(row=2,column=10, padx=1, pady=1, sticky="w")
Sector_label = Label(text="Sector(a,b,g,z):",font='Helvetica 7 bold')
Sector_label.grid(row=2,column=9, padx=1, pady=1, sticky="w")


SectorIP = Label(text="Sector:",font='Helvetica 9 bold')
SectorIPLabel = Label(text="10.100. + ",font='Helvetica 9 bold')
SectorIP.grid(row=1,column=0, padx=1, pady=1, sticky="w")
SectorIPLabel.grid(row=1,column=1, padx=1, pady=1, sticky="w")


GetSector = Button(text="Get",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(check_sector,Sector_third_octet,Sector_fourth_octet,Sector_selector))
GetSector.grid(row=1,column=4, padx=5, pady=10, sticky="w")

Reboot_sector_button = Button(text="Reboot Sector",background="#7d4845", foreground="#ccc",height = 0, width = 10, command=partial(reboot_sector,Sector_third_octet,Sector_fourth_octet,Sector_selector))
Reboot_sector_button.grid(row=1,column=8,columnspan=1, padx=5, pady=10, sticky="w")

Browser_button_sector = Button(text="Browser",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(open_browser_sector,Sector_third_octet,Sector_fourth_octet,Sector_selector))
Browser_button_sector.grid(row=1,column=6, padx=5, pady=10, sticky="w")

Ping_button_sector = Button(text="Ping",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(pingsector,Sector_third_octet,Sector_fourth_octet,ping_count,minustvar))
Ping_button_sector.grid(row=1,column=5, padx=5, pady=10, sticky="w")


Ubntpass_button = Button(text="048",background="#555", foreground="#ccc",height = 0, width = 6, command=ubntpass)
Ubntpass_button.grid(row=0, column=10, padx=5, pady=10, sticky="w")

Testpass_button = Button(text="test",background="#555", foreground="#ccc",height = 0, width = 6, command=testpass)
Testpass_button.grid(row=0, column=11, padx=5, pady=10, sticky="w")

Freq_button = Button(text="freq",background="#555", foreground="#ccc",height = 0, width = 6, command=freq)
Freq_button.grid(row=0, column=12, padx=5, pady=10, sticky="w")

Rootpass_button = Button(text="root",background="#555", foreground="#ccc",height = 0, width = 6, command=rootpass)
Rootpass_button.grid(row=1, column=11, padx=5, pady=10, sticky="w")

Atelpass_button = Button(text="atel",background="#555", foreground="#ccc",height = 0, width = 6, command=atelpass)
Atelpass_button.grid(row=1, column=12, padx=5, pady=10, sticky="w")

Mikrotik_button = Button(text="rOS",background="#555", foreground="#ccc",height = 0, width = 6, command=routeros)
Mikrotik_button.grid(row=1, column=10, padx=5, pady=10, sticky="w")

Compliance_test = Button(text="enCT",background="#555", foreground="#ccc",height = 0, width = 6, command=partial(enable_compliance_test,Point_third_octet,Point_fourth_octet))
Compliance_test.grid(row=2, column=12, sticky="w",padx="5", pady="5")


root.mainloop()


