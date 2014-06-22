import requests as re


a='''https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&response_type=code&client_id=87900254894-20ldk1hmfg6ouoc4snvtvrufuj585gu4.apps.googleusercontent.com&access_type=offline'''
b='''https://accounts.google.com/AccountChooser?service=lso&continue=https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%3Fresponse_type%3Dcode%26scope%3Dhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive%26access_type%3Doffline%26redirect_uri%3Dhttp%3A%2F%2Flocalhost%3A8080%2F%26client_id%3D87900254894-20ldk1hmfg6ouoc4snvtvrufuj585gu4.apps.googleusercontent.com%26hl%3Den%26from_login%3D1%26as%3D-6e22b4497960d6b7&btmpl=authsub&hl=en_GB'''
uid='shagun.exp@gmail.com'
pas='1qW@1qW@'
r=re.get(b,auth=(uid,pas))

print r.encoding
print r.url
print r.headers['content-type']
print r.status_code
q=r.text

f=open('file.html','w+')
f.write(q)
f.close()

rr=re.get('https://mail.google.com',auth=(uid,pas))

print rr.encoding
print rr.url
print rr.headers['content-type']
print rr.status_code
q=rr.text

f=open('file2.html','w+')
f.write(q)
f.close()


