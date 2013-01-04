# coding: utf-8

from dext.views import handler

from common.utils.resources import Resource
from common.utils.decorators import login_required

from game.prototypes import TimePrototype

from game.heroes.prototypes import HeroPrototype

from game.map.storage import map_info_storage
from game.map.logic import get_map_info
from game.map.places.prototypes import PlacePrototype
from game.map.generator import descriptors
from game.map.conf import map_settings

class MapResource(Resource):

    def __init__(self, request, *args, **kwargs):
        super(MapResource, self).__init__(request, *args, **kwargs)

    @handler('', method='get')
    def info(self):
        map_info = get_map_info()
        return self.json(status='ok', data=map_info)

    @login_required
    @handler('cell-info', method='get')
    def cell_info(self, x, y):

        x = int(x)
        y = int(y)

        world = map_info_storage.item.world

        cell = world.cell_info(x, y)

        randomized_cell = cell.randomize(seed=(x+y)*TimePrototype.get_current_time().game_time.day, fraction=map_settings.CELL_RANDOMIZE_FRACTION)

        return self.template('map/cell_info.html',
                             {'place': PlacePrototype.get_by_coordinates(x, y),
                              'cell': cell,
                              'descr_wind': descriptors.wind(randomized_cell),
                              'descr_temperature': descriptors.temperature(randomized_cell),
                              'descr_wetness': descriptors.wetness(randomized_cell),
                              'x': x,
                              'y': y,
                              'hero': HeroPrototype.get_by_account_id(self.account.id) if self.account else None} )
