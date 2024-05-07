# import timm
#
# model_names = timm.list_models()
# for i in model_names:
#     print(i)
import torch
print(torch.__version__)
print(torch.cuda.is_available())