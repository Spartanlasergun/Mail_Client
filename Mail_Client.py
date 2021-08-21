import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create a secure SSL context
context = ssl.create_default_context()

#Email Senders
email_senders = [["juliaroberts2357@gmail.com", "harvestmoon%100"],
                 ["lucalucagrimes@gmail.com", "harvestmoon%100"],
                 ["pollythefox9@gmail.com", "harvestmoon%100"],
                 ["marooneygoldman@gmail.com", "harvestmoon%100"],
                 ["narendrabrandonsingh@gmail.com", "lionheart%100"],
                 ["poppytest88@gmail.com", "harvestmoon%100"],
                 ["jacknicholson607@gmail.com", "harvestmoon%100"],
                 ["hennymenny245@gmail.com", "harvestmoon%100"]]

#Load mailing list
mail_data = open("C:/Users/bns36/Documents/Mail Client/Data/sorted.txt", "r", encoding="utf8")
mail = mail_data.read().splitlines()
mail_data.close()

#mail sent check
mails_sent = 0
mails_bounced = 0

#two-d array identifier
a = 0

mail_count = 0
infinity = 0

while infinity == 0:
    for email in email_senders:
        count = 0
        try:
            server = smtplib.SMTP(host='smtp.gmail.com', port=587)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(email_senders[a][0], email_senders[a][1])
            print(email_senders[a])
            print("Login Successful:")
            while count < 85:
                sender_email = email_senders[a][0]
                receiver_email = mail[mail_count]
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

                html = """\
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
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    mails_sent = mails_sent + 1
                    print(mails_sent)
                except:
                    mails_bounced = mails_bounced + 1
                    print("bounced")
                count = count + 1
                mail_count = mail_count + 1
            server.quit()
            time.sleep(10)
        except:
            print("Login Failure")
            time.sleep(10)
        a = a + 1
    time.sleep(60)
    if mails_sent > 3350:
        infinity = 1
    a = 0

print("Total Mails Sent = " + str(mails_sent))
