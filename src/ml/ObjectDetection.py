from transformers import DetrFeatureExtractor, DetrForObjectDetection
import torchvision.transforms as T
import torch as th


class ObjectDetection:
    """Class to handle loading the object detection model."""

    def __init__(self):
        self.feature_extractor = DetrFeatureExtractor.from_pretrained('facebook/detr-resnet-50')
        self.model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')

    def preprocess(self, image):
        transform = T.Compose([
            T.ToTensor(),
            T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        img_tens = transform(image).unsqueeze(0)
        return img_tens

    def detect(self, image):
        img_tens = self.preprocess(image)

        with th.no_grad():
            outputs = self.model(img_tens)

        return outputs

    def postprocess(self, image, outputs, threshold=0.9):
        probas = outputs.logits.softmax(-1)[0, :, :-1]
        keep = probas.max(-1).values > threshold

        target_sizes = th.tensor(image.size[::-1]).unsqueeze(0)
        postprocessed_outputs = self.feature_extractor.post_process(outputs, target_sizes)
        bboxes_scaled = postprocessed_outputs[0]['boxes'][keep]
        return probas[keep], bboxes_scaled, self.model.config.id2label
