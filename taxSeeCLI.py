#! /usr/bin/env python

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import sys

# Reading the data from the input file

missingTaxFile = pd.read_csv(sys.argv[1],header=None)

speciesNames = (missingTaxFile.iloc[:,[0]]).values.tolist()

speciesNames = np.array(speciesNames)
speciesNames = speciesNames.ravel()

specieslist = []
filesToRetry = []
taxidlist = []

# Creates the initial structure of the database for the missing tax data
missingTaxDb = pd.DataFrame()

missingTaxDb_cols = ['superkingdom',
                        'kingdom',
                        'subkingdom',
                        'superphylum',
                        'phylum',
                        'subphylum',
                        'superclass',
                        'class',
                        'subclass',
                        'superorder',
                        'order',
                        'suborder',
                        'superfamily',
                        'family',
                        'subfamily',
                        'tribe',
                        'subtribe',
                        'genus',
                        'subgenus',
                        'species',
                        'subspecies',
                        'taxid']

missingTaxDb = missingTaxDb.append(pd.Series(missingTaxDb_cols),ignore_index=True)

# Reads and stores  the taxids corresponding to the scientific names

for i in speciesNames:
    temparray1 = i.strip().split(' ')
    i = " ".join(temparray1)
    specieslist.append(i)
    URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=%s[SCIN]" % i
    print(URL)
    response = requests.get(URL)
    soup = bs(response.content,'xml')
    taxId = soup.find_all('Id')
    if(len(taxId) >0):
        with open("missingNamesTaxIds.txt",'a') as taxidinfo:
            for tax in taxId:
                taxidinfo.write(str(i)+"\t"+tax.get_text()+"\n")
                taxidlist.append(tax.get_text())
            
    else:
        filesToRetry.append(str(i))

# Reads and stores(as text files) the tax information for each taxid   
                
for i in taxidlist:
    
    URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=%s&mode=text&report=xml" % i
    print(URL)
    response = requests.get(URL)
    soup = bs(response.content,'xml')
    sci_names = soup.find_all('ScientificName')
    ranks = soup.find_all('Rank')
    with open(str(i)+".txt",'w') as taxinfo:
        for names,rank in zip(sci_names,ranks):
            if(rank.get_text() != "no rank"):              
                taxinfo.write(rank.get_text()+"\t"+names.get_text()+"\n")
    

# Goes through each text file for each taxid and extracts the tax information 
    
for i in taxidlist:
    taxinfoFile = pd.read_csv(str(i)+".txt",header=None,sep="\t")
    rankList = (taxinfoFile.iloc[:,[0]]).values.tolist()
    rankList = np.array(rankList)
    rankList.ravel()
    sciNameList = (taxinfoFile.iloc[:,[1]]).values.tolist()
    sciNameList = np.array(sciNameList)
    sciNameList.ravel()
    if('species' in rankList):
        Superkingdom_index = [i1 for i1, e in enumerate(rankList) if e == 'superkingdom']
        Kingdom_index = [i2 for i2, e in enumerate(rankList) if e == 'kingdom']
        Subkingdom_index = [i3 for i3, e in enumerate(rankList) if e == 'subkingdom']
        Superphylum_index = [i4 for i4, e in enumerate(rankList) if e == 'superphylum']
        Phylum_index = [i5 for i5, e in enumerate(rankList) if e == 'phylum']
        Subphylum_index = [i6 for i6, e in enumerate(rankList) if e == 'subphylum']
        Superclass_index = [i7 for i7, e in enumerate(rankList) if e == 'superclass']
        Class_index = [i8 for i8, e in enumerate(rankList) if e == 'class']
        Subclass_index = [i9 for i9, e in enumerate(rankList) if e == 'subclass']
        Superorder_index = [i10 for i10, e in enumerate(rankList) if e == 'superorder']
        Order_index = [i11 for i11, e in enumerate(rankList) if e == 'order']
        Suborder_index = [i12 for i12, e in enumerate(rankList) if e == 'suborder']
        Superfamily_index = [i13 for i13, e in enumerate(rankList) if e == 'superfamily']
        Family_index = [i14 for i14, e in enumerate(rankList) if e == 'family']
        Subfamily_index = [i15 for i15, e in enumerate(rankList) if e == 'subfamily']
        Tribe_index = [i16 for i16, e in enumerate(rankList) if e == 'tribe']
        Subtribe_index = [i17 for i17, e in enumerate(rankList) if e == 'subtribe']
        Genus_index = [i18 for i18, e in enumerate(rankList) if e == 'genus']
        Subgenus_index = [i19 for i19, e in enumerate(rankList) if e == 'subgenus']
        Species_index = [i20 for i20, e in enumerate(rankList) if e == 'species']
        Subspecies_index = [i21 for i21, e in enumerate(rankList) if e == 'subspecies']

# Stores the extracted tax info inside the pandas dataframe
        
        tempList22 = [None] * 22
        
        if(Superkingdom_index):
            tempList22[0] = str(sciNameList[Superkingdom_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[0] = 'n'
            
        if(Kingdom_index):
            tempList22[1] = str(sciNameList[Kingdom_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[1] = 'n'
            
        if(Subkingdom_index):
            tempList22[2] = str(sciNameList[Subkingdom_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[2] = 'n'
            
        if(Superphylum_index):
            tempList22[3] = str(sciNameList[Superphylum_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[3] = 'n'
            
        if(Phylum_index):
            tempList22[4] = str(sciNameList[Phylum_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[4] = 'n'
            
        if(Subphylum_index):
            tempList22[5] = str(sciNameList[Subphylum_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[5] = 'n'
            
        if(Superclass_index):
            tempList22[6] = str(sciNameList[Superclass_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[6] = 'n'
            
        if(Class_index):
            tempList22[7] = str(sciNameList[Class_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[7] = 'n'
            
        if(Subclass_index):
            tempList22[8] = str(sciNameList[Subclass_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[8] = 'n'
            
        if(Superorder_index):
            tempList22[9] = str(sciNameList[Superorder_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[9] = 'n'
            
        if(Order_index):
            tempList22[10] = str(sciNameList[Order_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[10] = 'n'
            
        if(Suborder_index):
            tempList22[11] = str(sciNameList[Suborder_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[11] = 'n'
            
        if(Superfamily_index):
            tempList22[12] = str(sciNameList[Superfamily_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[12] = 'n'
            
        if(Family_index):
            tempList22[13] = str(sciNameList[Family_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[13] = 'n'
            
        if(Subfamily_index):
            tempList22[14] = str(sciNameList[Subfamily_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[14] = 'n'
            
        if(Tribe_index):
            tempList22[15] = str(sciNameList[Tribe_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[15] = 'n'
            
        if(Subtribe_index):
            tempList22[16] = str(sciNameList[Subtribe_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[16] = 'n'
            
        if(Genus_index):
            tempList22[17] = str(sciNameList[Genus_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[17] = 'n'
            
        if(Subgenus_index):
            tempList22[18] = str(sciNameList[Subgenus_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[18] = 'n'
            
        if(Species_index):
            tempList22[19] = str(sciNameList[Species_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[19] = 'n'
            
        if(Subspecies_index):
            tempList22[20] = str(sciNameList[Subspecies_index[0]]).replace('[','').replace(']','').replace('\'','')
        else:
            tempList22[20] = 'n'
            
        tempList22[21] = str(i)
            
        missingTaxDb = missingTaxDb.append(pd.Series(tempList22),ignore_index=True)

# Converts the pandas dataframe to .csv format and saves the file.
        
missingTaxDb.to_csv("missingTaxonomyInfo.csv",index=False,header=False)

# Informs about scientific names for which the tax information retrieval failed. 

with open("taxSeeLog.txt",'w') as logFile:
    if(filesToRetry):
        logFile.write("There were problems in retrieving info for the following: \n\n")
        for i in filesToRetry:
            logFile.write(str(i)+'\n')
    else:
        logFile.write("It looks like all the info has been successfully retrieved")
    
    
