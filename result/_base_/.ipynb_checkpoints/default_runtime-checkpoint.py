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
load_from='/root/autodl-tmp/mask2former_internimage_h_896_80k_cocostuff164k.pth'
resume_from = None
workflow = [('train', 8)]
cudnn_benchmark = True
