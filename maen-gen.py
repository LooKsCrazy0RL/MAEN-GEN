import os
import time
import sys
import random
from faker import Faker

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"
    RED = "\033[31m"

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner_ascii():
    banner_lines = [
        "███╗   ███╗ █████╗ ███████╗███╗  ██╗",
        "████╗ ████║██╔══██╗██╔════╝████╗ ██║",
        "██╔████╔██║███████║█████╗  ██╔██╗██║",
        "██║╚██╔╝██║██╔══██║██╔══╝  ██║╚████║",
        "██║ ╚═╝ ██║██║  ██║███████╗██║ ╚███║",
        "╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚══╝"
    ]
    colors = [Colors.CYAN, Colors.BLUE, Colors.MAGENTA, Colors.RED, Colors.YELLOW, Colors.GREEN]
    for i, line in enumerate(banner_lines):
        print(colors[i % len(colors)] + line + Colors.RESET)
        time.sleep(0.1)

def animacion_inicio():
    clear()
    slow_print(Colors.GREEN + "[*] Iniciando MAEN..." + Colors.RESET, 0.05)
    time.sleep(0.5)
    slow_print(Colors.CYAN + "[*] Cargando módulos..." + Colors.RESET, 0.05)
    time.sleep(0.5)
    slow_print(Colors.YELLOW + "[*] Conectando con servidores..." + Colors.RESET, 0.05)
    time.sleep(0.8)
    slow_print(Colors.GREEN + "[✔] Todo listo!" + Colors.RESET, 0.05)
    time.sleep(0.5)
    clear()
    banner_ascii()
    time.sleep(0.5)

def barra_carga():
    for i in range(1, 21):
        sys.stdout.write(f"\r{Colors.YELLOW}Cargando: [{'#' * i}{'.' * (20 - i)}] {i*5}%{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def generar_tarjetas_aleatorias():
    cantidad = int(input("▶ Cantidad de tarjetas a generar: "))
    barra_carga()
    for _ in range(cantidad):
        tarjeta = "".join(str(random.randint(0, 9)) for _ in range(16))
        mes = str(random.randint(1, 12)).zfill(2)
        anio = str(random.randint(2025, 2030))
        cvv = str(random.randint(100, 999))
        print(f"{tarjeta}|{mes}|{anio}|{cvv}")

def generar_fake_data():
    paises = {
        "MX": "es_MX", "ES": "es_ES", "US": "en_US", "BR": "pt_BR", "FR": "fr_FR",
        "IT": "it_IT", "DE": "de_DE", "RU": "ru_RU", "CN": "zh_CN", "JP": "ja_JP",
        "KR": "ko_KR", "AR": "es_AR", "CL": "es_CL", "CO": "es_CO", "VE": "es_VE",
        "PE": "es_PE", "CA": "en_CA", "IN": "en_IN", "AU": "en_AU", "ZA": "en_ZA"
    }
    print(f"{Colors.CYAN}Paises disponibles:{Colors.RESET}")
    for k in paises:
        print(f"{k} ", end="")
    print()
    pais = input("▶ Código de país: ").upper()
    if pais not in paises:
        print("País no válido.")
        return
    fake = Faker(paises[pais])
    cantidad = int(input("▶ Cantidad de perfiles: "))
    barra_carga()
    for _ in range(cantidad):
        nombre = fake.name()
        direccion = fake.address().replace("\n", ", ")
        email = fake.email()
        telefono = fake.phone_number()
        tarjeta = fake.credit_card_number()
        fecha_exp = fake.credit_card_expire()
        cvv = fake.credit_card_security_code()
        print(f"{nombre} | {direccion} | {email} | {telefono} | {tarjeta}|{fecha_exp}|{cvv}")

def generar_con_bin():
    bin_input = input("▶ Ingresa BIN (6-16 dígitos): ").strip()
    mes_op = input("▶ Mes (MM) o R para random: ").upper()
    anio_op = input("▶ Año (YYYY) o R para random: ").upper()
    cvv_op = input("▶ CVV o R para random: ").upper()
    cantidad = int(input("▶ Cantidad de tarjetas: "))
    barra_carga()
    for _ in range(cantidad):
        tarjeta = bin_input + "".join(str(random.randint(0, 9)) for _ in range(16 - len(bin_input)))
        mes = mes_op if mes_op != "R" else str(random.randint(1, 12)).zfill(2)
        anio = anio_op if anio_op != "R" else str(random.randint(2025, 2030))
        cvv = cvv_op if cvv_op != "R" else str(random.randint(100, 999))
        print(f"{tarjeta}|{mes}|{anio}|{cvv}")

def generar_bins():
    print(f"{Colors.CYAN}Tipos de tarjeta:{Colors.RESET}")
    print("1. Visa\n2. MasterCard\n3. Amex\n4. Discover")
    tipo = input("▶ Elige el tipo (1-4): ").strip()
    cantidad = int(input("▶ Cantidad de BINs a generar: "))
    barra_carga()
    for _ in range(cantidad):
        if tipo == "1":
            inicio = "4"
            longitud = 6
        elif tipo == "2":
            inicio = "5"
            longitud = 6
        elif tipo == "3":
            inicio = "3"
            longitud = 6
        elif tipo == "4":
            inicio = "6"
            longitud = 6
        else:
            print("Tipo inválido.")
            return
        bin_generado = inicio + "".join(str(random.randint(0, 9)) for _ in range(longitud - 1))
        print(bin_generado)

def interfaz_principal():
    clear()
    banner_ascii()
    print(f"""{Colors.BOLD}{Colors.CYAN}
╔══════════════════════════════════════════════════════╗
║ 💳   M A E N   G E N   💳                           ║
║ Creador: {Colors.YELLOW}@LooKsCrazy0{Colors.CYAN}  | Canal: {Colors.YELLOW}@AN0M4LY_404       {Colors.CYAN}║
╚══════════════════════════════════════════════════════╝
{Colors.RESET}""")
    print(f"""
{Colors.GREEN}[1]{Colors.RESET} 💳 Generar tarjetas aleatorias
{Colors.GREEN}[2]{Colors.RESET} 👤 Generar Fake Data
{Colors.GREEN}[3]{Colors.RESET} 💳 Generar con BIN personalizado
{Colors.GREEN}[4]{Colors.RESET} 🔢 Generador de BIN
""")
    return input(f"{Colors.YELLOW}▶ Elige una opción: {Colors.RESET}")

if __name__ == "__main__":
    animacion_inicio()
    while True:
        op = interfaz_principal()
        if op == "1":
            generar_tarjetas_aleatorias()
        elif op == "2":
            generar_fake_data()
        elif op == "3":
            generar_con_bin()
        elif op == "4":
            generar_bins()
        else:
            print("Opción inválida.")
        input(f"{Colors.YELLOW}Presiona Enter para continuar...{Colors.RESET}")