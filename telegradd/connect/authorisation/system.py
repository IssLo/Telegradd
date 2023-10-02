from __future__ import annotations

import random
from typing import List, Dict, Tuple, TypeVar, Type
import hashlib, os


class DeviceInfo:
    def __init__(self, model, system, app):
        self.app = app
        self.system = system
        self.model = model

    def __str__(self) -> str:
        return f"{self.model} {self.system} {self.app}"

    def return_system(self):
        return self.model, self.system, self.app




class GeneralDesktopDevice():

    device_models = [
        "PC 64bit",
        "PC 64bit"
        "0133D9",
        "03X0MN",
        "04GJJT",
        "04VWF2",
        "04WT2G",
        "05DN3X",
        "05FFDN",
        "0679",
        "0692FT",
        "06CDVY",
        "07JNH0",
        "0841B1A",
        "0874P6",
        "08VFX1",
        "095TWY",
        "09DKKT",
        "0C1D71",
        "0GDG8Y",
        "0H0CC0",
        "0H869M",
        "0J797R",
        "0JC474",
        "0KM92T",
        "0KP0FT",
        "0KV3RP",
        "0KWVT8",
        "0M277C",
        "0M332H",
        "0M9XW4",
        "0MYG77",
        "0N7TVV",
        "0NWWY0",
        "0P270J",
        "0PD9KD",
        "0PPYW4",
        "0R1203",
        "0R849J",
        "0T105W",
        "0TP406",
        "0U785D",
        "0UU795",
        "0WCNK6",
        "0Y2MRG",
        "0YF8P5",
        "1005P",
        "1005PE",
        "10125",
        "103C_53307F",
        "103C_53307F G=D",
        "103C_53311M HP",
        "103C_53316J",
        "103C_53316J G=D",
        "103C_5335KV",
        "103C_5336AN",
        "1066AWU",
        "110-050eam",
        "122-YW-E173",
        "131-GT-E767",
        "1425",
        "1494",
        "1496",
        "1633",
        "181D",
        "1849",
        "18F9",
        "198C",
        "1998",
        "20060",
        "20216",
        "20245",
        "20250",
        "20266",
        "20351",
        "20384",
        "20ATCTO1WW",
        "20AWA161TH",
        "20BECTO1WW",
        "20HD005EUS",
        "20HES2SF00",
        "20V9",
        "2166",
        "216C",
        "2248",
        "22CD",
        "2349G5P",
        "2378DHU",
        "2A9A",
        "2AB1",
        "2AC8",
        "2AE0",
        "304Bh",
        "3060",
        "30B9",
        "30DC",
        "30F7",
        "3600",
        "3624",
        "3627",
        "3642",
        "3646h",
        "3679CTO",
        "3717",
        "4157RC2",
        "4313CTO",
        "500-056",
        "600-1305t",
        "600-1370",
        "60073",
        "740U5L",
        "765802U",
        "80B8",
        "80C4",
        "80D0",
        "80E3",
        "80E5",
        "80E9",
        "80FC",
        "80RU",
        "80S7",
        "80Y7",
        "8114",
        "81DE",
        "81EF",
        "81H9",
        "81MU",
        "81VV",
        "8216",
        "8217",
        "82KU",
        "838F",
        "843B",
        "844C",
        "84A6",
        "84DA",
        "8582",
        "86F9",
        "8786",
        "8I945PL-G",
        "90NC001MUS",
        "90NC00JBUS",
        "945GT-GN",
        "965P-S3",
        "970A-G/3.1",
        "980DE3/U3S3",
        "990FXA-UD3",
        "A320M-S2H",
        "A320M-S2H-CF",
        "A55M-DGS",
        "A58MD",
        "A78XA-A2T",
        "A7DA 3 series",
        "A88X-PLUS",
        "AB350 Gaming K4",
        "AO533",
        "ASUS MB",
        "AX3400",
        "Acer Desktop",
        "Acer Nitro 5",
        "Alienware",
        "Alienware 17",
        "Alienware 17 R2",
        "Alienware 18",
        "Alienware X51",
        "Alienware m15",
        "All Series",
        "Aspire 4520",
        "Aspire 4736Z",
        "Aspire 5",
        "Aspire 5250",
        "Aspire 5252",
        "Aspire 5536",
        "Aspire 5538G",
        "Aspire 5732Z",
        "Aspire 5735",
        "Aspire 5738",
        "Aspire 5740",
        "Aspire 6930G",
        "Aspire 8950G",
        "Aspire A515-51G",
        "Aspire E5-575G",
        "Aspire M3641",
        "Aspire M5-581T",
        "Aspire M5-581TG",
        "Aspire M5201",
        "Aspire M5802",
        "Aspire M5811",
        "Aspire M7300",
        "Aspire R5-571TG",
        "Aspire T180",
        "Aspire V3-574G",
        "Aspire V5-473G",
        "Aspire V5-552P",
        "Aspire VN7-792G",
        "Aspire X1301",
        "Aspire X1700",
        "Aspire X3400G",
        "Aspire one",
        "Asterope",
        "Aurora",
        "Aurora R5",
        "Aurora-R4",
        "B360M D3H-CF",
        "B360M-D3H",
        "B450M DS3H",
        "B450M DS3H-CF",
        "B550 MB",
        "B550M DS3H",
        "B560 MB",
        "B560M DS3H",
        "B85M-D2V",
        "B85M-G",
        "BDW",
        "Boston",
        "Burbank",
        "C40",
        "CELSIUS R640",
        "CG1330",
        "CG5290",
        "CG8270",
        "CM1630",
        "CathedralPeak",
        "Charmander_KL",
        "CloverTrail",
        "Cuba MS-7301",
        "D102GGC2",
        "D900T",
        "D945GCL",
        "DG41WV",
        "DH61WW",
        "DH67CL",
        "DH77EB",
        "DP55WB",
        "DT1412",
        "DX4300",
        "DX4831",
        "DX4860",
        "DX58SO",
        "Dazzle_RL",
        "Default string",
        "Dell DM061",
        "Dell DV051",
        "Dell DXC061",
        "Dell XPS420",
        "Dell XPS720",
        "Desktop",
        "Dimension 3000",
        "Dimension 4700",
        "Dimension E521",
        "Durian 7A1",
        "EP35-DS3",
        "EP35-DS3R",
        "EP35-DS4",
        "EP35C-DS3R",
        "EP43-DS3L",
        "EP45-DS3L",
        "EP45-UD3L",
        "EP45-UD3LR",
        "EP45-UD3P",
        "EP45-UD3R",
        "EP45T-UD3LR",
        "ET1831",
        "EX58-UD3R",
        "Eee PC",
        "Eureka3",
        "Extensa 5620",
        "Extensa 7620",
        "F2A88X-D3HP",
        "F5SL",
        "F71IX1",
        "FJNB215",
        "FM2A88X Pro3+",
        "FMCP7AM&#160;",
        "Freed_CFS",
        "G1.Assassin2",
        "G31M-ES2L",
        "G31MVP",
        "G31T-M2",
        "G33M-DS2R",
        "G41M-Combo",
        "G41M-ES2L",
        "G41MT-S2P",
        "G53JW",
        "G53SW",
        "G55VW",
        "G60JX",
        "G73Sw",
        "GA-73PVM-S2H",
        "GA-770T-USB3",
        "GA-78LMT-S2P",
        "GA-78LMT-USB3",
        "GA-790FXTA-UD5",
        "GA-870A-UD3",
        "GA-880GM-D2H",
        "GA-880GM-UD2H",
        "GA-880GM-USB3",
        "GA-880GMA-USB3",
        "GA-890GPA-UD3H",
        "GA-890XA-UD3",
        "GA-970A-D3",
        "GA-EA790X-DS4",
        "GA-MA74GM-S2H",
        "GA-MA770-UD3",
        "GA-MA770T-UD3",
        "GA-MA770T-UD3P",
        "GA-MA785GM-US2H",
        "GA-MA785GT-UD3H",
        "GA-MA78G-DS3H",
        "GA-MA78LM-S2H",
        "GA-MA790FX-DQ6",
        "GA-MA790X-DS4",
        "GA-MA790X-UD4",
        "GA401IV",
        "GA502IU",
        "GE60 2OC\\2OE",
        "GF8200E",
        "GL502VMK",
        "GL502VML",
        "GL552VW",
        "GL553VD",
        "GT5636E",
        "GT5654",
        "GT5674",
        "GT70 2OC/2OD",
        "Gateway Desktop",
        "Gateway M280",
        "Godzilla-N10",
        "H110M-A/M.2",
        "H110M-DVS R3.0",
        "H55-USB3",
        "H55M-S2V",
        "H61M-C",
        "H61M-HVS",
        "H61MXL/H61MXL-K",
        "H67M-D2-B3",
        "H81H3-AM",
        "H81M-D PLUS",
        "H87-D3H",
        "H87-D3H-CF",
        "H87-HD3",
        "H97-D3H",
        "H97M Pro4",
        "HP 15",
        "HP 620",
        "HP All-in-One 22-c1xx",
        "HP Compaq 6720s",
        "HP Compaq 8000 Elite SFF",
        "HP Compaq 8100 Elite CMT",
        "HP Compaq 8200 Elite CMT",
        "HP Compaq 8200 Elite USDT",
        "HP Compaq dc7800p Convertible",
        "HP ENVY",
        "HP ENVY 14",
        "HP ENVY 14 Sleekbook",
        "HP ENVY TS m6 Sleekbook",
        "HP ENVY x360 Convertible",
        "HP ENVY x360 m6 Convertible",
        "HP Elite x2 1012 G1",
        "HP EliteBook 6930p",
        "HP EliteBook 8540w",
        "HP EliteDesk 800 G1 SFF",
        "HP G62",
        "HP G70",
        "HP G7000",
        "HP HDX18",
        "HP Laptop 15-da0xxx",
        "HP Pavilion",
        "HP Pavilion 15",
        "HP Pavilion Gaming 690-0xxx",
        "HP Pavilion Gaming 790-0xxx",
        "HP Pavilion P6000 Series",
        "HP Pavilion Sleekbook 14",
        "HP Pavilion dm4",
        "HP Pavilion dv2700",
        "HP Pavilion dv3",
        "HP Pavilion dv4",
        "HP Pavilion dv5",
        "HP Pavilion dv6",
        "HP Pavilion dv7",
        "HP Pavilion g6",
        "HP ProBook 4320s",
        "HP ProBook 450 G2",
        "HP ProBook 4520s",
        "HP ProBook 4530s",
        "HP Spectre x360 Convertible",
        "HPE-498d",
        "HPE-560Z",
        "IDEAPAD",
        "IMEDIA MC 2569",
        "ISKAA",
        "IdeaCentre K330",
        "Infoway",
        "Inspiron",
        "Inspiron 1525",
        "Inspiron 1526",
        "Inspiron 1545",
        "Inspiron 1564",
        "Inspiron 1750",
        "Inspiron 3891",
        "Inspiron 518",
        "Inspiron 5570",
        "Inspiron 560",
        "Inspiron 570",
        "Inspiron 6000",
        "Inspiron 620",
        "Inspiron 660",
        "Inspiron 7559",
        "Inspiron 7720",
        "Inspiron N5010",
        "Inspiron N7010",
        "Intel_Mobile",
        "Ironman_SK",
        "K40ID",
        "K43SA",
        "K46CM",
        "K50AB",
        "K52JB",
        "K53SV",
        "K55VD",
        "K56CM",
        "KL3",
        "KM400A-8237",
        "Kabini CRB",
        "LENOVO",
        "LEONITE",
        "LH700",
        "LIFEBOOK SH561",
        "LNVNB161216",
        "LX6810-01",
        "LY325",
        "Lancer 5A2",
        "Lancer 5B2",
        "Latitude",
        "Latitude 3410",
        "Latitude 5400",
        "Latitude 6430U",
        "Latitude 7420",
        "Latitude 7490",
        "Latitude D630",
        "Latitude E4300",
        "Latitude E5450",
        "Latitude E6330",
        "Latitude E6430",
        "Latitude E6510",
        "Latitude E6520",
        "Lenovo B50-70",
        "Lenovo G50-80",
        "Livermore8",
        "M11x R2",
        "M14xR2",
        "M15x",
        "M17x",
        "M2N-E",
        "M2N-SLI",
        "M2N-X",
        "M3A-H/HDMI",
        "M3A770DE",
        "M3N78-AM",
        "M4A785TD-M EVO",
        "M4A785TD-V EVO",
        "M4A78LT-M",
        "M4A78T-E",
        "M4A79 Deluxe",
        "M4A79XTD EVO",
        "M4A87TD/USB3",
        "M4A89GTD-PRO",
        "M4N68T",
        "M4N98TD EVO",
        "M5640/M3640",
        "M570U",
        "M5A78L LE",
        "M5A78L-M LE",
        "M5A78L-M/USB3",
        "M5A87",
        "M5A88-V EVO",
        "M5A97",
        "M5A97 LE R2.0",
        "M5A97 R2.0",
        "M68MT-S2",
        "M750SLI-DS4",
        "M771CUH Lynx",
        "MA51_HX",
        "MAXIMUS V GENE",
        "MCP61PM-AM",
        "MCP73PV",
        "MJ-7592",
        "MS-16GC",
        "MS-1727",
        "MS-17K3",
        "MS-6714",
        "MS-7094",
        "MS-7325",
        "MS-7327",
        "MS-7350",
        "MS-7360",
        "MS-7366",
        "MS-7502",
        "MS-7514",
        "MS-7519",
        "MS-7522",
        "MS-7529",
        "MS-7549",
        "MS-7577",
        "MS-7583",
        "MS-7586",
        "MS-7592",
        "MS-7599",
        "MS-7637",
        "MS-7640",
        "MS-7641",
        "MS-7673",
        "MS-7678",
        "MS-7680",
        "MS-7681",
        "MS-7751",
        "MS-7752",
        "MS-7793",
        "MS-7816",
        "MS-7817",
        "MS-7821",
        "MS-7850",
        "MS-7917",
        "MS-7972",
        "MS-7977",
        "MS-7A34",
        "MS-7A62",
        "MS-7B00",
        "MS-7B46",
        "MS-7C02",
        "MS-7C75",
        "MX8734",
        "Makalu",
        "Mi Laptop",
        "N53SV",
        "N552VX",
        "N55SF",
        "N61Jq",
        "N68-GS3 UCC",
        "N68C-S UCC",
        "N76VZ",
        "N81Vp",
        "NFORCE 680i SLI",
        "NL8K_NL9K",
        "NL9K",
        "NP740U5L-Y03US",
        "NT500R5H-X51M",
        "NUC7i7DNB",
        "NUC7i7DNHE",
        "NV52 Series",
        "NV54 Series",
        "NWQAE",
        "Narra6",
        "Nettle2",
        "Nitro AN515-52",
        "Not Applicable",
        "Notebook PC",
        "OEM",
        "OptiPlex 330",
        "OptiPlex 745",
        "OptiPlex 755",
        "OptiPlex 9010",
        "OptiPlex GX520",
        "P170EM",
        "P170HMx",
        "P35-DS3L",
        "P43-A7",
        "P4M90-M7A",
        "P4P800",
        "P4S-LA",
        "P55-UD4",
        "P55-US3L",
        "P55-USB3",
        "P55A-UD3",
        "P55A-UD3R",
        "P55A-UD4",
        "P55A-UD4P",
        "P55M-UD2",
        "P5E-VM HDMI",
        "P5K PRO",
        "P5N32-E SLI",
        "P5Q SE2",
        "P5Q-PRO",
        "P5QL PRO",
        "P5QL-E",
        "P5QPL-AM",
        "P67A-UD3-B3",
        "P67A-UD4-B3",
        "P67A-UD5-B3",
        "P6T",
        "P6T DELUXE V2",
        "P6T SE",
        "P6X58D PREMIUM",
        "P6X58D-E",
        "P7477A-ABA 751n",
        "P7P55D",
        "P7P55D-E",
        "P7P55D-E LX",
        "P8610",
        "P8H61-M LE/USB3",
        "P8H67-M PRO",
        "P8P67",
        "P8P67 PRO",
        "P8P67-M PRO",
        "P8Z68-V LE",
        "P8Z68-V LX",
        "P8Z68-V PRO",
        "P8Z77-V",
        "P8Z77-V LX",
        "P9X79 LE",
        "PM800-8237",
        "PORTEGE R705",
        "PRIME A320M-K",
        "PRIME B450M-A",
        "PRIME X470-PRO",
        "PRIME Z270-A",
        "PRIME Z390-A",
        "PRIME Z490-V",
        "PWWAA",
        "Polaris_HW",
        "Portable PC",
        "PowerEdge 2950",
        "PowerEdge R515",
        "PowerEdge T420",
        "Precision",
        "Precision 7530",
        "Precision M6500",
        "Proteus IV",
        "QL5",
        "Qosmio X505",
        "R560-LAR39E",
        "ROG",
        "RS690M2MA",
        "RS780HVF",
        "RV415/RV515",
        "S500CA",
        "S550CM",
        "SABERTOOTH P67",
        "SABERTOOTH X58",
        "SAMSUNG ATIV",
        "SG41",
        "SJV50PU",
        "SKL",
        "SM80_HR",
        "SQ9204",
        "STRIKER II NSE",
        "SVE14125CLB",
        "SVE14A25CVW",
        "SX2801",
        "SX2802",
        "Satellite A200",
        "Satellite A215",
        "Satellite A300D",
        "Satellite A500",
        "Satellite A505",
        "Satellite A665",
        "Satellite A665D",
        "Satellite C660",
        "Satellite C855D",
        "Satellite L635",
        "Satellite L650",
        "Satellite P205D",
        "Satellite R630",
        "Shark 2.0",
        "Studio 1458",
        "Studio 1555",
        "Studio 1558",
        "Studio 1747",
        "Studio XPS 1640",
        "Studio XPS 7100",
        "Studio XPS 9100",
        "Suntory_KL",
        "Swift 3",
        "Swift SF314-52",
        "T5212",
        "T5226",
        "T9408UK",
        "TA790GX 128M",
        "TA790GX A3+",
        "TA790GXB3",
        "TA790GXE",
        "TA790GXE 128M",
        "TA990FXE",
        "TM1963",
        "TPower I55",
        "TZ77XE3",
        "ThinkPad L440",
        "ThinkPad T430",
        "ThinkPad T440p",
        "ThinkPad T470",
        "ThinkPad T510",
        "ThinkPad T540p",
        "Type1Family",
        "U50F",
        "UD3R-SLI",
        "UL30VT",
        "USOPP_BH",
        "UX303UB",
        "UX32VD",
        "VAIO",
        "VGN-NR498E",
        "VGN-NW265F",
        "VGN-SR45H_B",
        "VIOLET6",
        "VPCEB27FD",
        "VPCEE31FX",
        "VPCF11QFX",
        "VPCF1290X",
        "VPCF22C5E",
        "VPCF22J1E",
        "VPCS111FM",
        "Veriton E430",
        "VivoBook",
        "Vostro",
        "Vostro 1520",
        "Vostro 1720",
        "Vostro1510",
        "W35xSS_370SS",
        "W55xEU",
        "X421JQ",
        "X510UNR",
        "X550CA",
        "X550JX",
        "X555LAB",
        "X556UB",
        "X556UF",
        "X570 GAMING X",
        "X570 MB",
        "X58-USB3",
        "X58A-UD3R",
        "X58A-UD5",
        "X58A-UD7",
        "XPS",
        "XPS 13 9305",
        "XPS 13 9370",
        "XPS 15 9550",
        "XPS 15 9560",
        "XPS 630i",
        "XPS 730",
        "XPS 730X",
        "XPS 8300",
        "XPS 8700",
        "XPS 8940",
        "XPS A2420",
        "XPS L501X",
        "XPS L701X",
        "XPS M1530",
        "YOGA 530-14ARR",
        "YOGA 920-13IKB",
        "YOGATablet2",
        "Yoga2",
        "Z10PE-D8 WS",
        "Z170 PRO GAMING",
        "Z170-E",
        "Z170X-Gaming 5",
        "Z170X-UD3",
        "Z170X-UD3-CF",
        "Z370P D3",
        "Z370P D3-CF",
        "Z68 Pro3",
        "Z68A-D3-B3",
        "Z68A-D3H-B3",
        "Z68AP-D3",
        "Z68MA-D2H-B3",
        "Z68X-UD3H-B3",
        "Z68XP-UD3",
        "Z68XP-UD4",
        "Z77 Pro4",
        "Z77X-D3H",
        "Z87 Extreme6",
        "Z87-D3HP",
        "Z87-D3HP-CF",
        "Z87M Extreme4",
        "Z87N-WIFI",
        "Z87X-OC",
        "Z87X-OC-CF",
        "Z87X-UD4H",
        "Z97-A",
        "Z97-A-USB31",
        "Z97-AR",
        "Z97-C",
        "Z97-PRO GAMER",
        "Z97X-Gaming 7",
        "eMachines E725",
        "h8-1070t",
        "h8-1534",
        "imedia S3720",
        "ixtreme M5800",
        "p6654y",
        "p6710f",
    ]


class WindowsDevice(GeneralDesktopDevice):
    system_versions = ["Windows 10", "Windows 8", "Windows 8.1", "Windows 7", "Windows 11"]
    app_versions = ['4.9.7 x64', '4.9.7 x64', '4.9.6 x64', '4.9.4 x64', '4.9.2 x64', '4.9.1 x64', '4.8.10 x64',
                    '4.8.9 x64', '4.8.8 x64', '4.8.7 x64', '4.8.3 x64', '4.8.1 x64', '4.8.0 x64', '4.7.1 x64',
                    '4.7.0 x64', '4.6.5 x64', '4.6.3 x64', '4.6.1 x64', '4.5.3 x64', '4.5.2 x64', '4.4.1 x64']

    @property
    def device_list(self):
        dev = DeviceInfo(random.choice(GeneralDesktopDevice.device_models),
                                                    random.choice(WindowsDevice.system_versions),
                                                    random.choice(WindowsDevice.app_versions)).return_system()
        return f'{dev[0]}:{dev[1]}:{dev[2]}'






