import re
'''
Simple class to take adif file - and create csv
'''

class adif2csv(object):
    '''
    adiftocsv. This version assumes that all Columns are filled in the same.

    expected usage
    import adif2csv
    cvt=adif2csv()
    cvt.process("test.adif")
    for a in cvt.dump():
        print(''+a,end='')
    '''

    def __init__(self):
        '''
        Basic constructor
        :return:  None
        '''
        self.fields={}
        self.lines=[]
        self.header=""

    def process(self, filename):
        '''
        Open the file and store the data internally

        Note: At the moment there is no error checking that this has worked.

        :param filename:
        :return:
        '''
        with open(filename, 'rt') as f:
            for line in f:
                if line.startswith("<call"):
                    self.lines.append(line)
            f.close()
        self.make_dict()

    def make_dict(self, all_lines_same=True):
        '''
        This gnerates the header for the CSV file
        :param all_lines_same:
        :return:
        '''
        if len(self.lines) > 0:

            '''
            Make a regex to find the adif_codes, then chop the 1st letter off the string.
            Finally stitch it together as a string - and we have the header
            '''

            self.header = ",".join([ a[1:] for a in re.findall(r'<[a-z_]+',self.lines[0])])
        else:
            print("Error No dictionary can be made - there is no data")

    def dump(self):
        '''
        Simple iterator to allow the converted data to be output
        :return:
        '''
        yield (''+self.header+"\n")
        for line in self.lines:
            '''
            The data looks like this when split using <

            [
            '',
            'call:4>LZ7M ',
            'qso_date:8>20160618 ',
            ]

            So we split again using > - but only for an object who's length is > 0
            '''
            yield(','.join([f.split('>')[1] for f in line.split('<') if len(f) > 0]))

if __name__ == "__main__":
    cvt=adif2csv()
    cvt.process("test.adif")
    for a in cvt.dump():
        print(''+a,end='')
