# Copyright (c) OpenMMLab. All rights reserved.
from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class YindaDataset(CustomDataset):

    """Yinda dataset
        image color mask,16 class
    """
    CLASSES = (
        'background','breast')

    PALETTE = [[128,128,128],[0,64,0]]

    def __init__(self, **kwargs):
        super(YindaDataset, self).__init__(
            img_suffix='.png', seg_map_suffix='.png',**kwargs)#图片后缀为png，分割结束的名字为