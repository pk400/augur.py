import json
import websockets

AUGUR_DEFAULT_WS_PORT = 9001
AUGUR_TLS_WS_PORT = 9002
JSON_MEDIA_TYPE = 'application/json'

class AugurPy:
  def __init__(self, tls=False, host='localhost', port=AUGUR_DEFAULT_WS_PORT):
    self._tls = tls
    self._host = host
    self._port = port
    self.websocket = None

  async def open_connection(self):
    scheme = 'ws' if not self._tls else 'wss'
    api_request_url = '{}://{}:{}'.format(scheme, self._host, self._port)
    self.websocket = await websockets.connect(api_request_url)

  async def _call(self, method, params, _id=1):
    data = {'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': _id}
    await self.websocket.send(json.dumps(data))
    print(await self.websocket.recv())

  def get_markets(self, universe, creator=None, ):
    self._call(
      method='getMarkets',
      params={'universe': universe})

  async def get_categories(self, universe, sort_by=None, is_sort_descending=None,
    limit=None, offset=None, callback=None):
    """ Fetch categories in Augur universe. """
    await self._call(
      method='getCategories',
      params={'universe': universe,
              'sortBy': sort_by,
              'isSortDescending': is_sort_descending,
              'limit': limit,
              'offset': offset,
              'callback': callback})
  
