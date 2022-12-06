import smtplib, ssl

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	sender_email = "testpirrandi1728@gmail.com"
	password = "qldrqsfgtyxcvtif"
	receiver_email = "testpirrandi1728@gmail.com"

	context = ssl.create_default_context()

	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.ehlo() 
	    server.starttls(context=context) 
	    server.ehlo()
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)
	    print('Correo enviado con exito')
    
	except Exception as e:
	    print(e)
     
	finally:
	    server.quit()