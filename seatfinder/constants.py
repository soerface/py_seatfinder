from pathlib import Path

SCRIPT_URL = {
    'Karlsruhe': 'https://seatfinder.bibliothek.kit.edu/karlsruhe/getdata.php',
    'Geneva': 'https://seatfinder.bibliothek.kit.edu/unige/getdata.php',
    'Kassel': 'https://seatfinder.bibliothek.kit.edu/kassel/getdata.php',
    'St. Gallen': 'https://seatfinder.bibliothek.kit.edu/unisg_v2/getdata.php',
    'Tuebingen': 'https://seatfinder.bibliothek.kit.edu/tuebingen/getdata.php',
}

LOCATIONS = {
    'Karlsruhe': [
        'LSG',
        'LSM',
        'LST',
        'LSN',
        'LSW',
        'LBS',
        'BIB-N',
        'FBC',
        'FBP',
        'LAF',
        'FBA',
        'FBI',
        'FBM',
        'FBW',
        'FBH',
        'FBD',
        'TheaBib',
        'BLB',
        'WIS',
    ],
    'Geneva': [
        'ARVE',
        'MATHS',
        'ISE',
        'TERRE',
        'OBS',
        'BATELLED',
        'BC',
        'PHILOSOPHES',
        'JURA',
        'CMU',
        'MAIL',
    ],
    'Kassel': [
        'UBA0EP',
        'UBA1EP',
        'UBA2EP',
        'UBA3EP',
        'UBB0EP',
        'UBB0GP',
        'UBB1EP',
        'UBB1GP',
        'UBB2EP',
        'UBB2GP',
        'LeoEG',
        'LeoOG',
    ],
    'St. Gallen': [
        'BIB_EG',
        'BIB_OG',
        '09-116',
        '01_212',
        '01_311',
        'theCO',
        'ZIG_TH',
        'ZIG_Caf',
        'FHS_Bib',
        'KBV_HP',
        'ex_Bie',
    ],
    'Tuebingen': [
        'UBH1',
        'UBB2',
        'UBB2HLS',
        'UBA3A',
        'UBA3C',
        'UBA4A',
        'UBA4B',
        'UBA4C',
        'UBA5A',
        'UBA5B',
        'UBA5C',
        'UBA6A',
        'UBA6B',
        'UBA6C',
        'UBWZA',
        'UBWZB',
        'UBNEG',
        'UBCEG',
        'UBCUG',
        'UBLZN',
    ]
}

DATA_DIR = Path.home() / '.seatfinder/data'
