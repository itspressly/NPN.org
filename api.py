from flask import Flask, request,jsonify, render_template
import qrcode
# import pyzbar
import cv2


# # code =  request.form.get('code') 
c_barcode = 'http://qrco.de/bebUVc'

npn = Flask(__name__)

# @npn.route('/barcode', methods=['POST'])
# @npn.get("/barcode")


# def scan_qr_code():
#     # Initialize the video capture object using the default webcam
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Read a frame from the video stream
#         ret, frame = cap.read()

#         # Convert the frame to grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Use pyzbar to decode the QR codes from the frame
#         decoded_qr_codes = pyzbar.decode(gray)

#         # Loop over the detected QR codes
#         for qr_code in decoded_qr_codes:
#             # Extract the bounding box coordinates of the QR code
#             (x, y, w, h) = qr_code.rect

#             # Draw a rectangle around the QR code
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#             # Extract the data from the QR code
#             data = qr_code.data.decode('utf-8')

#             # Print the data
#             print("Scanned QR code:", data)

#         # Display the frame
#         cv2.imshow('QR Code Scanner', frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and destroy the windows
#     # cap.release()
#     cv2.destroyAllWindows()
#     return decoded_qr_codes, data

def n_barcode(decoded_qr_codes, data):
    # return(f'Sorry, It seems like you are a stranger.')
    if not decoded_qr_codes :
        # return render_template('.incorrect.html')
        return jsonify('The barcode you provided is incorrect.')
    else:
        if c_barcode:
            # return render_template('.index.html')
            print(data)
            return 'Successfully'  #come update later


    
# @npn.get("/correct-code", methods='POST')
# def inc_barcode():
#     if not c_barcode:
#         return render_template('.index.html')


if __name__ == "__main__":
    # scan_qr_code()
    npn.run(port=4620,debug=True)

