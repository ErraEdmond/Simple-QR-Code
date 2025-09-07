import qrcode 
import qrcode.constants

def create_qr_code(data: str, file_name: str, back_color = 'white', fill_color = 'black') -> None:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L, 
                       version=1,
                        box_size=10, 
                        border=1)

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color = fill_color, back_color = back_color)
    img.save(f'{file_name}.png')

create_qr_code(data='https://www.youtube.com/watch?v=2yTlvPSIePs', 
               file_name='qr_gu',
                back_color = (20,41,52))





