# The new config inherits a base config to highlight the necessary modification
_base_ = 'faster_rcnn/faster_rcnn_r50_fpn_2x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('background','breast')
data = dict(
    train=dict(
        img_prefix='../data_train/images/train/',
        classes=classes,
        ann_file='../data_train/annotations/train.json'),
    val=dict(
        img_prefix='../data_train/images/test/',
        classes=classes,
        ann_file='../data_train/annotations/test.json'),
    test=dict(
        img_prefix='../data_train/test/images/',
        classes=classes,
        ann_file='../data_train/annotations/test.json'))