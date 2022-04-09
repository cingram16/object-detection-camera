#Object Detection Camera System

###Description: 
This was a fun short project that takes images from a home security camera system, in this case Amazon Blink, 
to run object detection on the images. Most cameras will have some sort of motion detection available to warn
owners of activity happening outside the home. In most cases these systems can't provide much more information
than that, so I thought it'd be cool if the camera system could provide some information on what the actual activity is. 
See below for an example of the system determining there is a dog in direct view of the camera!

![readme.png](./assets/readme.png)

###Disclaimer:
This project uses some technology that I did not create myself.

Facebook Pre-trained Model: found on HuggingFace https://huggingface.co/facebook/detr-resnet-50

Amazon Blink Products: "Blink Wire-Free HS Home Monitoring & Alert Systems" is a trademark owned by Immedia Inc., see www.blinkforhome.com for more information. 

Blinkpy Lib: created by Kevin Fronczak (GitHub: fronzbot) and built off of MattTW's protocol https://github.com/MattTW/BlinkMonitorProtocol

###Installation: 

```
$ git clone https://github.com/cingram16/object-detection-camera.git
$ cd object-detection-camera
$ pip install -r requirements.txt
```

###Usage: 

Note: `blinkpy` calls out being careful with interval of requests to camera system!

Below shows how to run the program. Note, that `camera_system` is really the only required field.
SMS can be configured to send a text if an object meeting the threshold requirement is found. This is
currently setup through an AWS configuration. See SMS transactional messaging for AWS SNS, pay attention
to SMS pricing https://aws.amazon.com/sns/sms-pricing/ . 

```
% python3 run.py -h
usage: run.py [-h] [--camera_system CAMERA_SYSTEM] [--interval INTERVAL] [--threshold THRESHOLD] [--display DISPLAY] [--sms SMS] [--phone PHONE] [--profile PROFILE]

Object detection for a home security system that runs continuously at interval set.

optional arguments:
  -h, --help            show this help message and exit
  --camera_system CAMERA_SYSTEM
                        Camera system brand [blink]
  --interval INTERVAL   How often an image should be pulled for object detection (Recommended >30
  --threshold THRESHOLD
                        Object detection confidence threshold to display bounding box
  --display DISPLAY     Images with bounding box will appear at interval
  --sms SMS             Text of object detected will be sent if AWS configured
  --phone PHONE         Phone number for SMS to be sent to, refer to README
  --profile PROFILE     Credentials profile for supported cloud envs [AWS]
```
