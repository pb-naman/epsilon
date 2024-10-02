import pyTigerGraph as tg
from credentials import *

def get_tg_conn():
	conn = tg.TigerGraphConnection(host=HOST,
		username=USERNAME,
		password=PASSWORD,
		graphname=GRAPHNAME,
		gsPort="443"
		)
	conn.apiToken = conn.getToken(Secret)
	return conn


def tg_runInstalledQuery(queryname, params):
	conn_obj = get_tg_conn()
	return conn_obj.runInstalledQuery(queryName = queryname, params = params)
