class Graf:

	# Yapici islevi goren fonksiyon
	# Komsuluk matrisi ve gezilen dugumleri isaretleyen listeyi baslatir
	def __init__(self, n_dugum):

		self.n_dugum = n_dugum
		self.komsuluk_matrisi = [[] for i in range(n_dugum)]
		self.gezilen_dugumler = [False for i in range(n_dugum)]

	# d1 ve d2 dugumleri arasinda bir kenar olusturur
	def kenar_ekle(self, d1, d2):
		self.komsuluk_matrisi[d1].append(d2)

	# Graf uzerinde derinine arama yapar
	def derinine_arama(self, dugum):

		if self.gezilen_dugumler[dugum] is False:

			self.gezilen_dugumler[dugum] = True
			print(dugum, end='->')

		for cocuk_dugum in self.komsuluk_matrisi[dugum]:

			if self.gezilen_dugumler[cocuk_dugum] is False:
				self.derinine_arama(cocuk_dugum)


def main():

	graf = Graf(7)
	
	graf.kenar_ekle(0, 1)
	graf.kenar_ekle(0, 2)
	graf.kenar_ekle(1, 3)
	graf.kenar_ekle(1, 4)
	graf.kenar_ekle(2, 5)
	graf.kenar_ekle(2, 6)

	graf.derinine_arama(0)

if __name__ == "__main__":			
	main()	

	

