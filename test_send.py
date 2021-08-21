import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create a secure SSL context
context = ssl.create_default_context()

email_address = "hennymenny245@gmail.com"
password = "harvestmoon%100"

sender_email = "hennymenny245@gmail.com"
receiver_email = "bns360@live.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Paperweight - Non-Profit Mental Health Service"
message["From"] = sender_email
message["To"] = receiver_email
text = """\
Hi their friend,
I'm so sorry to bother you in the middle of your busy day, but if you can spare a few moments of your
time I would greatly appreciate it. I have recently started a Non_Profit organization that provides
free virtual counselling to those in need. If you can take a few moments to visit the page and leave
a like for me I would forever grateful. Thank you for you time and I hope you have a wonderful day.
You can follow the link here: https://www.facebook.com/paperweightoffical"""
part1 = MIMEText(text, "plain")
message.attach(part1)

html ="""\
<!DOCTYPE html> 
<html>
	<head>
		<title>paperWeight</title>
	</head>
	
	<body style="background-color: ghostwhite">
		<header>
				<h1 style="color: grey; background-color: lightblue;">paperWeight<sup><small>TM</small></sup></h1>
				<p><i><big>Non-Profit Organization</big></i> - <b><i>Mental Health Service</i></b></p>
				<p><b>FREE VIRTUAL COUNSELLING</b></p>
				<hr/>
		</header>

		<main>
			<hr/>
			<article>
				<section>
					<h4>Hi their friend!</h4>
					<p>I'm so sorry to bother you in the middle of your busy day, but if you can spare a few moments of your</p>
					<p>time I would greatly appreciate it. I have recently started a Non_Profit organization that provides</p>
                    <p>free virtual counselling to those in need. If you can take a few moments to visit the page and leave</p>
					<p>a like for me I would forever grateful. Thank you for you time and I hope you have a wonderful day.</p>
					<p>You can follow the link here:</p>
					<a href="https://www.facebook.com/paperweightoffical">PAPERWEIGHT MENTAL HEALTH SERVICE</a>
				</section>
	</body>
</html>"""

part2 = MIMEText(html, "html")
message.attach(part2)

try:
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(email_address, password)
    print("Email:" + email_address + "\nPassword:" + password)
    print("Login Successful:")
    try:
        server.sendmail(email_address, "bns360@live.com", message.as_string())
    except:
        print("Sending Failed")
except:
    print("Login Failure")