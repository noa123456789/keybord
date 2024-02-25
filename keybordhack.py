import random
import time
import pyautogui
import usb.core
import usb.util

# Functie om willekeurige getallen te typen
def type_random_numbers():
    while True:
        # Genereer een willekeurig getal tussen 0 en 9 en typ het
        random_number = random.randint(0, 9)
        pyautogui.press(str(random_number))
        time.sleep(0.1)  # Wacht een korte periode voordat het volgende getal wordt getypt

# Functie om te controleren op aangesloten USB-apparaten
def check_usb_connection():
    # Vendor ID en Product ID van het USB-apparaat waarnaar wordt gezocht
    vendor_id = 0x1234
    product_id = 0x5678

    # Zoek naar het USB-apparaat
    device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

    # Als het USB-apparaat is gevonden, voer dan een actie uit
    if device is not None:
        print("USB-apparaat verbonden!")
        # Voer hier de gewenste actie uit
    else:
        print("Wachten op USB-apparaat...")

if __name__ == "__main__":
    # Start een thread om willekeurige getallen te typen
    # (op de achtergrond terwijl we wachten op het USB-apparaat)
    # Zorg ervoor dat pyautogui is geïnstalleerd: pip install pyautogui
    import threading
    typing_thread = threading.Thread(target=type_random_numbers)
    typing_thread.daemon = True  # Zodat de thread stopt wanneer het hoofdprogramma stopt
    typing_thread.start()

    # Blijf controleren op USB-verbindingen
    while True:
        check_usb_connection()
        time.sleep(1)  # Controleer elke seconde opnieuw
