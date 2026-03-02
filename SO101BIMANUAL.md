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
  --dataset.repo_id=humjie/bimanual-so101-fold-towel-v4 \
  --dataset.num_episodes=60 \
  --dataset.single_task="Fold towel"

huggingface-cli upload humjie/bimanual-so101-fold-towel-v4 ~/.cache/huggingface/lerobot/humjie/bimanual-so101-fold-towel-v4 --repo-type dataset


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
  --output_dir=outputs/train/diffusion_bimanual-so101-fold-towel-v3-20 \
  --job_name=diffusion_bimanual-so101-fold-towel-v3-20 \
  --policy.device=cuda \
  --policy.repo_id=humjie/diffusion_bimanual-so101-fold-towel-v3-20 \
  --batch_size=4 \
  --num_workers=6 \
  --policy.use_amp=true \
  --save_freq=10000 \
  --eval_freq=10000 \
  --steps=150000 \
  --wandb.enable=true

lerobot-train \
  --config_path=outputs/train/diffusion_bimanual-so101-fold-towel-v3-20/checkpoints/last/pretrained_model/train_config.json \
  --resume=true



huggingface-cli upload humjie/diffusion_bimanual-so101-fold-towel-v2 \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-20-10000/checkpoints/last/pretrained_model

CKPT=020000
huggingface-cli upload humjie/diffusion_bimanual-so101-fold-towel-v3-20-${CKPT} \
  outputs/train/diffusion_bimanual-so101-fold-towel-v3-20/checkpoints/${CKPT}/pretrained_model



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
SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E121998", SYMLINK+="so101_follower_right"

SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E122112", SYMLINK+="so101_follower_left"

SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E120945", SYMLINK+="so101_leader_left"

SUBSYSTEM=="tty", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="55d3", ATTRS{serial}=="5B3E121687", SYMLINK+="so101_leader_right"

sudo udevadm control --reload-rules && sudo udevadm trigger


sudo sh -c 'sync; echo 3 > /proc/sys/vm/drop_caches'

lerobot-edit-dataset \
    --repo_id humjie/bimanual-so101-fold-towel-v4 \
    --operation.type delete_episodes \
    --operation.episode_indices "[59]"