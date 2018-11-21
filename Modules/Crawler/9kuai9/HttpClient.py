# -*- coding: utf-8 -*-

#---------------------------------------
#   程序：HttpClient.py
#   版本：0.1
#   作者：ctang
#   日期：2016-01-29
#   语言：Python 2.7.10
#   说明：http常用方法总结
#---------------------------------------

import cookielib, urllib, urllib2, socket

class HttpClient(object):
	__cookie = cookielib.CookieJar()
	__req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie))
	__req.addheaders = [
		('Accept', 'application/javascript, */*;q=0.8'),
		('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
	]
	urllib2.install_opener(__req)

	def Get(self, url, refer=None):
		try:
			req = urllib2.Request(url)
			if not (refer is None):
				req.add_header('Referer', refer)
			return urllib2.urlopen(req, timeout=120).read()
		except urllib2.HTTPError, e:
			return e.read()
		except socket.timeout, e:
			return ''
		except socket.error, e:
			return ''

	def Post(self, url, data, refer=None):
		try:
			req = urllib2.Request(url, urllib.urlencode(data))
			if not (refer is None):
				req.add_header('Referer', refer)
			return urllib2.urlopen(req, timeout=120).read()
		except urllib2.HTTPError, e:
			return e.read()
		except socket.timeout, e:
			return ''
		except socket.error, e:
			return ''

	def Download(self, url, file):
		output = open(file, 'wb')
		output.write(urllib2.urlopen(url).read())
		output.close()

	def getCookie(self, key):
		for c in self.__cookie:
			if c.name == key:
				return c.value
		return ''

	def setCookie(self, key, val, domain):
		ck = cookielib.Cookie(version=0, name=key, value=val, port=None, port_specified=False, domain=domain, domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
		self.__cookie.set_cookie(ck)

