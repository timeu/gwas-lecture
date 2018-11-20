import urllib
import scipy as SP
import os
import pdb

studies = {}

url_base = 'https://www.ebi.ac.uk/~stegle/limix/tutorials/data/'

studies['1000g'] = {}
studies['1000g']['url'] =  url_base + '1000g/1000g_chrom20_snps.hdf5'
studies['1000g']['path'] =  '1000g/1000g_chrom20_snps.hdf5'

studies['1000g_annotation'] = {}
studies['1000g_annotation']['url'] =  url_base + '1000g/1000g_sample_annotation.hdf5'
studies['1000g_annotation']['path'] =  '1000g/1000g_sample_annotation.hdf5'

studies['arab107'] = {}
studies['arab107']['url'] =  url_base + 'arab107/atwell_107.hdf5'
studies['arab107']['path'] =  'arab107/atwell_107.hdf5'

studies['BYxRM'] = {}
studies['BYxRM']['url'] =  url_base + 'BYxRM/BYxRM.hdf5'
studies['BYxRM']['path'] =  'BYxRM/BYxRM.hdf5'

studies['smith08'] = {}
studies['smith08']['url'] =  url_base + 'smith_2008/smith08.hdf5'
studies['smith08']['path'] =  'smith_2008/smith08.hdf5'

studies['glucs'] = {}
studies['smith08']['url'] =  url_base + 'cmeyer_glucs2015/bmeyer_etal.txt' 
studies['smith08']['path'] =  'cmeyer_glucs2015/bmeyer_etal.txt'

def get_file(study_name):
    """return hdf5 file and download from the web if needed"""
    study = studies[study_name]
    base_name = os.path.dirname(os.path.abspath(__file__))
    #do we have the file?
    file_name = os.path.join(base_name,study['path'])
    dir_name  = os.path.dirname(file_name)
    if not os.path.exists(file_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        print "file not found, downloading from %s" % study['url']
        download_file(study['url'],file_name) 
    return file_name

def download_file(url,file):
    testfile=urllib.URLopener()
    testfile.retrieve(url,file)

if __name__ == '__main__':
    get_file('1000g')
