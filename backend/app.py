import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient(
            headers={
               'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
                'x-rapidapi-key': "0cb1642762msh7fb4595b29245afp167c30jsn02e2a9801d0c"
            }
        )
        response = await http_client.fetch('https://covid-19-data.p.rapidapi.com/totals')
        print('response')
        self.write(response)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()