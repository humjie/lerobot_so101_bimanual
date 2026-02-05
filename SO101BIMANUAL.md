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
  --dataset.repo_id=humjie/bimanual-so101-fold-towel \
  --dataset.num_episodes=120 \
  --dataset.single_task="Fold towel"

huggingface-cli upload humjie/bimanual-so101-fold-towel ~/.cache/huggingface/lerobot/humjie/bimanual-so101-fold-towel --repo-type dataset


lerobot-replay \
  --robot.type=bi_so100_follower \
  --robot.left_arm_port=/dev/so101_follower_left \
  --robot.right_arm_port=/dev/so101_follower_right \
  --robot.id=bimanual_follower \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel \
  --dataset.episode=0

lerobot-train \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel \
  --policy.type=diffusion \
  --output_dir=outputs/train/diffusion_bimanual-so101-fold-towel \
  --job_name=diffusion_bimanual-so101-fold-towel \
  --policy.device=cuda \
  --policy.repo_id=humjie/diffusion_bimanual-so101-fold-towel

lerobot-train \
  --dataset.repo_id=humjie/bimanual-so101-fold-towel \
  --policy.type=diffusion \
  --output_dir=outputs/train/diffusion_bimanual-so101-fold-towel \
  --job_name=diffusion_bimanual-so101-fold-towel \
  --policy.device=cuda \
  --policy.repo_id=humjie/diffusion_bimanual-so101-fold-towel \
  --batch_size=8 \
  --num_workers=2 \
  --save_freq=1000

lerobot-train \
  --config_path=outputs/train/diffusion_bimanual-so101-fold-towel/checkpoints/last/pretrained_model/train_config.json \
  --resume=true \
  --save_freq=1000



huggingface-cli upload humjie/diffusion_bimanual-so101-fold-towel \
  outputs/train/diffusion_bimanual-so101-fold-towel/checkpoints/last/pretrained_model



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
  --dataset.repo_id=humjie/eval_diffusion_bimanual-so101-fold-towel \
  --dataset.single_task="Fold towel" \
  --policy.path=outputs/train/diffusion_bimanual-so101-fold-towel/checkpoints/last/pretrained_model


  --teleop.type=bi_so100_leader \
  --teleop.left_arm_port=/dev/so101_leader_left \
  --teleop.right_arm_port=/dev/so101_leader_right \
  --teleop.id=bimanual_leader



sudo apt install libnvidia-common-590 libnvidia-gl-590 nvidia-driver-590 -y