import falcon
import mysql.connector
import json
import collections
import settings

class Tes2Resource:
	def on_get(self, req, resp):
		cnx = mysql.connector.connect(**settings.dbconfig)
		cursor = cnx.cursor()
		
		query = ("SELECT field1 FROM tes2")
		cursor.execute(query)

		rows = cursor.fetchall()
		
		data_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['field1'] = row[0]
			data_list.append(d)
		
		resp.status = falcon.HTTP_200
		resp.body = json.dumps(data_list)

		cursor.close()
		cnx.close()
		
class Tes2Resourceid:
	def on_get(self, req, resp, id):
		cnx = mysql.connector.connect(**settings.dbconfig)
		cursor = cnx.cursor()
		
		query = ("SELECT field1 FROM tes2 WHERE id=%s")
		cursor.execute(query, (id, ))

		rows = cursor.fetchall()
		
		data_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['field1'] = row[0]
			data_list.append(d)
		
		resp.status = falcon.HTTP_200
		resp.body = json.dumps(data_list)

		cursor.close()
		cnx.close()
