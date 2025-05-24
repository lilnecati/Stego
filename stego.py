#!/usr/bin/env python3

import os
import sys
from PIL import Image
import binascii
import argparse
import magic
import exifread
from stegano import lsb
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import print as rprint
from alive_progress import alive_bar
import time

# Rich console oluştur
console = Console()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    banner = Text(r'''
    /\___/\
   (  o o  )  STEGO v1.0
   (  =^=  ) 
    (--m--)  
    
[ Cat Tools ]''', style="cyan bold")
    
    menu = Text('''
[*] Ana Menü:
1) 🖼️  Resim Analizi
2) 🔍 LSB Steganografi
3) 📋 Metadata Analizi
4) 🔤 String Extraction
5) 🔎 Magic Bytes Kontrolü
6) 🚪 Çıkış
''', style="green")

    panel = Panel(banner + menu, border_style="cyan")
    console.print(panel)

def loading_animation(duration=1):
    with alive_bar(100, title='[cyan]İşleniyor', bar='classic2') as bar:
        for _ in range(100):
            time.sleep(duration/100)
            bar()

def image_analysis(file_path):
    """Resim dosyası analizi"""
    try:
        with Image.open(file_path) as img:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Özellik", style="cyan")
            table.add_column("Değer", style="green")
            
            table.add_row("Resim Boyutu", f"{img.size}")
            table.add_row("Resim Formatı", f"{img.format}")
            table.add_row("Renk Modu", f"{img.mode}")
            table.add_row("Palette", 'Var' if img.palette else 'Yok')
            
            loading_animation()
            console.print("\n[bold green][+][/bold green] Resim Analiz Sonuçları:")
            console.print(table)
    except Exception as e:
        console.print(f"\n[bold red][-] Hata:[/bold red] {str(e)}")

def lsb_analysis(file_path):
    """LSB steganografi analizi"""
    try:
        loading_animation()
        secret = lsb.reveal(file_path)
        if secret:
            console.print(f"\n[bold green][+][/bold green] LSB ile gizlenmiş mesaj bulundu:")
            console.print(Panel(secret, style="green"))
        else:
            console.print("\n[bold yellow][!][/bold yellow] LSB ile gizlenmiş mesaj bulunamadı")
    except Exception as e:
        console.print(f"\n[bold red][-] Hata:[/bold red] {str(e)}")

def metadata_analysis(file_path):
    """Metadata analizi"""
    try:
        with open(file_path, 'rb') as f:
            loading_animation()
            tags = exifread.process_file(f)
            if tags:
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("Metadata", style="cyan")
                table.add_column("Değer", style="green")
                
                for tag in tags.keys():
                    table.add_row(str(tag), str(tags[tag]))
                
                console.print("\n[bold green][+][/bold green] Metadata Bilgileri:")
                console.print(table)
            else:
                console.print("\n[bold yellow][!][/bold yellow] Metadata bulunamadı")
    except Exception as e:
        console.print(f"\n[bold red][-] Hata:[/bold red] {str(e)}")

def string_extraction(file_path):
    """String extraction"""
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            strings = []
            current_string = ''
            
            for byte in content:
                if 32 <= byte <= 126:  # Yazdırılabilir ASCII karakterler
                    current_string += chr(byte)
                elif current_string:
                    if len(current_string) >= 4:  # En az 4 karakter uzunluğunda stringler
                        strings.append(current_string)
                    current_string = ''
            
            loading_animation()
            if strings:
                table = Table(show_header=True, header_style="bold magenta")
                table.add_column("ID", style="cyan", justify="right")
                table.add_column("String", style="green")
                
                for i, s in enumerate(strings, 1):
                    table.add_row(str(i), s)
                
                console.print("\n[bold green][+][/bold green] Bulunan Stringler:")
                console.print(table)
            else:
                console.print("\n[bold yellow][!][/bold yellow] String bulunamadı")
    except Exception as e:
        console.print(f"\n[bold red][-] Hata:[/bold red] {str(e)}")

def magic_bytes_check(file_path):
    """Magic bytes kontrolü"""
    try:
        loading_animation()
        file_type = magic.from_file(file_path)
        mime_type = magic.from_file(file_path, mime=True)
        
        with open(file_path, 'rb') as f:
            header = f.read(8).hex()
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Özellik", style="cyan")
        table.add_column("Değer", style="green")
        
        table.add_row("Dosya Türü", file_type)
        table.add_row("MIME Türü", mime_type)
        table.add_row("İlk 8 Byte (Hex)", header)
        
        console.print("\n[bold green][+][/bold green] Magic Bytes Analiz Sonuçları:")
        console.print(table)
    except Exception as e:
        console.print(f"\n[bold red][-] Hata:[/bold red] {str(e)}")

def get_file_path():
    while True:
        file_path = console.input("\n[bold cyan][?][/bold cyan] Analiz edilecek dosyanın yolunu girin: ")
        if os.path.exists(file_path):
            return file_path
        console.print("[bold red][-][/bold red] Dosya bulunamadı! Tekrar deneyin.")

def main():
    while True:
        clear_screen()
        print_banner()
        
        try:
            choice = console.input("[bold cyan][?][/bold cyan] Seçiminiz (1-6): ")
            if not choice.isdigit() or int(choice) not in range(1, 7):
                console.input("\n[bold red][-][/bold red] Geçersiz seçim! Devam etmek için ENTER'a basın...")
                continue

            choice = int(choice)
            if choice == 6:
                console.print("\n[bold green][*][/bold green] Programdan çıkılıyor...")
                sys.exit(0)

            file_path = get_file_path()
            
            modes = {
                1: image_analysis,
                2: lsb_analysis,
                3: metadata_analysis,
                4: string_extraction,
                5: magic_bytes_check
            }

            console.print(f"\n[bold cyan][*][/bold cyan] {file_path} dosyası analiz ediliyor...")
            modes[choice](file_path)
            
            console.input("\n[bold green][*][/bold green] Devam etmek için ENTER'a basın...")

        except KeyboardInterrupt:
            console.print("\n\n[bold green][*][/bold green] Program kapatılıyor...")
            sys.exit(0)
        except Exception as e:
            console.print(f"\n[bold red][-] Hata:[/bold red] {str(e)}")
            console.input("\n[bold green][*][/bold green] Devam etmek için ENTER'a basın...")

if __name__ == "__main__":
    main() 