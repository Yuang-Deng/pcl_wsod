test_cfg = dict({
                    'cfg_file' : './configs/baselines/vgg16_voc2007.yaml',
                    'cuda' : True,
                    'dataset' : 'voc2007test',
                    'load_ckpt' : './Outputs/vgg16_voc2007/May27-15-03-05_sjtu-Precision-5820-Tower_step/ckpt/model_step19999.pth',
                    'load_detectron' : None,
                    'multi_gpu_testing' : False,
                    'output_dir' : './Outputs/vgg16_voc2007/May27-15-03-05_sjtu-Precision-5820-Tower_step/output',
                    'range' : None,
                    'set_cfgs' : [],
                    'test_net_file' : './tools/test_net',
                    'vis' : False,
                })