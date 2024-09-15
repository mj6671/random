import qrcode
s=input("enter the link:")   
qr_img = qrcode.make(s)   
qr_img.save("qr-img.jpg") 
