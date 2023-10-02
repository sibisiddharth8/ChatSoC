import myLibs as mL

#load env file
mL.env()
#get api from env file
mL.myAi.api_key = mL.os.getenv("api_key")

# Chatbot func. 
def aiChat(qustion):
    model = mL.os.getenv("model")
    response = mL.myAi.Completion.create(
        engine=model,
        prompt=qustion,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.3
    )
    return response.choices[0].text.strip()

# Text to Image
def GenAiImg(text):
    # Initialize
    mL.myAi.api_key = mL.os.getenv("api_key")
    mL.myAi.Model.list()

    #response data
    rData = mL.myAi.Image.create(
        prompt = text,
        n = 1,
        size = '256x256') # Sizes = '256x256' | '512x512' | '1024x1024'

    # Extract Url from Response data
    load_data = mL.json.loads(str(rData))
    eUrl = load_data['data'][0] #eUrl - Extracted Url
    fUrl = eUrl['url'] # Final Url
    
    return fUrl

# Text to Audio
def txtToAud(txtAud):
    # initialize text to speech engine
    engine = mL.pyttsx3.init()

    # set voice properties
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # 0 - Male | 1 - Female
    engine.setProperty('rate',150)

    # convert text to audio
    return engine.say(txtAud),engine.runAndWait()

# Image download from Url
def imgFrUrl(url):
    
    # Send an HTTP GET request to the URL
    response = mL.requests.get(url)
    # Open the response content as a stream of bytes
    image_data = mL.BytesIO(response.content)
    # Create an Image object from the image data
    image = mL.img.open(image_data)
    downloadPath = mL.os.path.expanduser("~")+"/Downloads/{0}".format("Image.jpg")
    # Save the image to a file
    image.save(downloadPath)

# Youtube video download
def ytVidDownload(url):
    path = mL.os.path.expanduser("~")+ mL.os.getenv('downloadPath')
    try:
        yt = mL.yt(url)
        print("Downloading... Please Wait !")

        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        video.download(output_path=path)
        print(f'Downloaded : {yt.title} to {path}')
        print()
    except Exception as e:
        print(f'Error while downloading {url}: {e}')
        print()

#colored text         
def print_color(text, color):
    #difined colors
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m'
    }
    if color not in colors:
        raise ValueError(f"Invalid color '{color}'. Choose from {', '.join(colors.keys())}")
    return(f"{colors[color]}{text}{colors['reset']}")       

def barcode_scan():
    cap = mL.cv2.VideoCapture(0)
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        # Convert the frame to grayscale
        gray = mL.cv2.cvtColor(frame, mL.cv2.COLOR_BGR2GRAY)
        # Use pyzbar to scan the barcode
        barcodes = mL.pyzbar.decode(gray)
        # Loop over the detected barcodes
        for barcode in barcodes:
            # Extract the text and barcode type
            barcode_text = barcode.data.decode("utf-8")
            # Print the results
            cap.release()
            return barcode_text
            # Exit the loop
            break
        # Exit the program if a barcode is detected
        if len(barcodes) > 0:
            break
        # Exit if 'q' is pressed
        if mL.cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    

   








