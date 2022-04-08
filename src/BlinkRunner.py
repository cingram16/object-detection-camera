import time
from PIL import Image

from blinkpy.blinkpy import Blink
from src.CameraRunner import CameraRunner
from src.ml.ObjectDetection import ObjectDetection
from src.service.AwsSMSService import AwsSMSService
from src.service.ImageService import ImageService


class BlinkRunner(CameraRunner):

    def run(interval=30, threshold=0.5, display=False, profile='default', sms=False, phone=None):
        object_detection = ObjectDetection()
        blink = Blink()
        if blink.start():
            while True:
                send = False
                message = ''
                for name, camera in blink.cameras.items():
                    camera.snap_picture()
                    blink.refresh()
                    camera.image_to_file(f'./assets/{camera.attributes["name"]}.jpg')
                    image = Image.open(open(f'./assets/{camera.attributes["name"]}.jpg', 'rb'))

                    outputs = object_detection.detect(image)
                    probas_keep, bboxes_scaled, classes = object_detection.postprocess(image=image, outputs=outputs,
                                                                                       threshold=threshold)

                    if display:
                        ImageService.show_image(image, probas_keep, bboxes_scaled, classes)

                    message += f"Objects in {name}:\n"
                    print(len(probas_keep) > 0 or send)
                    send = len(probas_keep) > 0 or send
                    for p in probas_keep:
                        cl = p.argmax()
                        message += f'- {classes[cl.item()]} prob: {p[cl]:0.5f}\n'

                print(message)
                if send and sms:
                    sms_service = AwsSMSService()
                    sms_service.send(message=message, phone_number=phone, profile=profile)
                time.sleep(interval)
