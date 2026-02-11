import smtplib

email = "za378r@gmail.com"
password = "kkksnylyhnvlirjm"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)

print("Login successful!")

server.quit()