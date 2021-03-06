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
                self.df = gt.gt_io.yms.il.read()
            elif self.option['type'] == 'defect':
                self.df = gt.gt_io.yms.defect.read()

        elif self.option['source'] == 'extractor':
            if self.option['type'] == 'il':
                self.df = gt.gt_io.extractor.il.read()
            elif self.option['type'] == 'defect':
                self.df = gt.gt_io.extractor.defect.read()

        elif self.option['source'] == 'file':
            self.df = gt.gt_io.file.file.read()
