import requests
from PyPDF2 import PdfReader

# Read PDF
reader = PdfReader("PDF_input.pdf")
page = reader.pages[0]
text = page.extract_text()

# Text to Audio API (using Voice RSS, for free)
API_KEY = ""    # Use your API Key: http://www.voicerss.org/registration.aspx
URL_ENDPOINT = "http://api.voicerss.org/"
PARAMS = {
    "key": API_KEY,
    "hl": "en-us",
    "src": f"{text}",
    "v": "John"
}
# PARAMS - Refer to the api document: http://www.voicerss.org/api/

response = requests.get(URL_ENDPOINT, params=PARAMS)

# Save mp3 file
with open('Audio_output.mp3', 'wb') as f:
    f.write(response.content)

# 'wb' stands for:
# 'w': Write mode. It allows writing (and overwriting) to the file.
# 'b': Binary mode. It indicates that the file will be treated as a binary file, rather than a text file.


# I copied the code from below. Thank you for sharing.
# https://github.com/ahmedhseif/PDFtoAudioBook
