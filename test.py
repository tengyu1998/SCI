import os
import sys
import numpy as np
import torch
import argparse
import torch.utils
from PIL import Image
from torch.autograd import Variable
from model_test import Network
from multi_read_data import MemoryFriendlyLoader

parser = argparse.ArgumentParser("sci")
# parser.add_argument('--data_path', type=str, default='./data',
parser.add_argument('--data_path', type=str, default=r'C:\Users\ADMIN\Desktop\SCI\LOL\input',
                    help='location of the test data corpus')
parser.add_argument('--save_path', type=str, default=r'C:\Users\ADMIN\Desktop\SCI\Ours\LOL',
                    help='save location of the data corpus')
parser.add_argument('--model', type=str, default='./model/demo.pt',
                    help='save location of the data corpus')

args = parser.parse_args()
save_path = args.save_path
os.makedirs(save_path, exist_ok=True)

TestDataset = MemoryFriendlyLoader(img_dir=args.data_path, task='test')

test_queue = torch.utils.data.DataLoader(
    TestDataset, batch_size=1,
    pin_memory=True, num_workers=0)


def save_images(tensor, path):
    image_numpy = tensor[0].cpu().float().numpy()
    image_numpy = (np.transpose(image_numpy, (1, 2, 0)))
    im = Image.fromarray(np.clip(image_numpy * 255.0, 0, 255.0).astype('uint8'))
    im.save(path, 'png')


def main():
    if not torch.cuda.is_available():
        print('no gpu device available')
        sys.exit(1)

    model = Network()
    model = model.cuda()
    model_dict = torch.load(args.model, map_location='cuda:0')
    model.load_state_dict(model_dict)

    model.eval()
    with torch.no_grad():
        for _, (input, image_name) in enumerate(test_queue):
            input = Variable(input, volatile=True).cuda()
            image_name = image_name[0].split('\\')[-1].split('.')[0]
            enhance = model(input)

            u_name = '%s.png' % (image_name + '_enhance')
            u_path = save_path + '/' + u_name
            print('processing {}'.format(u_name))
            save_images(enhance, u_path)




if __name__ == '__main__':
    main()
