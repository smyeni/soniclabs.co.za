#!/usr/bin/env python3
"""
Sonic Home - Gas Specs QR Generator
Engineer-grade, Pi4 compatible
"""

import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# CONFIG
URL = "https://sonicauto.co.za/gas-specs"
OUTPUT_FILE = "sonic_home_gas_qr.png"
QR_SIZE = 10 # box_size
QR_BORDER = 4
CARD_WIDTH = 1200
CARD_HEIGHT = 1600
LABEL = "SONIC HOME"
SUB_LABEL = "TECH DATA PACK"
FOOTER = "Scan for full spec sheet | Stall #[Your Number]"

# COLOURS (engineer aesthetic)
BG = (245, 245, 240) # off-white, paper-like
BLACK = (20, 20, 20)
RED = (180, 40, 40) # safety red for accent
GREY = (100, 100, 100)

def generate_qr():
    """Generate QR code with high error correction"""
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=QR_SIZE,
        border=QR_BORDER,
    )
    qr.add_data(URL)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white").convert("RGB")

def create_card():
    """Build the full card with QR + labels"""
    # Base card
    card = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), BG)
    draw = ImageDraw.Draw(card)

    # Try to load a monospace font, fallback to default
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 64)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", 36)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", 28)
        font_code = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_code = ImageFont.load_default()

    # --- HEADER ---
    draw.text((60, 60), LABEL, fill=BLACK, font=font_large)
    draw.text((60, 140), SUB_LABEL, fill=RED, font=font_medium)
    
    # Red accent line
    draw.rectangle([60, 185, 300, 190], fill=RED)

    # --- QR CODE (centre) ---
    qr_img = generate_qr()
    qr_size = 600
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)
    
    qr_x = (CARD_WIDTH - qr_size) // 2
    qr_y = 280
    card.paste(qr_img, (qr_x, qr_y))

    # --- FOOTER TEXT ---
    draw.text((60, 950), FOOTER, fill=BLACK, font=font_small)

    # --- TECH SPECS MINI-BOX (engineer touch) ---
    specs_y = 1050
    draw.rectangle([60, specs_y, CARD_WIDTH - 60, specs_y + 240], outline=RED, width=2)
    
    spec_lines = [
        "PRESSURE ENVELOPE: CADAC (100%)",
        "REGULATOR: 2.8 kPa fixed | EFV-equipped",
        "CONNECTION: 3/4\" BSP standardised",
        "TESTING: Bubble-test per assembly",
        "STANDARDS: SABS 1237 | SABS 1151 | EN ISO 3834",
        "",
        "Cooker tops: CADAC | Alva | Totai (choice, not substitution)",
    ]
    
    y_offset = specs_y + 30
    for line in spec_lines:
        if "Cooker tops" in line:
            draw.text((80, y_offset), line, fill=GREY, font=font_code)
        elif line == "":
            y_offset += 10
        else:
            draw.text((80, y_offset), line, fill=BLACK, font=font_code)
        y_offset += 32

    # --- URL at bottom ---
    draw.text((60, CARD_HEIGHT - 60), URL, fill=RED, font=font_small)

    # Save
    card.save(OUTPUT_FILE)
    print(f"✅ QR card saved: {OUTPUT_FILE}")
    print(f"📐 Dimensions: {CARD_WIDTH}x{CARD_HEIGHT}px")
    print(f"🔗 URL: {URL}")

if __name__ == "__main__":
    # Install dependencies if missing
    try:
        import qrcode
        import PIL
    except ImportError:
        print("⚠️ Installing missing dependencies...")
        os.system("pip3 install qrcode[pil] Pillow")
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
    
    create_card()
