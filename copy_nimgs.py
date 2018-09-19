import os
import os.path as op
import shutil
from glob import glob

zstats = dict(anticipation='6', faces='8', gstroop='3', harriri='3',
              workingmemory='3')

this_dir = '/home/lsnoek1/projects/CrossingBorders'
base_dir = '/home/lsnoek1/projects/PIOP1_vm/firstlevel'
task_dirs = [d for d in glob(op.join(this_dir, 'selected_imgs', '*')) if op.isdir(d)]

for task_dir in task_dirs:
    task = op.basename(task_dir)
    
    dest_dir = op.join(this_dir, 'all_nimgs', task)
    if not op.isdir(dest_dir):
        os.makedirs(dest_dir)

    imgs = glob(op.join(task_dir, '*.png'))
    for img in imgs:
        sub_name = op.basename(img).split('_')[-1].split('.')[0]
        feat_dir = op.join(base_dir, task, 'BETWEEN', sub_name)
        nimg = glob(op.join(feat_dir, '*', '*.feat', 'stats', 'zstat%s.nii.gz' % zstats[task]))[0]
        
        new_name = sub_name + '_' + op.basename(nimg).replace('.nii.gz', '_%s.nii.gz' % task)
        shutil.copyfile(nimg, op.join(dest_dir, new_name))
