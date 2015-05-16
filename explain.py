import MeCab
import romkan
import pdb

from xml.etree.ElementTree import iterparse
from bottle import route, run, view, request
from urllib.request import urlopen
from gzip import GzipFile

mc = MeCab.Tagger('-Owakati')

try:
    source = iterparse("JMdict_e.gz.txt")
except FileNotFoundError:
    source = iterparse(GzipFile(fileobj=urlopen("ftp://ftp.monash.edu.au/pub/nihongo/JMdict_e.gz")))

jmdict = {}
for event, elem in source:
    if elem.tag == "entry":
        keb   = [e.text for e in elem.findall("k_ele/keb")]
        reb   = [e.text for e in elem.findall("r_ele/reb")]
        gloss = [e.text for e in elem.findall("sense/gloss")]
        for k in keb or reb:
            jmdict[k] = (reb, gloss)
        elem.clear()

@route('/')
@view('index')
def index():
    text = request.query.getunicode('text', '')
    words = mc.parse(text).strip().split(' ')
    pronunciation = [jmdict.get(w, ([], []))[0] for w in words]
    english = [jmdict.get(w, ([], []))[1] for w in words]
    romaji = [[romkan.to_roma(w) for w in p] for p in pronunciation]

    return {"text": text,
            "words": words,
            "pronunciation": pronunciation,
            "romaji": romaji,
            "english": english}

run(host='localhost', port=8080, debug=True, reloader=True)
