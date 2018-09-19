import os
import os.path as op
import shutil
from glob import glob

zstats = dict(anticipation='6', faces='8', gstroop='3', harriri='3',
              workingmemory='3')

this_dir = '/home/lsnoek1/projects/CrossingBorders/all_imgs'
base_dir = '/home/lsnoek1/projects/PIOP1_vm/firstlevel'
task_dirs = [d for d in glob(op.join(base_dir, '*')) if op.isdir(d)]

for task_dir in task_dirs:
    task = op.basename(task_dir)
    print('task: %s' % task)
    dest_dir = op.join(this_dir, task)
    if not op.isdir(dest_dir):
        os.makedirs(dest_dir)

    imgs = glob(op.join(task_dir, 'BETWEEN', 'sub*', '*', '*.feat',
                        'rendered_thresh_zstat%s.png' % zstats[task]))

    if len(imgs) == 0:
        imgs = glob(op.join(task_dir, 'BETWEEN', 'sub*', '*.feat', 'rendered_thresh_zstat%s.png' % zstats[task]))

    print('number of imgs: %i' % len(imgs))
    for i, img in enumerate(imgs):
        sub_name = op.basename(op.dirname(img)).split('.feat')[0]
        shutil.copyfile(img, op.join(dest_dir, op.basename(img).replace('.png', '_%s.png' % sub_name)))
