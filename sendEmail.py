import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import getpass
#普通消息
def plainText():
    for i in range(1):
        print("请输入你学校账户的SMTP服务器(一般情况下直接为你们的网址，比如mail.bjtu.edu.cn)")
        smtpAdd=input()
        server = smtplib.SMTP(smtpAdd,25)
        server.starttls()#加密传输
        server.ehlo()
        account=input("请输入账户：  ")
        password=getpass.unix_getpass("请输入密码：  ")
        server.login(account,password)
        msg = MIMEMultipart()
        # msg['From']="nidayede"
        # msg['To']="Dog"
        sub=input("请输入主题")
        msg['Subject']=sub
        message=input("请输入要发送的文本信息：   ")
        msg.attach(MIMEText(message))
        To=input("请输入收件人地址")
        a=input("是否要发送附件，是输入1，否则输入0:   ")
        if a=="0":
            text=msg.as_string()
            server.sendmail(account,To,text)
            print("发送成功")
        else:
            filename=input("输入文件路径:   ")
            attachment=open(filename,'rb')
            p=MIMEBase("1","2")
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(p) 
            text=msg.as_string()
            server.sendmail(account,To,text)
            print("发送成功")

plainText()
