import os
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--trainpath', type=str,
                default='/opt/meituan/cephfs/user/hadoop-mt-ocr/shangcai/data/places2/a',
                help='path to the dataset')
parser.add_argument('--trainoutput', default='places2_train.flist',type=str, help='path to the file list')
parser.add_argument('--testpath', type=str,
                default='/opt/meituan/cephfs/user/hadoop-mt-ocr/shangcai/data/places2/a',
                help='path to the dataset')
parser.add_argument('--testoutput', default='places2_test.flist',type=str, help='path to the file list')
#validation_static_view.flist,train_shuffled.flist
args = parser.parse_args()
ext = {'.JPG', '.JPEG', '.PNG', '.TIF', 'TIFF'}

images = []
for root, dirs, files in os.walk(args.trainpath):
    print('loading ' + root)
    i=-1
    for file in files:
        if os.path.splitext(file)[1].upper() in ext:
            images.append(os.path.join(root, file))


images = sorted(images)
np.savetxt(args.trainoutput, images, fmt='%s')

with open(args.trainoutput, 'r') as f1:
    list1 = f1.readlines()
print(len(list1))

# images = []
# for root, dirs, files in os.walk(args.testpath):
#     print('loading ' + root)
#     i=0
#     for file in files:
#         if os.path.splitext(file)[1].upper() in ext:
#             if i < 50:
#                 images.append(os.path.join(root, file))
#                 i+=1
#
# images = sorted(images)
# np.savetxt(args.testoutput, images, fmt='%s')
#
# with open(args.testoutput, 'r') as f1:
#     list1 = f1.readlines()
# print(len(list1))