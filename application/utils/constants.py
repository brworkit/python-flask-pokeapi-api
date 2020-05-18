from os import environ
APP_TOKEN = environ["APP_TOKEN"] 
PARAMS_DEFAULT={"sourceId": environ["SOURCE_ID"]} 

TOP_CATEGORIES = [
    {"id": 99002, "name": "Eletrônicos"},
    {"id": 99008, "name": "Saúde e Beleza"},
    {"id": 77, "name": "Celular/Smartphone"},
    {"id": 99004, "name": "Moda e Acessórios"},
    {"id": 3482, "name": "Livros"},
    {"id": 99007, "name": "Casa e Decoração"},
    {"id": 99005, "name": "Esportes e Lazer"},
    {"id": 6409, "name": "Games"},
    {"id": 99003, "name": "Eletrodomésticos"}
]


TOP_STORES = [
    {"name": "Amazon", "id": 5992},
    {"name": "Americanas", "id": 5632},
    {"name": "Netshoes", "id": 5783},
    {"name": "Submarino", "id": 5766},
    {"name": "Positivo", "id": 6117},
    {"name": "Shoptime", "id": 5644},
    {"name": "Livraria Cultura", "id": 5876},
    {"name": "Brastemp", "id": 5936},
    {"name": "Consul", "id": 5937},
    {"name": "TNG", "id": 6076},
    {"name": "Electrolux", "id": 6078},
    {"name": "Aramis", "id": 6110},
    {"name": "KitchenAid", "id": 6227},
    {"name": "Zattini", "id": 5953},
    {"name": "+Barato", "id": 6360},
    {"name": "iRobot", "id": 6209},
    {"name": "CentralAr", "id": 6144},
    {"name": "Baitashop", "id": 6599},
    {"name": "Found IT", "id": 6433},
    {"name": "Color Brinque", "id": 6592},
    {"name": "Zona Cerealista", "id": 6247},
    {"name": "Vhita", "id": 6481},
    {"name": "Descomplica", "id": 6577}
]