import smtplib

# Жду от вас письмо! (слайды 14-18). Воспользуйтесь менеджером контекста (with … as) (слайд 20)
# (Не забудьте для себя понять код из официальной документации – слайд 17).


smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()
smtp_object.login('storchak.eugene@gmail.com', '******')
smtp_object.sendmail(from_addr="storchak.eugene@gmail.com",
                     to_addrs="Y.g.novoselova@gmail.com",
                     msg="test abc")
smtp_object.quit()
