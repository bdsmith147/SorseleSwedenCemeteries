# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:40:47 2020

@author: benjamin
"""

from lxml import html
import requests
import numpy as np
import pandas as pd
import datetime as dt
from time import time as t

#Uncomment each block block below one at a time to extract data from each cemetery.

#Cemetery 1:
#cemetery_name = 'sorsele-skogskyrkogard'
#blocks = np.array(['1', '2', '3', '4', '6', '7', '8', 'AL', '10', '11', '12', '13', '13ML', '14', '15'])
#pages_in_block = np.array([4, 2, 6, 4, 7, 6, 3, 1, 3, 1, 1, 3, 1, 2, 1])

#Cemetery 2:
#cemetery_name = 'sorsele-gamla-kyrkogard'
#blocks = np.array(['0'])
#pages_in_block = np.array([21])

#Cemetery 3:
#cemetery_name = 'skogskyrkogarden'
#blocks = np.array(['1', '2', '3', '4', '5', '7', '8', 'a', 'allm', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
#pages_in_block = np.array([2, 3, 3, 5, 5, 3, 2, 8, 3, 4, 4, 10, 5, 5, 6, 6])

#Cemetery 4:
#cemetery_name = 'viktoriakyrkans-kyrkogard'
#blocks = np.array(['0'])
#pages_in_block = np.array([1])

#Cemetery 5:
#cemetery_name = 'mala-gamla'
#blocks = np.array(['askf', 'aslu', 'maga', 'milu', 'urnf'])
#pages_in_block = np.array([1, 0, 11, 2, 1])

#Cemetery 6:
#cemetery_name = 'gargnas-kyrkogard'
#blocks = np.array(['1', '2', '3', '3ml'])
#pages_in_block = np.array([18, 6, 2, 1])


numBlocks = len(blocks)

mainURL = 'http://gravar.se/en/forsamling/mala-sorsele-pastorat/' + cemetery_name + '/0/'

entries = []
AllData = pd.DataFrame(columns=['Block', 'Names', 'Births', 'Deaths', 'Site', 'Link'])
for b in range(numBlocks):
    blockURL = mainURL + blocks[b] + '/page/'
    domain = 'http://gravar.se'
    
    # Generate arrays to append data to
    block_labels = np.array([]) # The cemetery block designator
    block_links = np.array([]) # All URLs to individual pages
    block_names = np.array([]) # All full names
    block_births = np.array([]) # All birth dates
    block_deaths = np.array([]) # All death dates
    block_sites = np.array([]) # The grave sites within the cemetery block
    
    for i in range(pages_in_block[b]): # Extract the data from each page in a cemetery block
        pnum = str(i+1)
        page = requests.get(blockURL + pnum)
        tree = html.fromstring(page.content)
        links = np.array(tree.xpath('//ul[@class="buried"]/*/div/h2/a/@href'))
        links = np.array([domain + link for link in links]) # Add the domain
        names = np.array(tree.xpath('//ul[@class="buried"]/*/div/h2/a/text()'))
        birth_elem = tree.xpath('//ul[@class="buried"]/*/div/p[1]/span[1]')
        births = np.array([be.text for be in birth_elem])
        births[births == None] = ''#'0001-01-01'
        
        
        death_elem = tree.xpath('//ul[@class="buried"]/*/div/p[1]/span[2]')
        deaths = np.array([de.text for de in death_elem])
        deaths[deaths == None] = ''#'0001-01-01'
        
        
        sites = np.array(tree.xpath('//ul[@class="buried"]/*/div/p[2]/span/text()'))
        labels = np.array([blocks[b]]*len(names))
        
        block_links = np.append(block_links, links)
        block_names = np.append(block_names, names)
        block_labels = np.append(block_labels, labels)
        block_births = np.append(block_births, births)
        block_deaths = np.append(block_deaths, deaths)
        block_sites = np.append(block_sites, sites)
    block_blocks = np.array([blocks[b] * len(block_names)])
    print(blocks[b], ': ', len(block_names))
    entries.append(len(block_names))

    data = np.stack([block_labels, block_names, block_births, block_deaths, block_sites, block_links]).T
    df = pd.DataFrame(data, columns=['Block', 'Names', 'Births', 'Deaths', 'Site', 'Link'])
    AllData = AllData.append(df)
#births as date objects
#block_births = [dt.datetime.strptime(block_births[i], '%Y-%m-%d').date() for i in range(len(block_births))]
#block_deaths = [dt.datetime.strptime(block_deaths[i], '%Y-%m-%d').date() for i in range(len(block_deaths))]
#%%
begtime = t()
print('Saving...')      
AllData.to_csv(cemetery_name + '.csv', encoding='utf-8-sig')
print('Completed CSV')
endtime = t()
print('Total Time: ', (endtime - begtime), ' s')
