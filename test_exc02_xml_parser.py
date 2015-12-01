import xml.etree.ElementTree as ET
import unittest
import exc02_xml_parser

class TestParser(unittest.TestCase):

	def testIfRaiseExceptionWhenFileIsNotFound(self):
		parser = exc02_xml_parser.Parser('xml/NotFound.xml')
		self.assertRaises(IOError,parser.run())

	def testIfRaiseExceptionWhenXmlIsIncorret(self):
		parser = exc02_xml_parser.Parser('xml/BooksBad.xml')
		self.assertRaises(ET.ParseError,parser.run())

	def testIfNotIsRaise(self):
		parser = exc02_xml_parser.Parser('xml/Books.xml')
		try:
			parser.run()
		except:
			self.fail()

if __name__ == "__main__":
    unittest.main()