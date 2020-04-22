import json, random, string
from . import app, client, cache, create_noninternal_token, create_internal_token, logging, init_database
from unittest import mock
from unittest.mock import patch


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class TestZdetailGet :
    

    def mocked_requests_get(*args, **kwargs):
        host = "https://zodiacal.herokuapp.com/leo"
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data
        
        if len(args) > 0:
            if args[0] == host :
                return MockResponse(
                    [
                        {
                            '_id': '597412e4734d1d6202a9020e',
                            'name': 'Leo',
                            '__v': 0,
                            'famous_people': [
                                'Madonna',
                                ' Jennifer Lopez',
                                ' Kylie Jenner',
                                ' Barack Obama',
                                ' Bill Clinton',
                                ' Demi Lovato',
                                ' Halle Berry',
                                ' Mila Kunis',
                                ' Robert DeNiro',
                                ' Robert Redford',
                                ' Jennifer Lawrence',
                                ' Cara Delavingne',
                                ' Daniel Radcliffe',
                                ' Tom Brady',
                                ' Anna Kendrick',
                                ' Joe Jonas',
                                ' Arnold Schwarzenegger',
                                ' Chris Hemsworth',
                                ' Whitney Houston',
                                ' Giuliana Rancic',
                                ' Yasser Arafat',
                                ' Kylie Jenner',
                                ' Jennifer Lawrence',
                                ' Herbert Hoover',
                                ' Alduous Huxley',
                                ' J.K. Rowling',
                                ' Ray Bradbury',
                                ' Yves Saint-Laurent',
                                ' Coco Chanel',
                                ' Michael Kors',
                                ' Domenico Dolce'
                            ],
                            'how_to_spot': [
                                'Distinctive mane of hair',
                                ' regal posture'
                            ],
                            'secret_wish': [
                                'To rule the world'
                            ],
                            'hates': [
                                'Being ignored',
                                ' silver medals (instead of gold)',
                                ' bland food',
                                ' being alone',
                                ' goodbyes'
                            ],
                            'bad_traits': [
                                'Arrogant',
                                ' wasteful',
                                ' sloppy',
                                ' cold-hearted',
                                ' jealous',
                                ' aggressive'
                            ],
                            'good_traits': [
                                'Courageous',
                                ' kind',
                                ' generous',
                                ' loyal',
                                ' protective',
                                ' nakedly honest',
                                ' entertaining'
                            ],
                            'favorites': [
                                'Theaters',
                                ' cameras',
                                ' DVDs',
                                ' rich desserts',
                                ' red roses',
                                ' exchanging gifts',
                                ' singing',
                                ' affection',
                                ' compliments',
                                ' great clothes'
                            ],
                            'ruling_planet': [
                                'The Sun'
                            ],
                            'body_parts': [
                                ' Heart',
                                ' upper back',
                                ' spine'
                            ],
                            'symbol': 'The lion',
                            'keywords': [
                                'Passion',
                                ' Romance',
                                ' Expression',
                                ' Drama',
                                ' Playfulness',
                                ' Courageous',
                                'Loyal'
                            ],
                            'vibe': 'Radiant energy',
                            'compatibility': [
                                'Aries',
                                ' Gemini',
                                ' Libra',
                                ' Sagittarius'
                            ],
                            'mental_traits': [
                                'Leos are loving and sensitive leaders',
                                ' Leos love children, are very attractive, enjoy luxury and jewelry, and have a bigger-than-life dramatic attitude',
                                ' Leos are show-offs, egoistical, dominant, powerful, determined, charismatic, very demanding, athletic, smart, arrogant, pompous, conceited, temperamental, competitive, passionate, stubborn, loud, loyal, strong-willed, and usually laid-back, but can be highly aggressive or even potentially destructive',
                                ' They typically want to be the center of attention and have a tremendous sense of vitality'
                            ],
                            'physical_traits': [
                                'Leos are known for their glamorous, thick, mane-like dark hair, large dark eyes, proud and confident expression which usually results includes their chin going up a little (resembles a lion), Leo is one of the attractive signs, but they can sometimes have bad luck',
                                ' They may get irritated and have a prominent nose',
                                ' They are typically tall with thin waists, trim athletic legs, broad shoulders, and muscular bodies',
                                ' Leos are the type to have a Leo symbol tattoo',
                                ' They also have very dramatic appearance '
                            ],
                            'sun_dates': [
                                'July 23',
                                'August 22'
                            ],
                            'cardinality': 'Fixed',
                            'element': 'Fire'
                        }
                    ], 200
                )

        else:
            return MockResponse(None, 404)

    # @mock.patch('requests.get', get_mock, post_mock, client_mock, client)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_client_list(self, get_mock, client) :
        # token = create_internal_token()
        # data = {
        #     "zodiak" : "Leo"
        # }
        res = client.get('http://0.0.0.0:5000/detail?zodiak=Leo')

        res_json = json.loads(res.data)
        
        assert res.status_code == 200
