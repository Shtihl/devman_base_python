import os
import smtplib


login = os.environ['LOGIN']
password = os.environ['PASSWORD']

header_from = 'shtihlfd@yandex.ru'
header_to = 'shtihl-fd@yandex.ru'
header_subject = 'dvmn invitation'
header_content_type = 'text/plain; charset="UTF-8"'

email_template = '''\
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''

friend_name = "Shtihl"
sender_name = "Dmitriy"
ref_link = "https://dvmn.org/referrals/Kqg7ALsVtdKa78ct8Y8EvvOLBc7TxNK3k8dpaHQq/"
email_text = email_template.replace('%friend_name%', friend_name).replace("%my_name%", sender_name).replace('%website%', ref_link)

letter = f"""\
From: {header_from}
To: {header_to}
Subject: {header_subject}
Content-Type: {header_content_type}

{email_text}
"""

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password) 
server.sendmail(header_from, header_to, letter)
server.quit()
