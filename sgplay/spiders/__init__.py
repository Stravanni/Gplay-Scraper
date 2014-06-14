from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.item import Item
from sgplay.items import SgplayItem
from scrapy.http import Request

from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url

from pyvirtualdisplay import Display
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

#from selenium import selenium
from selenium import webdriver

import string
import time

import lxml.html

###### PROVA GPLAY con SELENIUM #######

class SgplaySpider(BaseSpider):
	name = "spider_sgplay"
	allowed_domains = ["google.com"]
	start_urls = [
		"https://play.google.com/store/apps/category/FINANCE/collection/topselling_paid?start=0&num=24"
	  # "https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE/collection/topselling_paid"
	]
	
	def __init__(self):
		BaseSpider.__init__(self)
		self.verificationErrors = []
		self.driver = webdriver.Firefox()
		###self.selenium = selenium("localhost", 4444, "*chrome", "http://www.domain.com")
		#self.selenium.start("captureNetworkTraffic=true")
		###self.selenium.start()
	
	def __del__(self):
		###self.selenium.stop()
		print self.verificationErrors
		CrawlSpider.__del__(self)	
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//a[@class="title"]')
		###sel = self.selenium
		dri = self.driver
		
		dri.get(response.url)
		
		if dri:
			#Wait for javascript to load in Selenium                                                                                       
			#time.sleep(1)
			print("------------\nwebDriver Loaded correct\n------------")
		
		
		ret = dri.execute_script("var res = false;return document.URL;")
		print("\nlink:");
		print(ret);
		
		# ret = dri.execute_script("var res = false;var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");function fireClick(elem) {if(typeof elem == \"string\") elem = document.getElementById(objID);if(!elem) return;if(document.dispatchEvent) {var oEvent = document.createEvent( \"MouseEvents\" );oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);res = elem.dispatchEvent( oEvent );}else if(document.fireEvent){elem.click();}};links = Array.prototype.slice.call(myLink);fireClick(links[0]);return res")
		#ris = dri.find_element_by_id("com.ikamasutra.android")
		ret = dri.execute_script("var res = false;" + 
				"var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");" + 
				"function fireClick(elem) {" + 
				#"if(typeof elem == \"string\") elem = document.getElementById(objID);"+
				#"if(!elem) {res = 1;return;}"+
				#"if(document.dispatchEvent)"+
				"{var oEvent = document.createEvent( \"MouseEvents\" );res = false;" + 
				"oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);" + 
				"res = elem.dispatchEvent( oEvent );}" + 
				#"else if(document.fireEvent){elem.click();res = 3;}"+
				"};" + 
				"links = Array.prototype.slice.call(myLink);" + 
				"fireClick(links[0]);")

		#print("\n\n\nritorna?");
		#print(ret);
		#print(ris);
		#print("\n\n\n");
		#
		#xml = sel.captureNetworkTraffic("url")
		#print(xml)
		##################################################
		##################################################
		#
		# Il tempo ci vuole?
		#
		#time.sleep(1) #wait a second for page to load
		#
		# ===> Sembra di no!
		#
		##################################################
		##################################################
		
		#root = lxml.html.fromstring(sel.get_html_source())
		#root = sel.getLocation()
		#print(root)
		ret = dri.execute_script("var res = false;return document.URL;")
		print("\nlink:");
		print(ret);
		#print(ris);
		print("\n\n\n");
		
##############################################################################################################################################################
# Ripetuto per test		
# 1 ##########################################################################################################################################################
		ret = dri.execute_script("var res = false;" + 
				"var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");" + 
				"function fireClick(elem) {" + 
				#"if(typeof elem == \"string\") elem = document.getElementById(objID);"+
				#"if(!elem) {res = 1;return;}"+
				#"if(document.dispatchEvent)"+
				"{var oEvent = document.createEvent( \"MouseEvents\" );res = false;" + 
				"oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);" + 
				"res = elem.dispatchEvent( oEvent );}" + 
				#"else if(document.fireEvent){elem.click();res = 3;}"+
				"};" + 
				"links = Array.prototype.slice.call(myLink);" + 
				"fireClick(links[0]);")
				
		ret = dri.execute_script("var res = false;return document.URL;")
		print("\nlink:");
		print(ret);
		#print(ris);
		print("\n\n\n");

# 2 ##########################################################################################################################################################
		ret = dri.execute_script("var res = false;" + 
				"var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");" + 
				"function fireClick(elem) {" + 
				#"if(typeof elem == \"string\") elem = document.getElementById(objID);"+
				#"if(!elem) {res = 1;return;}"+
				#"if(document.dispatchEvent)"+
				"{var oEvent = document.createEvent( \"MouseEvents\" );res = false;" + 
				"oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);" + 
				"res = elem.dispatchEvent( oEvent );}" + 
				#"else if(document.fireEvent){elem.click();res = 3;}"+
				"};" + 
				"links = Array.prototype.slice.call(myLink);" + 
				"fireClick(links[0]);")
				
		ret = dri.execute_script("var res = false;return document.URL;")
		print("\nlink:");
		print(ret);
		#print(ris);
		print("\n\n\n");

# 3 ##########################################################################################################################################################
		ret = dri.execute_script("var res = false;" + 
				"var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");" + 
				"function fireClick(elem) {" + 
				#"if(typeof elem == \"string\") elem = document.getElementById(objID);"+
				#"if(!elem) {res = 1;return;}"+
				#"if(document.dispatchEvent)"+
				"{var oEvent = document.createEvent( \"MouseEvents\" );res = false;" + 
				"oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);" + 
				"res = elem.dispatchEvent( oEvent );}" + 
				#"else if(document.fireEvent){elem.click();res = 3;}"+
				"};" + 
				"links = Array.prototype.slice.call(myLink);" + 
				"fireClick(links[0]);")
				
		ret = dri.execute_script("var res = false;return document.URL;")
		print("\nlink 3:");
		print(ret);
		#print(ris);
		print("\n\n\n");

##############################################################################################################################################################
		
		
		items = []
		i = 0
		for site in sites:
			#print("\n")
			#print(i)
			#i+=1
			
			url_ = site.select('@href').extract()
			#print("\n")
			#print(url_[0])
			#print("\n")
			url = "https://play.google.com" + url_[0]
			
			#
			# Parse dell'App
			#
			# Ricordarsi di usare lo 'yield' invece del return, se no terminerebbe il ciclo
			# cosa che avverrebbe con il 'retunrn'
			#yield Request(url,callback=self.parse_it)
			#return Request("https://play.google.com/store/apps/details?id=com.ikamasutra.android&feature=apps_topselling_paid#?t=W251bGwsMSwxLG51bGwsImNvbS5pa2FtYXN1dHJhLmFuZHJvaWQiXQ..",
			#				callback=self.parse_it)
		
	def parse_it(self, response):
		hxs = HtmlXPathSelector(response)
		title = hxs.select('//h1[@class="doc-banner-title"]')
		item = SgplayItem()
		item['title'] = title.select('text()').extract()
		#item['desc'] = site.select('href').extract()
		return item


class SgplaySpider_test_url_relativi(CrawlSpider):
	name = "spider_sgplay_relative"
	allowed_domains = ["google.com"]
	start_urls = [
	   "https://play.google.com/store/apps/category/COMMUNICATION?feature=category-nav"
	]
	
	rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('/store/apps/category/',)), callback='parse_it', follow=True),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(SgmlLinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )
	
	def parse_it(self, response):
		print("\nlink:")
		print(response.url)
		print("\n")
		item = SgplayItem()
		item['link'] = response.url
		return item

################################################################################################################################################################
#.......................................IMPORTANTE..............................................................................................................
#.........................IMPORTANTE....          ....IMPORTANTE................................................................................................
#..........IMPORTANTE...............    IMPORTANTE     ................IMPORTANTE...............................................................................
#.........................IMPORTANTE....          ....IMPORTANTE................................................................................................
#.......................................IMPORTANTE..............................................................................................................
################################################################################################################################################################
#
# ----------------        MODIFICA		           -------------------------------------------------------------------------------------------------------------
# ----------------        FIREFOX PROFILE		  -------------------------------------------------------------------------------------------------------------
# 
# Modifico il Firefox profile di default per non caricare CSS ed immagini (anche flash dalla via, ma non mi intreresserebbe per GPlay)
#
# Prendo di riferimento:
#	
#	(1)	http://stackoverflow.com/questions/7157994/do-not-want-images-to-load-and-css-to-render-on-firefox  // utilizzare addon firefox
#	(2) http://snippets.scrapy.org/snippets/22/																// utilizzare webDriver
#	(3)	http://code.google.com/p/selenium/wiki/FirefoxDriver												// wiki webDriver
#
#	*ricordarsi import:
#		from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
#
################################################################################################################################################################
################################################################################################################################################################

class SgplaySpider_test_url_relativi_noImage_noCSS(BaseSpider):
	name = "spider_sgplay_category"
	allowed_domains = ["google.com"]
	start_urls = [
	   "https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE/collection/topselling_paid"
	]
	
	#base_url = 'https://play.google.com'
	
	def disableImages(self):
		fireFoxProfile = FirefoxProfile()	# Nuovo profilo di FireFox #(anonimo credo, ma non importa, a meno che non voglia crearne uno, salvarlo e caricarlo da qua) 

		fireFoxProfile.set_preference('permissions.default.stylesheet', 2)						# no CSS
		fireFoxProfile.set_preference('permissions.default.image', 2)							# no Image
		# fireFoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')	# no Flash 
		return fireFoxProfile	# restituico il profilo appena creato

	def __init__(self):
		BaseSpider.__init__(self)	# inizializzo il baseSpider con il metodo originale (sto riscrivendo il metodo '__init__()')
		self.verificationErrors = []
		
		# --- Disattivare l'apertura del brawser -------------------------------------
		# Funziona soltatno con Linux, per via delle dipendenze grafiche...
		# self.display = Display(visible=0,backend ='xvnb', size=(800, 600))
		# self.display = Display(visible=0, size=(800, 600))
		# self.display.start()
		# ----------------------------------------------------------------------------
		self.driver = webdriver.Firefox(self.disableImages()) # carico il webdriver con il profilo che crea la funzione 'disableImages()'
		#self.driver = webdriver.Firefox() # carico il webdriver con profilo anonimo (originale)
	
	def parse(self, response):
		# hxs = HtmlXPathSelector(response)
		# sites = hxs.select('//a[@class="title"]')

		urls = []
		url = " "

		dri = self.driver
		dri.get(response.url)
		if dri:
			#Wait for javascript to load in Selenium                                                                                       
			#time.sleep(1)
			print("------------\nwebDriver Loaded correct\n------------")
		
		url_old = dri.execute_script("return document.URL;")
		urls.append(url_old)	# lo inserisco perhe' e' il primo...
		#print("\nlink:");
		#print(url_old);
		
		while (url != url_old):
			url_old = dri.execute_script("return document.URL;")
			ret = dri.execute_script("var res = false;" + 
				"var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");" + 
				"function fireClick(elem) {" + 
				#"if(typeof elem == \"string\") elem = document.getElementById(objID);"+
				#"if(!elem) {res = 1;return;}"+
				#"if(document.dispatchEvent)"+
				"{var oEvent = document.createEvent( \"MouseEvents\" );res = false;" + 
				"oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);" + 
				"res = elem.dispatchEvent( oEvent );}" + 
				#"else if(document.fireEvent){elem.click();res = 3;}"+
				"};" + 
				"links = Array.prototype.slice.call(myLink);" + 
				"fireClick(links[0]);")
			url = dri.execute_script("return document.URL;")	
			urls.append(url)
		
		i = 0
		
		for link in urls:
			i += 1
			print("**************************\n")
			print(i)
			print("\n")
			yield Request(link, callback=self.parse_page)
	
	def parse_page(self, response):
		hxs = HtmlXPathSelector(response)			# Obj hxs per ispezionare l'XPath
		sites = hxs.select('//a[@class="title"]')	# Seleziono tutte le 'div' della classe 'title' ===> rappresentano le singole app
		#base_url = get_base_url(response)			# Mi serve l'url base, per ricorstuire l'url assoluto successivamente (le app hanno url relativi)
		
		for site in sites:
			url_ = site.select('@href').extract()[0]	# estraggo l'oggeto url. [0] perche' e' restituito come lista, invece voglio la string...
			#print("\n"+url_+"\n")
			#print("\n"+urljoin_rfc("https://play.google.com",url_)+"\n")
			yield Request(urljoin_rfc("https://play.google.com", url_), callback=self.parse_it)		# YIELD su l'url ASSOLUTO, con callback alla funzione 'parse_it'
		
		
	def parse_it(self, response):
		print("\n\n\n\nyield\n")
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//h1[@class="doc-banner-title"]')
		items = []
		for site in sites:
			item = SgplayItem()
			item['title'] = site.select('text()').extract()
			#print("\n"+item['title']+"\n")
		#item['desc'] = site.select('href').extract()
			items.append(item)
		return items

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
#
#			CrowlSpider per piu' categorie
#
################################################################################################################################################################
#	La struttura dello SPIDER risuulta essere l'innesto di piu' spider (funzioni di parse che richiamano 'Request' a partide dagli URL ritrovati:
#
#	CrawlSpider
#		==========> ParseCategory
#						==========> ParsePage
#										==========>Parse_it
#													(solo qui realmente estraggo gli oggetti "app" dalla pagina)
#
################################################################################################################################################################
#
#	Esplorare PIU' CATEGORIE
#
# Questo Spider eredita da CrawlSpider, e segue due regole:
#	
#	Rule (1): Esplora ('allow') le categorie esistenti
#	Rule (2): Per ogni categoria ricerca la pagina_1 sia delle 'pay' che delle 'free' cosi' da poter passare i link a 'PARSE_CATEGORY
#
################################################################################################################################################################

class SgplaySpider_CrawlSpider(CrawlSpider):
	name = "spider_sgplay_cs"
	allowed_domains = ["google.com"]
	start_urls = [
	   "https://play.google.com/store",
	   #"https://play.google.com/store/apps/category/BUSINESS?feature=category-nav",
	   #"https://play.google.com/store/apps/category/BOOKS_AND_REFERENCE?feature=category-nav"
	]
	
	rules = (
				# [R1]
				#
				# Quello che serve a 'Rule (2)' [R2] deve essere in 'deny' qua, perche' se no:
				# chiama il metodo 'parse' classico e non il 'parse_category' di R2
				#
		#Rule(SgmlLinkExtractor(allow=('/store/apps/category',), deny=('/[a-bA-B].*/collection/',))),
		Rule(SgmlLinkExtractor(allow=('/store/apps/category', ),deny = ('/BUSINESS.*/collection/',))),
		#Rule(SgmlLinkExtractor(allow=('/store/apps/category',), deny=('/[e-gE-G].*/collection/',))),
		        
		        # [R2]
		        #
		        # Estrae i link delle categorie e  
		        #
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        #Rule(SgmlLinkExtractor(allow=('/apps/category/[a-bA-B].*/collection/',)), callback='parse_category'), # (A-B)
        Rule(SgmlLinkExtractor(allow=('/apps/category/BUSINESS.*/collection/',)), callback='parse_category'), # (A-B)
        #Rule(SgmlLinkExtractor(allow=('/apps/category/[e-gE-G].*/collection/', )), callback='parse_category'),	# (E-G)
        #Rule(SgmlLinkExtractor(allow=('/apps/category/.*BOOK.*/collection/', )), callback='parse_category'), # solo libri
    )
	
	def disableImages(self):
		fireFoxProfile = FirefoxProfile()	# Nuovo profilo di FireFox #(anonimo credo, ma non importa, a meno che non voglia crearne uno, salvarlo e caricarlo da qua) 
		
		fireFoxProfile.set_preference('permissions.default.stylesheet', 2)						# no CSS
		fireFoxProfile.set_preference('permissions.default.image', 2)							# no Image
		# fireFoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so','false')	# no Flash 
		return fireFoxProfile	# restituico il profilo appena creato

	def __init__(self):
		CrawlSpider.__init__(self)	# inizializzo il baseSpider con il metodo originale (sto riscrivendo il metodo '__init__()')
		self.verificationErrors = []
		
		# --- Disattivare l'apertura del brawser -------------------------------------
		# Funziona soltatno con Linux, per via delle dipendenze grafiche...
		# self.display = Display(visible=0,backend ='xvnb', size=(800, 600))
		# self.display = Display(visible=0, size=(800, 600))
		# self.display.start()
		# ----------------------------------------------------------------------------
		self.driver = webdriver.Firefox(self.disableImages()) # carico il webdriver con il profilo che crea la funzione 'disableImages()'
		#self.driver = webdriver.Firefox() # carico il webdriver con profilo anonimo (originale)
	
	def parse_category(self, response):
		print("\n\n\n*************************************")
		print("\n\n\n*************************************")
		print("\n\n\n*************************************")
		print("\n\n\n*************************************")
		
		urls = []
		url = " "

		dri = self.driver
		dri.get(response.url)
		if dri:
			#Wait for javascript to load in Selenium                                                                                       
			#time.sleep(1)
			print("------------\nwebDriver Loaded correct\n------------")
		
		url_old = dri.execute_script("return document.URL;")#+"?start=0&num=24"
		url_old += "?start=0&num=24"	# Con questa concatenazione mi ispeziona anche la prima pagina
										# !!! non so perche' senza non lo faccia
										#     Con lo spider "spider_sgplay_category" base
										#     ispeziona lo stesso, ma qua no (?!)
		
		urls.append(url_old)	# lo inserisco perhe' e' il primo...
		
		#print("\nlink:");
		#print(url_old);
		
		while (url != url_old):
			url_old = dri.execute_script("return document.URL;")
			ret = dri.execute_script("var res = false;" + 
				"var myLink = document.getElementsByClassName(\"num-pagination-page-button num-pagination-next goog-inline-block\");" + 
				"function fireClick(elem) {" + 
				#"if(typeof elem == \"string\") elem = document.getElementById(objID);"+
				#"if(!elem) {res = 1;return;}"+
				#"if(document.dispatchEvent)"+
				"{var oEvent = document.createEvent( \"MouseEvents\" );res = false;" + 
				"oEvent.initMouseEvent(\"click\", true, true,window, 1, 1, 1, 1, 1, false, false, false, false, 0, elem);" + 
				"res = elem.dispatchEvent( oEvent );}" + 
				#"else if(document.fireEvent){elem.click();res = 3;}"+
				"};" + 
				"links = Array.prototype.slice.call(myLink);" + 
				"fireClick(links[0]);")
			url = dri.execute_script("return document.URL;")	
			urls.append(url)
		
		i = 0
		
		for link in urls:
			i += 1
			print("**************************\n")
			print(i)
			print("\n")
			yield Request(link, callback=self.parse_page)
	
	def parse_page(self, response):
		hxs = HtmlXPathSelector(response)			# Obj hxs per ispezionare l'XPath
		sites = hxs.select('//a[@class="title"]')	# Seleziono tutte le 'div' della classe 'title' ===> rappresentano le singole app
		#base_url = get_base_url(response)			# Mi serve l'url base, per ricorstuire l'url assoluto successivamente (le app hanno url relativi)
		
		for site in sites:
			url_ = site.select('@href').extract()[0]	# estraggo l'oggeto url. [0] perche' e' restituito come lista, invece voglio la string...
			#print("\n"+url_+"\n")
			#print("\n"+urljoin_rfc("https://play.google.com",url_)+"\n")
			yield Request(urljoin_rfc("https://play.google.com", url_), callback=self.parse_it)		# YIELD su l'url ASSOLUTO, con callback alla funzione 'parse_it'
		
		
	def parse_it(self, response):
		print("\n\n\n\nyield\n")
		hxs = HtmlXPathSelector(response)
		# Elementi da estrarre:
		#link = response.url	# Questo sistema non e' corretto!!
							# Viene restituito un link 'relativo' alla pagina dei 'topselling' dalla quale sono arrivato
							# Per avere il linlk corretto devo ricercare l'elemento 'assoluto' all'interno
							# ===>
							# <link rel="canonical" href="..." />
							#
		link = hxs.select('//link[@rel="canonical"]')
		title = hxs.select('//h1[@class="doc-banner-title"]')
		desc = hxs.select('//div[@id="doc-original-text"]')
		category = hxs.select('//dd/a[contains(@href,\'/store/apps/category\')]')	# contains(str1, str_contenuta) 
																					#restituisce TRUE se
																					# la stringa2 e' contenuta nella stringa1
		item = SgplayItem()
		
		item['link'] = link.select('@href').extract()
		item['category'] = category.select('text()').extract()
		item['title'] = title.select('text()').extract()
		
		desc_p = desc.select('./p')
		item['desc'] = desc.select('.//text()').extract()
		#for p in desc_p:
		#	item['desc'] += desc_p.select('text()').extract()
	
		return item






################################################################################################################################################################
#
#			SPIDER per ricercare apps a partire dalla pagina di altre app
#
#			App(1)===>	(n)Link suggeriti===>	Ricorsico
#
#			!!!
#			!!! Da dove parte? ->	Esistono App 'strategiche'?
#			!!! Quando finisce? ->	Si creano dei cicli? Se utilizzo 'unique' nell'estrazione dei link e' sufficiente
#			!!! Ridondanza? ->	Da gestire fuori dallo spider
#			!!!	
#
################################################################################################################################################################
class SgplaySpider_CrawlSpider_fromApp(CrawlSpider):
	name = "spider_sgplay_fromApp"
	allowed_domains = ["google.com"]
	start_urls = [
		#"https://play.google.com/store/apps/details?id=com.google.android.street",
		"https://play.google.com/store/apps/details?id=com.DreamFactory.ChineseChess",
	]
	
	rules = (
		#Rule(SgmlLinkExtractor(allow=('/store/apps/details?id=com.zingmagic.chinesechessvfr.*',), unique=True), callback='parse_it', follow=True),
		#Rule(SgmlLinkExtractor(allow=('/store/apps/details.*',), unique=True), callback='parse_it', follow=True),
		Rule(SgmlLinkExtractor(allow=('/store/apps/details.*',), unique=True), callback='parse_it', follow=False),
    )
	
	def parse_it(self, response):
		#print("TROVATO")
		hxs = HtmlXPathSelector(response)
		
		link = hxs.select('//link[@rel="canonical"]')
		title = hxs.select('//h1[@class="doc-banner-title"]')
		desc = hxs.select('//div[@id="doc-original-text"]')
		category = hxs.select('//dd/a[contains(@href,\'/store/apps/category\')]')	
		
		#ITEM
		item = SgplayItem()
		
		##
		##	Per avere codifica "utf-8" posso fare velocemente questo, ma sarebbe meglio modificare l' "Item Exporters"
		##
		
		## #mod .encode("utf-8") 
		item['link'] = link.select('@href').extract()				# originale
		item['category'] = category.select('text()').extract()		# originale
		item['title'] = title.select('text()').extract()			# originale
		item['desc'] = desc.select('.//text()').extract()			# originale
		
#		item['link'] = link.select('@href').extract()[0].encode('utf-8')			# nuovo
#		item['category'] = category.select('text()').extract()[0].encode('utf-8')	# nuovo
#		item['title'] = title.select('text()').extract()[0].encode('utf-8')		# nuovo
#		desc_ = desc.select('.//text()').extract()							# nuovo
#		
#		descrizione_unita = ''												# nuovo
#		# 'desc_' e' un array che include tutta la descrizione estratta come 'array'
#		# questo e' dovuto al fatto che la desc ha sottosezioni <p> ad esempio </p>
#		for d in desc_:	
#			 descrizione_unita += d.encode('utf-8')
#		item['desc'] = descrizione_unita
		
		### #mod fine #mod
		vuoto = []
		if(item['title'] != vuoto):
			return item
		else:
			print("*******************************************")
			print("*******************************************")
			print("*******************************************")
