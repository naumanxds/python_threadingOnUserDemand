import threading
class Threads:
	def __init__(self, tId):
		self.thread = threading.Thread(target=self.getComments)
		self.tId = tId

	def getComments(self):
		while True:
			try:
				url = urlArr.pop(0)
			except:
				break
			self.dummyFunc(url)

	def dummyFunc(self, url):
		for l in range(5):
			print(self.tId + ' - is working on : ' + url + '\n')


threadLock = threading.Lock()
threadArr = []
urlArr = ['url1','url2','url3','url4','url5','url6','url7','url8']
threadNo = input('Enter the number of threads you want : ')

for l in range(threadNo):
	threadArr.append(Threads('t-' + str(l)))

for l in threadArr:
	l.thread.start()

for l in threadArr:
	l.thread.join()
