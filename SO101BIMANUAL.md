lerobot-teleoperate \
  --robot.type=bi_so100_follower \
  --robot.left_arm_port=/dev/so101_follower_left \
  --robot.right_arm_port=/dev/so101_follower_right \
  --robot.id=bimanual_follower \
  --teleop.type=bi_so100_leader \
  --teleop.left_arm_port=/dev/so101_leader_left \
  --teleop.right_arm_port=/dev/so101_leader_right \
  --teleop.id=bimanual_leader \
  --display_data=true \
  --robot.cameras='{
    top: {"type": "opencv", "index_or_path": "/dev/video6", "width": 640, "height": 480, "fps": 30},
    right: {"type": "opencv", "index_or_path": "/dev/video4", "width": 640, "height": 480, "fps": 30},
    left: {"type": "opencv", "index_or_path": "/dev/video2", "width": 640, "height": 480, "fps": 30}
  }'

lerobot-record \
  --robot.type=bi_so100_follower \
  --robot.left_arm_port=/dev/so101_follower_left \
  --robot.right_arm_port=/dev/so101_follower_right \
  --robot.id=bimanual_follower \
  --teleop.type=bi_so100_leader \
  --teleop.left_arm_port=/dev/so101_leader_left \
  --teleop.right_arm_port=/dev/so101_leader_right \
  --teleop.id=bimanual_leader \
  --display_data=true \
  --robot.cameras='{
    top: {"type": "opencv", "index_or_path": "/dev/video6", "width": 640, "height": 480, "fps": 30},
    right: {"type": "opencv", "index_or_path": "/dev/video4", "width": 640, "height": 480, "fps": 30},
    left: {"type": "opencv", "index_or_path": "/dev/video2", "width": 640, "height": 480, "fps": 30}
  }' \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel-v5 \
  --dataset.num_episodes=60 \
  --dataset.single_task="Fold towel"

hf upload humjie/bimanual-so101-fold-towel-v5 ~/.cache/huggingface/lerobot/humjie/bimanual-so101-fold-towel-v5 --repo-type dataset


lerobot-replay \
  --robot.type=bi_so100_follower \
  --robot.left_arm_port=/dev/so101_follower_left \
  --robot.right_arm_port=/dev/so101_follower_right \
  --robot.id=bimanual_follower \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel \
  --dataset.episode=0

lerobot-train \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel-v3 \
  --policy.type=diffusion \
  --output_dir=outputs/train/diffusion_bimanual-so101-fold-towel-v3-60 \
  --job_name=diffusion_bimanual-so101-fold-towel-v3-60 \
  --policy.device=cuda \
  --policy.repo_id=humjie/diffusion_bimanual-so101-fold-towel-v3-60 \
  --batch_size=8 \
  --num_workers=8 \
  --policy.use_amp=true \
  --save_freq=10000 \
  --eval_freq=10000 \
  --steps=100000 \
  --wandb.enable=true \
  --resume=true

lerobot-train \
  --config_path=outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/last/pretrained_model/train_config.json \
  --resume=true


hf download humjie/bimanual-so101-fold-towel-v4 --local-dir ~/.cache/huggingface/lerobot/humjie/bimanual-so101-fold-towel-v4 --repo-type dataset


lerobot-edit-dataset \
    --repo_id humjie/bimanual-so101-fold-towel-v4 \
    --operation.type split \
    --operation.splits '{"20": 0.3333333333, "40": 0.6666666666}'

lerobot-edit-dataset \
    --new_repo_id humjie/bimanual-so101-fold-towel-v3_20-v4_20-v5_20 \
    --operation.type merge \
    --operation.repo_ids "['humjie/bimanual-so101-fold-towel-v3_20', 'humjie/bimanual-so101-fold-towel-v4_20', 'humjie/bimanual-so101-fold-towel-v5_20']"


hf upload humjie/diffusion_bimanual-so101-fold-towel-v2 \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-20-10000/checkpoints/last/pretrained_model

CKPT=020000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model










lerobot-train \
  --config_path=outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/last/pretrained_model/train_config.json \
  --resume=true
CKPT=020000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=030000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=040000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=050000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=060000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=070000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=080000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=090000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
CKPT=100000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3-60-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-60/checkpoints/${CKPT}/pretrained_model
lerobot-train \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel-v3_20-v4_20-v5_20 \
  --policy.type=diffusion \
  --output_dir=outputs/train/diffusion_bbimanual-so101-fold-towel-v3_20-v4_20-v5_20 \
  --job_name=diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20 \
  --policy.device=cuda \
  --policy.repo_id=humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20 \
  --batch_size=8 \
  --num_workers=8 \
  --policy.use_amp=true \
  --save_freq=10000 \
  --eval_freq=10000 \
  --steps=100000 \
  --wandb.enable=true
CKPT=010000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=020000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=030000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=040000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=050000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=060000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=070000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=080000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=090000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model
CKPT=100000
hf upload humjie/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3_20-v4_20-v5_20/checkpoints/${CKPT}/pretrained_model










lerobot-record  \
  --robot.type=bi_so100_follower \
  --robot.left_arm_port=/dev/so101_follower_left \
  --robot.right_arm_port=/dev/so101_follower_right \
  --robot.id=bimanual_follower \
  --robot.cameras='{
    top: {"type": "opencv", "index_or_path": "/dev/video6", "width": 640, "height": 480, "fps": 30},
    right: {"type": "opencv", "index_or_path": "/dev/video4", "width": 640, "height": 480, "fps": 30},
    left: {"type": "opencv", "index_or_path": "/dev/video2", "width": 640, "height": 480, "fps": 30}
  }' \
  --display_data=false \
  --dataset.repo_id=humjie/eval_diffusion_bimanual-so101-fold-towel-v2 \
  --dataset.single_task="Fold towel" \
  --policy.path=outputs/train/diffusion_bimanual-so101-fold-towel-v2/checkpoints/040000/pretrained_model




sudo nano /etc/udev/rules.d/99-lerobot.rules
SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E121998", SYMLINK+="so101_follower_right", MODE="0666"

SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E122112", SYMLINK+="so101_follower_left", MODE="0666"

SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E120945", SYMLINK+="so101_leader_left", MODE="0666"

SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E121687", SYMLINK+="so101_leader_right", MODE="0666"

sudo udevadm control --reload-rules && sudo udevadm trigger


sudo sh -c 'sync; echo 3 > /proc/sys/vm/drop_caches'

lerobot-edit-dataset \
    --repo_id humjie/bimanual-so101-fold-towel-v4 \
    --operation.type delete_episodes \
    --operation.episode_indices "[59]"
