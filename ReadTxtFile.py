from xbrl import XBRLParser, GAAP, GAAPSerializer


def readFile():
    xbrl_parser = XBRLParser()

    xbrl = xbrl_parser.parse("C://Users//eric//Desktop//Textfiles//0001193125-17-035551.xml")
    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20131228", context="current", ignore_errors=0)
    serializer = GAAPSerializer()
    result = serializer.dump(gaap_obj)
    print(result.data)
