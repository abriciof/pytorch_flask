import io
import torch 
import torch.nn as nn 
import torchvision.transforms as transforms 
from PIL import Image

def transform_image(image_bytes):
    transform = transforms.Compose([transforms.Resize((32,32)),
                                    transforms.CenterCrop(32),
                                    transforms.ToTensor()])

    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)