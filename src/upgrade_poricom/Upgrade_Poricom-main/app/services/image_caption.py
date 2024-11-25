from transformers import VisionEncoderDecoderModel, AutoFeatureExtractor, AutoTokenizer
import torch
from PIL import Image
# from ..utils.constants import SETTINGS_FILE_DEFAULT
# import configparser

class ImageCaptioning:
    def __init__(self, model_name="nlpconnect/vit-gpt2-image-captioning", device=None, max_length=16, num_beams=4):
        # Load the model, processor, and tokenizer
        self.model = VisionEncoderDecoderModel.from_pretrained(model_name)
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Set device (default: CUDA if available, otherwise CPU)
        self.device = torch.device(device if device else ("cuda" if torch.cuda.is_available() else "cpu"))
        self.model.to(self.device)
        
        # Generation settings
        self.max_length = max_length
        self.num_beams = num_beams
    
    def predict(self, image_paths):
        # Preprocess images
        images = []
        for image_path in image_paths:
            i_image = Image.open(image_path)
            if i_image.mode != "RGB":
                i_image = i_image.convert(mode="RGB")
            images.append(i_image)
        
        # Extract features
        pixel_values = self.feature_extractor(images=images, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(self.device)
        
        # Generate captions
        output_ids = self.model.generate(pixel_values, max_length=self.max_length, num_beams=self.num_beams)
        preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        return [pred.strip() for pred in preds]

# config = configparser.ConfigParser()
# config.read('/home/jin/Poricom-main/app/assets/images/home.png')
# explain_image_path = config["General"]["Explain_image_path"]
# print("Explain_image_path:", '/home/jin/Poricom-main/app/assets/images/home.png')
# captioner = ImageCaptioning(max_length=20, num_beams=5)
# captions = captioner.predict(['/home/jin/Poricom-main/app/assets/images/home.png'])
# print(captions)
