import argparse
import sys

from src.BlinkRunner import BlinkRunner


def parse_boolean(value):
    value = value.lower()

    if value in ["true", "yes", "y", "1", "t"]:
        return True
    elif value in ["false", "no", "n", "0", "f"]:
        return False

    return False


def main(argv):
    parser = argparse.ArgumentParser(description="A program that accepts one string and two boolean values.")
    parser.add_argument("--camera_system", help="Camera system brand [blink]")
    parser.add_argument("--interval", type=int, default=60, help="How often an image should be pulled for object detection (Recommended >30")
    parser.add_argument("--threshold", type=float, default=0.5, help="Object detection confidence threshold to display bounding box")
    parser.add_argument("--display", type=parse_boolean, default=False, help="Images with bounding box will appear at interval")
    parser.add_argument("--sms", type=parse_boolean, default=False, help="Text of object detected will be sent if AWS configured")
    parser.add_argument("--phone", help="Phone number for SMS to be sent to, refer to README")
    parser.add_argument("--profile", help="Credentials profile for supported cloud envs [AWS]")
    args = parser.parse_args()

    if args.camera_system == 'blink':
        BlinkRunner.run(interval=args.interval,
                        threshold=args.threshold,
                        display=args.display,
                        profile=args.profile,
                        sms=args.sms,
                        phone=args.phone)


if __name__ == "__main__":
    main(sys.argv[1:])
