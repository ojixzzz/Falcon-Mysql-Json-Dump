import falcon
from Tes import TesResource, TesResourceid
from Tes2 import Tes2Resource, Tes2Resourceid

app = falcon.API()
tes	= TesResource()
tesid = TesResourceid()
tes2 = Tes2Resource()
tes2id = Tes2Resourceid()

app.add_route('/tes', tes)
app.add_route('/tes/{id}', tesid)

app.add_route('/tes2', tes2)
app.add_route('/tes2/{id}', tes2id)
