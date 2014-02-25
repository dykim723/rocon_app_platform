#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_app_platform/license/LICENSE
#
#################################################################################

from __future__ import division, print_function 

#from .rapp import Rapp, MetaRapp
from .utils import load_rapp_path_dict
from .params import DEFAULT_ROCON_URI
from .exceptions import InvalidRappException
from .rapp import Rapp
from rocon_console import console

class RappIndexer(object):

    def __init__(self):
        self.raw_data_path = {}
        self.raw_data = {}

        # TODO : We might want to manipulate raw_data to have better format in the future. e.g) cache creation
        # self.data = {} 

        self.update_index()

        pass

    def update_index(self):
        self.raw_data_path = load_rapp_path_dict()

        raw_data = {}
        for name, path in self.raw_data_path.items():
            try:
                r = Rapp(name)
                r.load_from_file(path)
                raw_data[name] = r
                console.pretty_println('[' + name + '] : ' + str(r.type) + ' has been added')
            except InvalidRappException as ire:
                console.warning('Error in [' + name + '] : ' + str(ire))
            except Exception as e:
                console.warning('Error in [' + name + '] : ' + str(e))

        for name in raw_data:
            print(str(name))


    def get_parent(self, rapp_name):
        '''
          returns the nearest parent instance of the given rapp
        '''
        # TODO : 
        pass

    def get_root_parent(self, rapp_name):
        '''
          returns the root parent rapp instance of given name
        '''
        pass

    def get_rapp(self, rapp_name):
        '''
          returns rapp instance of given name
        '''
        pass

    def get_compatible_rapps(self, rocon_uri=DEFAULT_ROCON_URI): # TODO: add capability check later
        '''
          returns all rapps which are compatible with given URI 
        '''
        pass

    def to_dot(self):
        '''
            returns the dot graph format
        '''
        # TODO
        pass