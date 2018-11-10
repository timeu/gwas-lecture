import h5py 
import scipy as sp
import re
import pdb


if __name__ == '__main__':
	geno = sp.loadtxt('BYxRM_GenoData.txt',dtype='str')
	pheno = sp.loadtxt('BYxRM_PhenoData.txt',dtype='str')

	#parse genotype markers
	pattern=re.compile('(.*)_chr(.*?)_(.*?)_(.*?)_(.*?).*')
	alleles = []
	pos     = []
	chrom   = []
	for marker in geno[1::,0]:
		p = pattern.match(marker)
		pos.append(p.group(3))
		chrom.append(p.group(2))
		_alleles = [p.group(4),p.group(5)]
		alleles.append(_alleles)
	pos = sp.array(pos,dtype='int')
	chrom = sp.array(chrom,dtype='int')
	alleles = sp.array(alleles)


	Mgeno = sp.array(1.0*(geno[1::,1::]=='R'),dtype='uint8')
	geno_ID = geno[0,1::]
	pheno_ID = pheno[1::,0]

	Mpheno = pheno[1::,1::]
	Mpheno[Mpheno=='NA']='NAN'
	Mpheno = sp.array(Mpheno,dtype='float')
	phenotype_names = pheno[0,1::]

	f = h5py.File('./BYxRM.hdf5','w')
	f_geno = f.create_group('genotype')
	f_pheno = f.create_group('phenotype')
	f_geno.create_group('col_header')
	f_geno.create_group('row_header')
	f_geno.create_dataset(name='matrix',data=Mgeno.T,chunks=(Mgeno.shape[1],1000),compression='gzip')
	f_geno['row_header'].create_dataset(name='sample_ID',data=geno_ID)
	f_geno['col_header'].create_dataset(name='chrom',data=chrom)
	f_geno['col_header'].create_dataset(name='pos',data=pos)
	f_geno['col_header'].create_dataset(name='alleles',data=alleles)

	f_pheno.create_group('col_header')
	f_pheno.create_group('row_header')
	f_pheno.create_dataset(name='matrix',data=Mpheno,compression='gzip')
	f_pheno['row_header'].create_dataset(name='sample_ID',data=pheno_ID)
	f_pheno['col_header'].create_dataset(name='phenotype_ID',data=phenotype_names)

