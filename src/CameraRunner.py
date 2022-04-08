from abc import ABC, abstractmethod


class CameraRunner(ABC):

    @abstractmethod
    def run(self, interval=30, threshold=0.5, display=False, profile='default', sms=False, phone=None):
        pass