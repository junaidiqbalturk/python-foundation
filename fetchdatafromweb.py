from urllib import request

r = request.urlopen("https://www.google.com.pk")
print(r.getcode())
print(r.read())