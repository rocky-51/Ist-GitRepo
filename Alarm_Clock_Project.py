import datetime,time,winsound

print("Cancel\t\tEDIT ALARM\t\tDone\n")
print("H:\t00\t01\t02...21\t\t22\t23")
print("M:\t00\t01\t02...57\t\t58\t59")
set_alarm=input("Input time in HH:MM:SS= ")
s_a=set_alarm.split(':')
while True:
    print(time.strftime('%H:%M:%S'))
    time.sleep(1)
    if(s_a[0]==time.strftime('%H') and s_a[1]==time.strftime('%M') and s_a[2]==time.strftime('%S')):
        print(time.strftime('\n%H:%M:%S'))
        time.sleep(1)
        print("TIME TO WAKE UP!!")
        break

