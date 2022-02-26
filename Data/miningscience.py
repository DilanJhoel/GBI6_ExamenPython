# pip install biopython
# pip install Bio
import os
import Bio
from Bio.Seq import Seq
from Bio import Entrez
def download_pubmed(keyword):
    """
    Permite descargar información sobre publicaciones y artículos relacionados con la **palabra clave** que se usa para buscar.
    """
    from Bio import Entrez
    Entrez.email = "dilan.porras@est.ikiam.edu.ec"
    ID_pubmed = Entrez.esearch(db = "pubmed", term = keyword,
                                usehistory = "y")
    print("Resultados encontrados:")
    record = Entrez.read(ID_pubmed) 
    id_list = record["IdList"]
    print(record["Count"])
    webenv = record["WebEnv"] #Web Enviroment that contains the UID list to be provided,
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db = "pubmed",
                           rettype = "medline",
                           retmode = "text", #@https://www.ncbi...,
                           retstart = 0,
                           retmax = 543, #máximo 10000,
                           webenv = webenv,
                           query_key = query_key)
    print("Ingrese nombre con terminación (ejemplo: *file.txt*):")
    file = open(input(), "w") 
    file.write(handle.read())
    file.close()
    return file.name #return file → que tipo de archivo es.
    #print(handle.read()) 

######
import csv 
import re
import pandas as pd 
from collections import Counter

def mining_pubs(tipo):
    """
    Permite usar tres tipos de variables: **DP** sobre el año de publicación del artículo por PMID, **AU** sobre el número de autores por PMID, **AD** sobre el conteo de autores por país, para mostrar un dataframe como resultado.
    """
    print("Ingrese el nombre del archivo:")
    with open(input()) as f:
        my_text = f.read()
    if tipo == "DP":
        PMID = re.findall("PMID- (\d*)", my_text) 
        year = re.findall("DP\s{2}-\s(\d{4})", my_text)
        PMID_A = pd.DataFrame()
        PMID_A["PMID"] = PMID
        PMID_A["DP_year"] = year
        return (PMID_A)
    elif tipo == "AU": 
        PMID = re.findall("PMID- (\d*)", my_text) 
        autors = my_text.split("PMID- ")
        autors.pop(0)
        autors_number = []
        for i in range(len(autors)):
            number = re.findall("AU -", autors[i])
            n = (len(number))
            autors_number.append(n)
        PMID_B = pd.DataFrame()
        PMID_B["PMID"] = PMID 
        PMID_B["num_auth"] = autors_number
        return (PMID_B)
    elif tipo == "AD": 
        my_text = re.sub(r" [A-Z]{1}\.","", my_text)
        my_text = re.sub(r"Av\.","", my_text)
        my_text = re.sub(r"Vic\.","", my_text)
        my_text = re.sub(r"Tas\.","", my_text)
        AD = my_text.split("AD  - ")
        countries = []
        for i in range(len(AD)): 
            country = re.findall("\S, ([A-Za-z]*)\.", AD[i])
            if not country == []: 
                if not len(country) >= 2:  
                    if re.findall("^[A-Z]", country[0]): 
                        countries.append(country[0])
        count=Counter(countries)
        result = {}
        for key in count:
            value = count[key]
            if value != 1: 
                result[key] = value
        autors_country = pd.DataFrame()
        autors_country["country"] = result.keys()
        autors_country["num_auth"] = result.values()
        return (autors_country)