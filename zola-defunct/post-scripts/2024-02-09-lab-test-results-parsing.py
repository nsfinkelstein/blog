import torch
from transformers import TableTransformerForObjectDetection

# new v1.1 checkpoints require no timm anymore
device = 'cuda' if torch.cuda.is_available() else 'cpu'

structure_model = TableTransformerForObjectDetection.from_pretrained(
    'microsoft/table-structure-recognition-v1.1-all'
)

structure_model = TableTransformerForObjectDetection.from_pretrained(
    'microsoft/table-structure-recognition-v1.1-all'
)
structure_model.to(device)
print('')
