#!/usr/bin/env bash

set -euo pipefail

# Usage:
#   ./upload_checkpoints.sh model_one model_two
#
# Dummy example:
#   ./upload_checkpoints.sh diffusion_bimanual-so101-fold-towel_dummyA diffusion_bimanual-so101-fold-towel_dummyB
#
# Optional range control:
#   START=10000 END=50000 STEP=10000 ./upload_checkpoints.sh model_one model_two
#
# If you want to hardcode multiple defaults, edit DEFAULT_MODELS like this:
#   DEFAULT_MODELS=(
#     "diffusion_bimanual-so101-fold-towel_80"
#     "diffusion_bimanual-so101-fold-towel_dummyA"
#   )
DEFAULT_MODELS=(
    "diffusion_bimanual-so101-fold-towel_100"
    "diffusion_bimanual-so101-fold-towel_80"
    "diffusion_bimanual-so101-fold-towel_60"
    "diffusion_bimanual-so101-fold-towel-v3-60"
    "diffusion_bimanual-so101-fold-towel-v3_60-v4_20-v5_20"
    "diffusion_bimanual-so101-fold-towel-v3_60-v4_40-v5_40"
    "diffusion_bimanual-so101-fold-towel-v3_60-v4_60-v5_60"
    "diffusion_bimanual-so101-fold-towel_40"
    )

START="${START:-10000}"
END="${END:-100000}"
STEP="${STEP:-10000}"

if (( $# > 0 )); then
  MODELS=("$@")
else
  MODELS=("${DEFAULT_MODELS[@]}")
fi

echo "Models: ${MODELS[*]}"
echo "Range: ${START} -> ${END} (step ${STEP})"

for MODEL in "${MODELS[@]}"; do
  echo "== Model: ${MODEL} =="

  for ((ckpt=START; ckpt<=END; ckpt+=STEP)); do
    CKPT="$(printf "%06d" "${ckpt}")"
    SRC="outputs/train/${MODEL}/checkpoints/${CKPT}/pretrained_model"
    DST="humjie/${MODEL}-${CKPT}"

    if [[ ! -d "${SRC}" ]]; then
      echo "[skip] missing directory: ${SRC}"
      continue
    fi

    echo "[upload] ${DST} <- ${SRC}"
    hf upload "${DST}" "${SRC}"
  done
done

echo "Done."