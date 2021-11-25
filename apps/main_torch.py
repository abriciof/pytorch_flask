import io
import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms 
from PIL import Image

class CNN(nn.Module):
  def __init__(self):
    super().__init__()
    self.conv1 = nn.Conv2d(3, 6, 5)                               
    self.pool = nn.MaxPool2d(2, 2)    
    self.conv2 = nn.Conv2d(6, 16, 5) 
    self.fc1 = nn.Linear(16 * 5 * 5, 120)
    self.fc2 = nn.Linear(120, 84)
    self.fc3 = nn.Linear(84, 4)

  def forward(self, x):
    x = self.pool(F.relu(self.conv1(x)))
    x = self.pool(F.relu(self.conv2(x)))
    x = torch.flatten(x, 1) 
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)
    return x


transform_prediction = transforms.Compose([transforms.Resize((32,32)),
                                        transforms.CenterCrop(32),
                                        transforms.Grayscale(num_output_channels=3),                                         
                                        transforms.ToTensor()])


caminho_modelo = 'static\modelo.pth'
model = CNN()
model.load_state_dict(torch.load(caminho_modelo))
model.eval()
learning_rate = 0.01
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def verifica_imagem(imagem_PIL):
  imagem = transform_prediction(imagem_PIL).unsqueeze(dim=0).to(device)
  prediction = model(imagem)
  resultado = str(torch.argmax(prediction))
  resultados = {
    "tensor(0)": "Fusível",
    "tensor(1)": "Relé",
    "tensor(2)": "Capacitor Eletrolítico",
    "tensor(3)": "LED"
  }
  return resultados.get(resultado, "Nenhum")

#   def transform_image(image_bytes):
#     transform_prediction = transforms.Compose([transforms.Resize((32,32)),
#                                             transforms.CenterCrop(32),
#                                             transforms.Grayscale(num_output_channels=3),                                         
#                                             transforms.ToTensor()])

#     image = Image.open(io.BytesIO(image_bytes))
#     return transform_prediction(image).unsqueeze(0)