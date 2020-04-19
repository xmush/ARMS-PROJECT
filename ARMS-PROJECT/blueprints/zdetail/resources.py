class ZodiakDetailResource(Resurce):

    # get zodiak detail host
    host = app.config['ZDETAIL_HOST']

#     wio_host = "https://api.weatherbit.io/v2.0"
#     # @jwt_required
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('ip', location='args', default=None)
#         args = parser.parse_args()

#         rq = requests.get(self.wio_host + '/ip', params={'ip': args['ip']})
#         geo = rq.json()
#         lat = geo['latitude']
#         lon = geo['longitude']
#         rq = requests.get(self.wio_host + '/current', params={'lat': lat, 'lon': lon})
#         current = rq.json()

#         return {
#             'city': geo['city'],
#             'organization': geo['organization'],
#             'timezone': geo['timezone'],
#             'current_weather': {
#                 'date': current['data'][0]['datetime'],
#                 'temp': current['data'][0]['temp']
#             }
#         }

api.add_resource(ZodiakDetailResource, '/zodiakDetail')