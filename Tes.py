import falcon
import mysql.connector
import json
import collections
import settings

class TesResource:
	def on_get(self, req, resp):
		cnx = mysql.connector.connect(**settings.dbconfig)
		cursor = cnx.cursor()
		
		query = ("SELECT field1,field2 FROM tes")
		cursor.execute(query)

		rows = cursor.fetchall()
		
		data_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['field1'] = row[0]
			d['field2'] = row[1]
			data_list.append(d)
		
		resp.status = falcon.HTTP_200
		resp.body = json.dumps(data_list)

		cursor.close()
		cnx.close()

class TesResourceid:
	def on_get(self, req, resp, id):
		cnx = mysql.connector.connect(**settings.dbconfig)
		cursor = cnx.cursor()
		
		query = ("SELECT field1,field2 FROM tes WHERE id=%s")
		cursor.execute(query, (id,))

		rows = cursor.fetchall()
		
		data_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['field1'] = row[0]
			d['field2'] = row[1]
			data_list.append(d)
		
		resp.status = falcon.HTTP_200
		resp.body = json.dumps(data_list)

		cursor.close()
		cnx.close()
