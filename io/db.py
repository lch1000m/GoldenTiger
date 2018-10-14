# db class for reading many db and type

import goldentiger as gt



class DB(object):

    def __init__(self, option):
        self.option = option


    def read(self):
        """
        read file by it's option
        :return: dataframe
        """
        if self.option['source'] == 'yms':
            if self.option['type'] == 'il':
                self.df = gt.io.yms.il.read()
            elif self.option['type'] == 'defect':
                self.df = gt.io.yms.defect.read()

        elif self.option['source'] == 'extractor':
            if self.option['type'] == 'il':
                self.df = gt.io.extractor.il.read()
            elif self.option['type'] == 'defect':
                self.df = gt.io.extractor.defect.read()

        elif self.option['source'] == 'file':
            self.df = gt.io.file.file.read()


    def add_step_desc(self):
        """
         add step_desc information
        """
        pass


    def add_measure_info(self):
        """
        add location & measure information
        """
        pass


    def vehicle_integration(self):
        """
        integrate step & item information along different vehicles
        """
        pass


    def add_outlier_info(self):
        """
        add outlier information aling group
        """
        pass
