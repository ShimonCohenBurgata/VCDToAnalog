
class Signal(object):
    """
    Class that represent the analog info of a specific io
    """

    def __init__(self, wildcard, name, io, size, hier):
        """
        Constructor
        :param name: --> The name of the signal
        :param io: --> signal can be input or output
        :param size: --> the bus size
        :param hier: --> the hierarchy of the signal from top level
        """
        self._wildcard = wildcard
        self._name = name
        self._io = io
        self._size = size
        self._hier = hier
        self._attri = {'trise': 0.1, 'tfall': 0.1, 'vih': 2.0, 'vil': 0.0, 'vol': 0.00001, 'voh': 1.6}

    def set_attri(self, attri, val):
        """
        Attribute setter
        :param attri: --> the name of the attribute
        :param val: --> the value of the attribute
        for example -->  sig = Signal('25MHz_CLK', 'in', 3)
                         sig.set_attri('trise', 0.2)
        """

        if attri in self._attri.keys():
            self._attri[attri] = val
        else:
            raise ValueError("'{}' is not a valid attribute \n \t Valid attributes are {}"
                             .format(attri, list(self._attri.keys())))

    def get_attri(self, attri):
        """
        Get signal attribute
        :param attri: --> the name of the attribute
        :return --> the value of the attribute
        for example --> sig.get_io('trise')
        """
        try:
            return self._attri[attri]
        except KeyError as e:
            print("'{}' is not a valid attribute \n \t Valid attributes are {}"
                  .format(attri, list(self._attri.keys())))

    def set_io(self, io):
        """
        Set the signal io
        valid inputs are 'in' and 'out'
        :param io:
        :return:
        for example --> sig.set_io('in')
        """
        if io != 'in' and io != 'out':
            raise ValueError("'{}' is not a valid io \n \t Valid io's are 'in' and 'out'".format(io))
        else:
            self._io = io

    def get_io(self):
        """
        Get the signal io
        :return: --> io name
        """
        return self._io

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_size(self, size):
        self._size = size

    def get_size(self):
        return self._size

    def set_hier(self, hier):
        self._hier = hier

    def get_hier(self):
        return self._hier

    def set_wildcard(self, wildcard):
        self._wildcard = wildcard

    def get_wildcard(self):
        return self._wildcard

    def __str__(self):

        str_size = ''

        if self._hier != '':
            str_hier = '.scope module {} \n.hier 1'.format(self._hier) + '\n'
            str_hier_info = '{}.'.format(self._hier)
        else:
            str_hier = ''
            str_hier_info = ''

        st = ''
        st += str_hier
        st += '.' + self._io + ' ' + self._name + str_size + '\n'
        if self._io == 'in':
            st += '.' + 'vih' + ' ' + str(self._attri['vih']) + ' ' + str_hier_info + self._name + str_size + '\n'
            st += '.' + 'vil' + ' ' + str(self._attri['vil']) + ' ' + str_hier_info + self._name + str_size + '\n'
            st += '.' + 'trise' + ' ' + str(self._attri['trise']) + ' ' + str_hier_info + self._name + str_size + '\n'
            st += '.' + 'tfall' + ' ' + str(self._attri['tfall']) + ' ' + str_hier_info + self._name + str_size + '\n'

        elif self._io == 'out':
            st += '.' + 'vol' + ' ' + str(self._attri['vol']) + ' ' + str_hier_info + self._name + str_size + '\n'
            st += '.' + 'voh' + ' ' + str(self._attri['voh']) + ' ' + str_hier_info + self._name + str_size + '\n'

        else:
            raise ValueError("io can be input or output")

        return st
