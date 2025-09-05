import spacy
from spacy.pipeline import EntityRuler

# Lista de nomes
nomes_personalizados = [
    "GENOVEVA", "ZITA", "ALMA", "HERTA", "FAUSTA", "EURIDICE", "ZELI",
    "ILIDIA", "OTAVIANA", "QUIRINO", "FLORISA", "CASILDA", "SERAFIN",
    "CELSA", "ONDINA", "VICENTINA", "LAUDELINA", "BENVINDA", "DIONIZIA",
    "HELMA", "MERCES", "JUDITI", "EUTALIA", "YEDDA", "CONCEICAO",
    "ADOLPHO", "MIGUELINA", "NEDINA", "IZIDORO", "ALAIDES", "AGUSTINHO",
    "ORIDES", "ILSE", "SIVIRINO", "VITALINA", "OLINDINA", "ZELINDA",
    "GENY", "ZELINA", "PERCILIA", "ZEFERINO", "LIBERATO", "RAYMUNDO",
    "NAZIRA", "EMIDIA", "VERGILIO", "VENANCIA", "GODOFREDO", "LEONTINA",
    "ALBINA", "LEOCADIA", "FLORIZA", "JARDELINA", "SILVERIA", "GUILHERMINO",
    "CIDALIA", "AMANDIO", "HOLANDA", "SATURNINO", "CENIRA", "VALDEMIRA",
    "OLINDO", "CLEMENTINO", "ETELVINO", "JUVENTINO", "AMELIO", "ATALIBA",
    "ANILDA", "FILOMENO", "DELZA", "LEONIDIO", "ZULMIRA", "ERMELINDA",
    "BALBINA", "FIRMINA", "ANTONINA", "JANUARIA", "GERALDINO", "BELARMINO",
    "OLINTO", "ENEDINO", "CASIMIRO", "DEOLINDA", "MALVINA", "AVELINA",
    "OFELIA", "ISALRA", "ESTANISLAU", "IDALINO", "CACILDA", "ITALIA",
    "GERCINA", "OZORIO", "GUILERMINA", "TEODOMIRO", "ERNESTINA", "ANESIA",
    "DELMIRA", "ABADIA", "BENIGNO", "EUPIDIO", "OTACILIA", "ORLANDA",
    "VITALINO", "BERNADINO", "TERTULIANO", "ORESTE", "LEVINO", "FLORINDA",
    "CELESTINA", "ERONDINA", "HERCILIA", "EVANGELINA", "CELITA", "JOVENTINO",
    "ROSITA", "ALCINA", "AMBROSIO", "MARCOLINO", "VALDIVINA", "GERALDINA",
    "CARMELINA", "AMERICA", "ADALGIZA", "JULITA", "GUMERCINDO", "GENESIA",
    "OLIVA", "NARCISA", "ORESTES", "EPIFANIO", "HAYDEE", "RUFINO", "ROSALVA",
    "LAURENTINO", "AURELINA", "IGNES", "CELESTINO", "MODESTO", "INOCENCIO",
    "DELFINO", "EMA", "IRACY", "AURELINO", "OSCARINA", "GONCALA", "CORNELIO",
    "FRANCINA", "DILCE", "JOVINA", "AUZIRA", "EMMA", "ZILA", "ADILIA",
    "SANTINO", "VICENCIA", "DJANIRA", "ISIDORO", "CLARINDO", "DOROTEIA",
    "ZORAIDE", "LEONIDA", "ONORIO", "AGNELO", "HERMINIA", "ALTINA",
    "ARGEMIRO", "EDITH", "SANTO", "PERPETUA", "ALMERINDO", "CECI",
    "SANTINA", "CLOTILDE", "ALTAMIRA", "WALDOMIRO", "PIEDADE", "SILVINA",
    "DORACI", "JURACY", "CARMINA", "ESTELINA", "FORTUNATO", "JESUINA",
    "SEVERIANO", "AGRIPINO", "ZULEICA", "CONSTANTINO", "BERTA", "URBANO",
    "ETELVINA", "ODILIA", "CARLINDA", "DAVINA", "DARCY", "IRENA", "MOACYR",
    "PALMIRA", "HONORIO", "ALVINA", "JUSTINA", "JOVITA", "FRANCELINA",
    "CARMELIA", "CREMILDA", "FLORENCIO", "OSORIO", "JOVELINO", "ARMINDA",
    "DIONISIA", "DINORA", "ANIZIA", "CARMELA", "CLAUDINA", "FELICIANA",
    "CONSUELO", "JOVINO", "OVIDIO", "ARACI", "SANTA", "BELMIRO",
    "CONSTANCIA", "JACY", "DALVINA", "BERNARDINO", "NELLY", "SERAFIM",
    "ELPIDIO", "OLIMPIA", "BENTA", "CLELIA", "ANESIO", "JOSINA", "ARMINDO",
    "ERMINIA", "CARLOTA", "ENEDINA", "JUDITH", "LAUDELINO", "GEORGINA",
    "JOSEFINA", "IRMA", "EUVIRA", "MARTINHA", "HERMINIO", "CUSTODIO",
    "ADALGISA", "ZUMIRA", "FRIDA", "ALMIRA", "IDA", "JORGINA", "CLARINDA",
    "JOVELINA", "LAURITA", "MERCEDES", "CLEMENTE", "GUIOMAR", "OTILIA",
    "EFIGENIA", "DAGMAR", "EULINA", "DEJANIRA", "LEONILDA", "LUCINDA",
    "DIRCE", "WALDEMAR", "ANISIA", "DOLORES", "THEREZA", "ESTELITA",
    "ELSA", "FILOMENA", "EURIDES", "ERCILIA", "CORINA", "ONOFRE",
    "ALMERINDA", "JUREMA", "GENTIL", "LAURINDA", "ARLINDA", "LINDAURA",
    "GENI", "JOAQUINA", "LEONOR", "TEODORA", "JACI", "AVELINO",
    "OLINDA", "ALBINO", "MARIETA", "ARISTIDES", "OLIMPIO", "ANTONIETA",
    "ADELINA", "GERALDA", "ALBERTINA", "MATILDE", "ALEXANDRINA",
    "LAZARA", "IDALINA", "NADIR", "SEVERINA", "ELVIRA", "TERESINHA",
    "GUILHERMINA", "INACIA", "AUGUSTA", "ODETE", "CARMELITA", "OSWALDO",
    "EDITE", "DIVA", "JULIETA", "IRACI", "IZAURA", "ALZIRA", "ZILDA",
    "AURORA", "JUDITE", "NORMA", "CANDIDA", "JANDIRA", "NEUZA",
    "ROSALINA", "NILZA", "ALAIDE", "ADELAIDE", "HILDA", "IRACEMA", "ILDA",
    "NAIR", "MARGARIDA", "ISAURA", "ELZA", "TEREZINHA", "BENEDITA",
    "AMELIA", "SEBASTIANA", "OLGA", "CONCEICAO", "IRENE", "RAIMUNDA",
]
# Lista de nomes de batismo mais comuns.
nomes_comuns_lista = [
    "Jose", "Joao", "Antonio", "Francisco", "Carlos", "Paulo", "Pedro",
    "Lucas", "Luiz", "Marcos", "Luis", "Gabriel", "Rafael", "Daniel",
    "Marcelo", "Bruno", "Eduardo", "Felipe", "Raimundo", "Rodrigo",
    "Maria", "Jose", "Ana", "Joao", "Antonio", "Francisco", "Carlos",
    "Paulo", "Pedro", "Lucas", "Luiz", "Marcos", "Luis", "Gabriel",
    "Rafael", "Francisca", "Daniel", "Marcelo", "Bruno", "Eduardo",
]

# Cria uma lista de padrões para o EntityRuler
patterns = [{"label": "PESSOA", "pattern": name} for name in set(nomes_personalizados + nomes_comuns_lista)]

# Carrega o modelo base do spaCy em português
nlp = spacy.load("pt_core_news_sm")

# Cria o EntityRuler e adiciona os padrões personalizados
ruler = nlp.add_pipe("entity_ruler", before="ner")
ruler.add_patterns(patterns)

# Texto de exemplo (com nomes da sua lista)
texto_exemplo = (
    "A documentação foi assinada por Moacyr e Celsa. "
    "A equipe de trabalho é composta por Maria, Carlos, e um especialista chamado Amândio. "
    "O responsável é o senhor Adalberto, que não está na sua lista."
)

# Processa o texto com o pipeline atualizado
doc = nlp(texto_exemplo)

# Itera sobre as entidades e imprime o texto e o rótulo
print("Entidades encontradas no texto:")
for ent in doc.ents:
    if ent.label_ == "PESSOA":
        print(f"Tipo: {ent.label_:<5} | Texto: {ent.text}")