import pandas as pd
import xml.etree.ElementTree as ET
import uuid
from xml.dom import minidom
import random


def generate_st():
    return "ST/"+ str(random.randint(10000000,99999999))

def generate_id():
    return str(uuid.uuid4())


def main():
    filepath1 = "srodki_trwale/ewidencja-srodkow-trwalych.xlsx"

    #mapping_functions()
    file1 = pd.read_excel(filepath1, dtype="str")
    
    root = ET.Element("session", {"xmlns": "http://www.soneta.pl/schema/business"})
   

    for _, v in file1.iterrows():
        srodek = create_srodek_trwaly_xml(v)
        if srodek is not None:
            root.append(srodek)
    
    tree = ET.ElementTree(root)
    tree.write("srodki_temp.xml", encoding="utf-8", xml_declaration=True)
    
    
    prettified_xml = prettify_xml("srodki_temp.xml")
    
    
    with open("srodki.xml", "w", encoding="utf-8") as f:
        f.write(prettified_xml)
    
    print("Zakończono generowanie listy")

def prettify_xml(xml_file):
    
    with open(xml_file, "r", encoding="utf-8") as f:
        xml_str = f.read()
    
   
    parsed_xml = minidom.parseString(xml_str)
    return parsed_xml.toprettyxml(indent="  ")

def create_srodek_trwaly_xml(record):
    id_srodek = f"SrodekTrwalyBase_{generate_id()[-8:]}"  
    srodek_element = ET.Element("SrodekTrwalyBase", {
        "id": id_srodek,
        "class": "Soneta.SrodkiTrwale.SrodekTrwaly,Soneta.Ksiega"
    })
    
    
    ET.SubElement(srodek_element, "Typ").text = "ŚrodekTrwały"
    #ET.SubElement(srodek_element, "NumerInwentarzowy").text = record.get("NumerInwentarzowy", "")
    ET.SubElement(srodek_element, "NumerInwentarzowy").text = generate_st()

    ET.SubElement(srodek_element, "Nazwa").text = record.get("Nazwa", "")
    ET.SubElement(srodek_element, "NumerFabryczny").text = ""
    ET.SubElement(srodek_element, "Opis").text = ""
    ET.SubElement(srodek_element, "PozyskanieNrDokumentu").text = ""
    ET.SubElement(srodek_element, "PozyskanieData").text = ""
    
    ET.SubElement(srodek_element, "ZbycieNrDokumentu").text = ""
    ET.SubElement(srodek_element, "ZbycieData").text = ""
    
    #ET.SubElement(srodek_element, "RozpoczecieAmortyzacji").text = "False"
    #ET.SubElement(srodek_element, "RozpoczecieAmortyzacjiPodatkowa").text = "False"
    ET.SubElement(srodek_element, "DataRozpoczeciaAmortyzacji").text = ""
    ET.SubElement(srodek_element, "DataRozpoczeciaAmortyzacjiPodatkowa").text = ""
    ET.SubElement(srodek_element, "DataZakonczeniaAmortyzacji").text = ""
    ET.SubElement(srodek_element, "Stan").text = "Wpisany"
    ET.SubElement(srodek_element, "DataRejestracji").text = ""
    ET.SubElement(srodek_element, "DataRozpoczeciaUzytkowania").text = ""
    ET.SubElement(srodek_element, "DataLikwidacji").text = ""
    ET.SubElement(srodek_element, "DataBO").text = ""
    ET.SubElement(srodek_element, "WartoscPoczatkowaBilansowaBO").text = "0.00 PLN"
    ET.SubElement(srodek_element, "WartoscPoczatkowaPodatkowaBO").text = "0.00 PLN"
    ET.SubElement(srodek_element, "WartoscBilansowaBO01").text = "0.00 PLN"
    ET.SubElement(srodek_element, "WartoscPodatkowaBO01").text = "0.00 PLN"
    ET.SubElement(srodek_element, "OdpisyBilansoweBO01").text = "0.00 PLN"
    ET.SubElement(srodek_element, "OdpisyPodatkoweBO01").text = "0.00 PLN"
    ET.SubElement(srodek_element, "WartoscBilansowaBO").text = "0.00 PLN"
    ET.SubElement(srodek_element, "WartoscPodatkowaBO").text = "0.00 PLN"
    ET.SubElement(srodek_element, "OdpisyBilansoweBO").text = "0.00 PLN"
    ET.SubElement(srodek_element, "OdpisyPodatkoweBO").text = "0.00 PLN"
    ET.SubElement(srodek_element, "DataRozpoczeciaUzytkowaniaBO").text = ""
    ET.SubElement(srodek_element, "DataRozpoczeciaAmortyzacjiBO").text = ""
    ET.SubElement(srodek_element, "MiejsceUzytkowania").text = ""
    ET.SubElement(srodek_element, "DataBOMSR").text = ""
    ET.SubElement(srodek_element, "MetodaBOMSR").text = "Brak"
    ET.SubElement(srodek_element, "WspolczynnikBOMSR").text = "0.00%"
    ET.SubElement(srodek_element, "WartoscBOMSR").text = "0.00 PLN"
    ET.SubElement(srodek_element, "MiesiacNaliczeniaPodatku").text = ""
    ET.SubElement(srodek_element, "RodzajNieruchomosci").text = "Grunt"
    ET.SubElement(srodek_element, "Kategoria").text = ""

    
    historia = ET.SubElement(srodek_element, "Historia")
    his_id = f"SrodekTrwalyBaseHistoria_{generate_id()[-8:]}"
    historia_element = ET.SubElement(historia, "SrodekTrwalyBaseHistoria", {
        "id": his_id, 
        "class": "Soneta.SrodkiTrwale.SrodekTrwalyHistoria,Soneta.Ksiega"
    })
    ET.SubElement(historia_element, "Srodek").text = id_srodek
    ET.SubElement(historia_element, "Aktualnosc").text = "(wszystko)"
    ET.SubElement(historia_element, "Typ").text = "ŚrodekTrwały"
    ET.SubElement(historia_element, "KRST").text = "00000000-0008-0006-2371-000000000000"
    ET.SubElement(historia_element, "Ilosc").text = "1"
    ET.SubElement(historia_element, "JednostkaMiary").text = "00000000-0011-0007-0001-000000000000"
    ET.SubElement(historia_element, "MiejsceUzytkowania").text = ""
    ET.SubElement(historia_element, "CentrumKosztow").text = ""
    ET.SubElement(historia_element, "Odpowiedzialny").text = ""
    ET.SubElement(historia_element, "Nazwisko").text = ""
    ET.SubElement(historia_element, "Wydzial").text = ""

    bilansowa = ET.SubElement(historia_element, "Bilansowa")
    ET.SubElement(bilansowa, "Metoda").text = "Liniowa"
    ET.SubElement(bilansowa, "Stawka").text = "20.00%"
    ET.SubElement(bilansowa, "Wspolczynnik").text = "1.00"

    podatkowa = ET.SubElement(historia_element, "Podatkowa")
    ET.SubElement(podatkowa, "Metoda").text = "Liniowa"
    ET.SubElement(podatkowa, "Stawka").text = "20.00%"
    ET.SubElement(podatkowa, "Wspolczynnik").text = "1.00"

    ET.SubElement(historia_element, "UlgaInwestycyjna").text = "0.00 PLN"
    ET.SubElement(historia_element, "UlgaInwestycyjna30").text = "0.00 PLN"

    sezonowosc = ET.SubElement(historia_element, "Sezonowosc")
    ET.SubElement(sezonowosc, "Rodzaj").text = "Miesięczna"
    ET.SubElement(sezonowosc, "Wartosc").text = "111111111111"
    #ET.SubElement(sezonowosc, "Proporcjonalnie").text = "False"

    ET.SubElement(historia_element, "Zestaw").text = ""
    ET.SubElement(historia_element, "WartoscRynkowa").text = "0.00 PLN"
    ET.SubElement(historia_element, "DataWyceny").text = ""
    ET.SubElement(historia_element, "MetodaWRMSR").text = "Brak"
    ET.SubElement(historia_element, "WspolczynnikWRMSR").text = "0.00%"
    ET.SubElement(historia_element, "WartoscWRMSR").text = "0.00 PLN"
    ET.SubElement(historia_element, "Lokalizacja").text = ""
    ET.SubElement(historia_element, "Kategoria").text = ""
    ET.SubElement(historia_element, "Elementy").text = ""

    historia_ext = ET.SubElement(historia_element, "SrodekTrwalyBaseHistoriaExtension")
    historia_ext_element = ET.SubElement(historia_ext, "SrodekTrwalyBaseHistoriaExtension", id=f"SrodekTrwalyBaseHistoriaExtension_{generate_id()[-8:]}")
    ET.SubElement(historia_ext_element, "Host").text = his_id
    ET.SubElement(historia_ext_element, "KrajDostawy").text = ""
    ET.SubElement(historia_ext_element, "Dostawca").text = ""
    ET.SubElement(historia_ext_element, "OpisTechniczny").text = ""
    ET.SubElement(historia_ext_element, "NumerProjektu").text = ""
    ET.SubElement(historia_ext_element, "TypWlasnosci").text = "0"
    ET.SubElement(historia_ext_element, "TypKorektaVAT").text = "None"
    ET.SubElement(historia_ext_element, "Rewers").text = ""
    ET.SubElement(historia_ext_element, "CharakterSkladnika").text = ""
    ET.SubElement(historia_ext_element, "StatusSkladnika").text = ""
    ET.SubElement(historia_ext_element, "RodzajSkladnika").text = ""
    ET.SubElement(historia_ext_element, "DzierzawaSkladnika").text = ""
    ET.SubElement(historia_ext_element, "TypSkladnika").text = ""
    ET.SubElement(historia_ext_element, "RozliczeniePlatnosci").text = ""
    ET.SubElement(historia_ext_element, "KarencjaKomercja").text = "(pusty)"
    ET.SubElement(historia_ext_element, "NumerPokoju").text = ""
    #ET.SubElement(historia_ext_element, "KodJednostkiOrganizacyjnej").text = ""
    #ET.SubElement(historia_ext_element, "KodSK").text = ""
    ET.SubElement(historia_ext_element, "MulID").text = ""
    ET.SubElement(historia_ext_element, "Lokalizacja").text = ""
    ET.SubElement(historia_ext_element, "NumerInwentarzowy").text = record.get("NumerInwentarzowy", "")
    ET.SubElement(historia_ext_element, "Uzytkownicy").text = ""

    ET.SubElement(srodek_element, "PlanAmortyzacji").text = ""
    ET.SubElement(srodek_element, "Podzielniki").text = ""

    
    ext_element = ET.SubElement(srodek_element, "SrodekTrwalyBaseExtension", id=f"SrodekTrwalyBaseExtension_{generate_id()[-8:]}")
    ET.SubElement(ext_element, "Host").text = id_srodek
    #ET.SubElement(ext_element, "Terminal").text = "False"
    ET.SubElement(ext_element, "TerminalID").text = ""
    ET.SubElement(ext_element, "TerminalSymbol").text = ""

    return srodek_element

def mapping_functions(fpath1,fpath2):
    pass

if __name__ == "__main__":
    main()