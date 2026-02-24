import qrcode

#Taking UPI id as a Input 
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can Modify these URLs based on the payment apps you want to support 
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR code for each Payment app
googlepay_qr = qrcode.make(googlepay_url)

#Save the QR code to Image file(optional) 
googlepay_qr.save('googlepay_qr.png')

#Display The Qr codes (use Pillow Library)
googlepay_qr.show()