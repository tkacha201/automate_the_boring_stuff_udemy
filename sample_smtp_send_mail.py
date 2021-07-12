import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) #second argument is a port, ports differ based on providers
conn.ehlo() #connecting to that smtp server
conn.starttls() #begin encryption
conn.login('sample.mail@gmail.com', 'password') #had to follow this to get a password - https://support.google.com/accounts/answer/185833?hl=en
conn.sendmail('sample.mail@gmail.com', 'sample.recipient@mail.com', 'Subject: Test mail.\n\nHello this is a test\n\n-Bye.')
conn.quit() #disconnect
