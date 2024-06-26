import numpy as np
from typing import Any, Tuple
from torch.utils.data import Dataset
from PIL import Image

class MyCIFAR10(Dataset):
    def __init__(self, data, target, transform=None, target_transform=None):
        super().__init__()
        self.data = data
        self.target = target
        self.transform = transform
        self.target_transform = target_transform
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index: int) -> Tuple[Any, Any]:

        img, target = self.data[index], self.target[index]

        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target