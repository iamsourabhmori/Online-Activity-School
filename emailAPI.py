def sendMail(emailid,pwd,subject="",html=""):
#def sendMail(emailid,pwd,subject=""):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	
	me = "darkweb1.hack@gmail.com"
	you = emailid

	msg = MIMEMultipart('alternative')
	msg['From'] = me
	msg['To'] = you

	if subject=="registration confirmation":
		msg['Subject'] = "Verification Mail RoomRent.com"
	else:
		msg['Subject'] = subject

	if html=="":
		html = """<html>
  					<head></head>
  					<body>
    					<h1>Rohit Sharma Your Account is Hacked Now 😃</h1>
    					<p>You have been successfully Hacked, please click on the link below to verify your account</p>
    					<h2>Username : """+emailid+"""</h2>
    					<h2>Password : """+str(pwd)+"""</h2>
    					<br>
    					
  					</body>
				</html>
			"""
	else:
		html = html
	
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("darkweb1.hack@gmail.com", "qrxsdopcolcaferb") 
	
	part2 = MIMEText(html, 'html')

	msg.attach(part2)
	
	s.sendmail(me,you, str(msg)) 
	s.quit() 
	print("mail send successfully....")
