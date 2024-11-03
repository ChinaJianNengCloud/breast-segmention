# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='TensorboardLoggerHook',by_epoch=False)
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = '/mnt/f/yinda/qianyi/InternImage-master/InternImage-master/mask2former_internimage_h_896_80k_cocostuff164k.pth'

resume_from = None
workflow = [('train', 1)]
cudnn_benchmark = True
