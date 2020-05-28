import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.start_preview()
    camera.start_recording('foo.h264')
    camera.wait_recording(10)
    camera.stop_preview()
    
    camera.exposure_compensation = 2
    camera.exposure_mode = 'spotlight'
    camera.meter_mode = 'matrix'
    camera.image_effect = 'gpen'
    
    time.sleep(2)
    camera.exif_tags['IFD0.Artist'] = 'Song'
    camera.exif_tags['IFD0.Copyright'] = 'Copyleft Song'
    camera.capture('foo.jpg')
    camera.stop_preview()