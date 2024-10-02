import pyTigerGraph as tg
from credentials import *

def get_tg_conn():
	conn = tg.TigerGraphConnection(host=HOST,
		username=USERNAME,
		password=PASSWORD,
		graphname=GRAPHNAME,
		)
	try:
		conn.apiToken = conn.getToken(Secret)
		return conn
	except :
		print()


def tg_runInstalledQuery(queryname, params):
	conn_obj = get_tg_conn()
	return conn_obj.runInstalledQuery(queryName = queryname, params = params)
