"""Create print-ready QR assets after the final site address is known."""
import sys
from urllib.parse import urlparse
try:
    import qrcode
    import qrcode.image.svg
except ImportError:
    raise SystemExit("Install the generator first: python -m pip install 'qrcode[pil]'")
if len(sys.argv) != 2:
    raise SystemExit('Usage: python tools/make_qr.py https://YOUR-PUBLISHED-SITE/')
url = sys.argv[1]
p = urlparse(url)
if p.scheme != 'https' or not p.netloc or 'YOUR-' in url:
    raise SystemExit('Supply the actual published HTTPS website address.')
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=14, border=4)
qr.add_data(url)
qr.make(fit=True)
qr.make_image(fill_color='black', back_color='white').save('open-house-qr.png')
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save('open-house-qr.svg')
print('Created open-house-qr.png and open-house-qr.svg for ' + url)
