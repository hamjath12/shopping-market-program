import re
import smtplib
import datetime

print("***welcome department store***")
print("->menu_card \n cooking_item-> rice,sugar,salt,oil \n cooking_powder-> rasam,sambar,Garam masala,Pepper \n cleaning_product-> surf,soap,comfort,harpic,paste")


one_rice=1200
one_sugar=60
one_oil=100
one_maida=90
one_salt=20
one_rasam=20
one_sambar=20
one_garam_masala=20
one_pepper=20
one_surf=120
one_soap=30
one_harpic=80
one_comfort=90
one_paste=100

def shopping_market():
    date_time=datetime.datetime.now()

    f=open("name_list.py","r")
    name=f.read()

    your_order=input("enter your order:").lower()
    x=re.search(your_order,name)
    print(x)
    if x:
        print(f"->your order {your_order} is available ")
    else:
        print(f"{your_order} is not available")
        
    try:
        how_many=int(input(f"how many you want {your_order} :"))
        if your_order=="rice":
            total=one_rice*how_many
        elif your_order=="sugar":
            total=one_sugar*how_many
        elif your_order=="salt":
            total=one_salt*how_many
        elif your_order=="oil":
            total=one_oil*how_many
        elif your_order=="sambar":
            total=one_sambar*how_many
        elif your_order=="rasam":
            total=one_rasam*how_many
        elif your_order=="garam masala":
            total=one_garam_masala*how_many
        elif your_order=="pepper":
            total=one_pepper*how_many
        elif your_order=="surf":
            total=one_surf*how_many
        elif your_order=="soap":
            total=one_soap*how_many
        elif your_order=="comfort":
            total=one_comfort*how_many
        elif your_order=="harpic":
            total=one_harpic*how_many
        elif your_order=="paste":
            total=one_paste*how_many
        else:
            print("invalid value")
            

        if total>0 :
            gst_bill=(10/100)*total
            total_bill=total+gst_bill
        
            try:
                customer_mail=input("enter your e-mail :").strip()
                receiver_mail=[customer_mail]
                for i in receiver_mail:
                    s=smtplib.SMTP('smtp.gmail.com',587)
                    s.starttls()
                    s.login("mohammedhamjath.24@gmail.com","tnnv ogaz gpjy iyik")
                    message=(f"your bill is {total} and include gst bill is {gst_bill} and total {total_bill}\n {date_time}")
                    s.sendmail("mohammedhamjath.24@gmail.com",i,message)
                    s.quit()
                        
                    print("->mail sent successfully")
                    print(f"->your bill is {total} and include gst bill is {gst_bill} and total {total_bill}\n {date_time}")
        
            except:
                print("mail not sent???")
        else:
            print("try again")   
    except:
        print("type only number !!!")
shopping_market()






